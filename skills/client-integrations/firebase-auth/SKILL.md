---
name: firebase-auth
description: Google Sign-In integration with Firebase for client-side apps. Use when working on authentication, login flow, social auth, or token management.
---

# Firebase Authentication

Firebase Auth — Google Sign-In popup, ID token verification with backend.

## Auth Flow

```
User clicks "Sign in with Google"
  -> Firebase popup -> User selects account
  -> Firebase returns ID Token (JWT)
  -> Frontend sends ID Token to Backend /api/auth/social
  -> Backend verifies, creates/finds user
  -> Returns: accessToken + refreshToken
  -> Frontend stores tokens
```

## Key Concepts

- **Popup fallback:** If popup blocked -> redirect method
- **Token refresh:** 401 interceptor auto-refreshes, on failure -> logout
- **Backend verification:** Firebase Admin SDK `VerifyIdTokenAsync()`

## Error Codes

| Error Code | Handling |
|------------|----------|
| `auth/popup-blocked` | Fallback to `signInWithRedirect` |
| `auth/popup-closed-by-user` | Show "Sign in cancelled" |
| `auth/network-request-failed` | Show network error |

## Security

1. Always verify ID token on backend
2. Short access token lifetime (15 min)
3. Handle sign-out everywhere — clear all storage
