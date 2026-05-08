---
name: stripe-payments
description: Stripe payment integration — Checkout Sessions, webhooks, payment processing for .NET. Use when working on payments, checkout flow, or Stripe webhooks.
---

# Stripe Payments

Checkout Sessions, Webhooks, and Payment processing.

## Checkout Session Flow

```
Frontend (Checkout) --> Backend (Create) --> Stripe (Hosted)
                                                  |
Database (Update) <-- Webhook (Handle) <-- Payment (Complete)
```

## Create Checkout Session

```csharp
var options = new SessionCreateOptions
{
    PaymentMethodTypes = new List<string> { "card" },
    LineItems = items.Select(item => new SessionLineItemOptions
    {
        PriceData = new SessionLineItemPriceDataOptions
        {
            UnitAmount = (long)(item.Price * 100),
            Currency = "usd",
            ProductData = new SessionLineItemPriceDataProductDataOptions { Name = item.Name }
        },
        Quantity = item.Quantity
    }).ToList(),
    Mode = "payment",
    SuccessUrl = _settings.SuccessUrl,
    CancelUrl = _settings.CancelUrl,
    Metadata = new Dictionary<string, string> { { "userId", userId.ToString() } }
};
var session = await new SessionService().CreateAsync(options);
```

## Webhook Handler

```csharp
[HttpPost("webhook")]
public async Task<IActionResult> HandleWebhook()
{
    var json = await new StreamReader(HttpContext.Request.Body).ReadToEndAsync();
    var stripeEvent = EventUtility.ConstructEvent(json, Request.Headers["Stripe-Signature"], _settings.WebhookSecret);

    switch (stripeEvent.Type)
    {
        case Events.CheckoutSessionCompleted:
            await HandleCheckoutCompleted(stripeEvent.Data.Object as Session);
            break;
        case Events.PaymentIntentPaymentFailed:
            await HandlePaymentFailed(stripeEvent.Data.Object as PaymentIntent);
            break;
    }
    return Ok();
}
```

## Important Events

| Event | Action |
|-------|--------|
| `checkout.session.completed` | Update order, grant access |
| `payment_intent.succeeded` | Log, analytics |
| `payment_intent.payment_failed` | Notify user |
| `charge.refunded` | Revoke access, update order |

## Local Development

```bash
stripe listen --forward-to localhost:5199/api/payments/webhook
stripe trigger checkout.session.completed
```

## Test Cards

| Card | Result |
|------|--------|
| 4242424242424242 | Success |
| 4000000000000002 | Decline |
| 4000000000009995 | Insufficient funds |

## Security

1. Never log full card numbers
2. Always verify webhook signatures
3. Use idempotency keys for retry safety
4. Use Stripe Checkout (hosted) for PCI compliance
