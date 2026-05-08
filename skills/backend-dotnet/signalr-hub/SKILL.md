---
name: signalr-hub
description: SignalR real-time communication — hubs, groups, JWT auth for WebSocket. Use when working on chat, real-time messaging, or WebSocket connections.
---

# SignalR Hub

Real-time bidirectional communication via WebSocket.

## Architecture

```
Client <--> Hub (ChatHub) <--> Groups (Sessions)
                  |
              Database (Messages)
```

## Hub Pattern

```csharp
[Authorize]
public class ChatHub : Hub
{
    public override async Task OnConnectedAsync()
    {
        var userId = Context.User?.FindFirst(ClaimTypes.NameIdentifier)?.Value;
        await Groups.AddToGroupAsync(Context.ConnectionId, $"user_{userId}");
        await base.OnConnectedAsync();
    }

    public async Task JoinSession(string sessionId)
    {
        await Groups.AddToGroupAsync(Context.ConnectionId, $"session_{sessionId}");
    }

    public async Task SendMessage(string sessionId, string content)
    {
        var message = await _chatService.SendMessageAsync(sessionId, GetUserId(), content);
        await Clients.Group($"session_{sessionId}").SendAsync("ReceiveMessage", message);
    }
}
```

## Client Integration (TypeScript)

```typescript
const connection = new signalR.HubConnectionBuilder()
  .withUrl("/hubs/chat", { accessTokenFactory: () => accessToken })
  .withAutomaticReconnect([0, 2000, 5000, 10000, 30000])
  .build();

connection.on("ReceiveMessage", (message) => { /* handle */ });
await connection.start();
```

## JWT Authentication for WebSocket

```csharp
options.Events = new JwtBearerEvents
{
    OnMessageReceived = context =>
    {
        var accessToken = context.Request.Query["access_token"];
        if (!string.IsNullOrEmpty(accessToken) && context.HttpContext.Request.Path.StartsWithSegments("/hubs"))
            context.Token = accessToken;
        return Task.CompletedTask;
    }
};
```

## Group Patterns

```csharp
await Clients.Group($"user_{userId}").SendAsync("Notification", data);
await Clients.Group($"session_{sessionId}").SendAsync("Message", message);
await Clients.OthersInGroup($"session_{sessionId}").SendAsync("Typing", userId);
```

## Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| 401 on connect | Token not passed | Use accessTokenFactory |
| CORS error | Missing AllowCredentials | Add to CORS policy |
| Messages not received | Not in group | Call JoinSession first |
| Reconnect fails | Token expired | Refresh token before reconnect |
