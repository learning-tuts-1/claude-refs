---
name: firebase-admin
description: Firebase Admin SDK for .NET backend — ID token verification and social login. Use when working on social auth, token verification, or Firebase integration.
---

# Firebase Admin SDK

ID token verification from social sign-in providers.

## Architecture

```
Client (ID Token) --> Backend (Verify) --> Firebase (Google)
                           |
                     Create User + JWT Tokens
```

## Key Concepts

- **NuGet:** `FirebaseAdmin` package
- **Init:** `FirebaseApp.Create()` with `GoogleCredential.FromFile()`
- **Verify:** `FirebaseAuth.DefaultInstance.VerifyIdTokenAsync(idToken)`
- **FirebaseUserInfo:** Uid, Email, Name, Picture, Provider, EmailVerified
- **Provider:** nested in `token.Claims["firebase"]["sign_in_provider"]`
- **Flow:** Verify token -> Find/Create user -> Generate JWT tokens

## Providers

| Provider | `sign_in_provider` value |
|----------|--------------------------|
| Google | `google.com` |
| Facebook | `facebook.com` |
| Email/Password | `password` |

## Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| `InvalidIdToken` | Wrong project ID | Check Firebase config |
| `ExpiredIdToken` | Token > 1 hour old | Client should refresh |
| `CredentialNotFound` | Missing JSON file | Check path in appsettings |
