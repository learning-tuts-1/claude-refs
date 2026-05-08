---
name: cloudflare-r2
description: Cloudflare R2 S3-compatible storage — signed URLs, file uploads, bucket management for .NET. Use when working on file storage, downloads, or signed URL generation.
---

# Cloudflare R2 Storage

R2 (S3-compatible) storage — file uploads, signed URLs for secure downloads.

## Architecture

```
Client --> Backend (Signed URL) --> Cloudflare R2
  |                                      |
  +------ Direct download (signed URL) --+
```

## Configuration

```json
{
  "CloudflareR2": {
    "AccountId": "your-account-id",
    "AccessKeyId": "your-access-key",
    "SecretAccessKey": "your-secret-key",
    "BucketName": "your-bucket",
    "PublicUrl": "https://pub-xxx.r2.dev"
  }
}
```

## Key Concepts

- **R2StorageService** implements `IStorageService` using `IAmazonS3` client
- **ServiceURL** format: `https://{AccountId}.r2.cloudflarestorage.com`
- **ForcePathStyle = true** required for R2 compatibility
- **Signed URLs** via `GetPreSignedURL` with expiration (15-60 min)
- **File keys** follow pattern: `{category}/{handle}/{filename}`

## Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| 403 Forbidden | Wrong credentials | Verify AccessKeyId/SecretAccessKey |
| URL expired | Expiration too short | Increase expirationMinutes |
| CORS error | Missing R2 CORS config | Add origins in R2 dashboard |
| File not found | Wrong key pattern | Check category-to-key mapping |

## Security

1. Never expose raw bucket URLs — always use signed URLs
2. Short expiration times (15-60 min)
3. Verify ownership before generating URL
4. Log downloads for analytics and abuse detection
5. Rate limit URL generation
