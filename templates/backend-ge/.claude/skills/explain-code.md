# explain-code - კოდის ახსნა

## როდის გამოვიყენოთ
როცა მომხმარებელი ითხოვს კოდის ახსნას, ფუნქციის გარჩევას, ან ლოგიკის გაგებას.

## ფორმატი

### 1. მოკლე აღწერა (1-2 წინადადება)
რას აკეთებს ეს კოდი?

### 2. ASCII დიაგრამა
```
Input → [Process A] → [Process B] → Output
            │
            ▼
       [Side Effect]
```

### 3. ნაბიჯ-ნაბიჯ
```
ნაბიჯი 1: რა ხდება პირველად
ნაბიჯი 2: რა ხდება მერე
ნაბიჯი 3: რას აბრუნებს
```

### 4. Gotchas (პოტენციური პრობლემები)
- რაზე უნდა ვიყოთ ფრთხილად?
- Edge cases
- Performance considerations

### 5. ანალოგია (სურვილისამებრ)
რეალური სამყაროს მაგალითი რომ უკეთ გასაგები იყოს.

## წესები

- **ქართულად** ახსენი ბიზნეს ლოგიკა
- **ინგლისურად** დატოვე ტექნიკური ტერმინები
- **ASCII დიაგრამა** სავალდებულოა data flow-სთვის
- **არ გაამარტივო ზედმეტად** - მომხმარებელი პროგრამისტია
- **Gotchas** ნაწილი სავალდებულოა

## მაგალითი

```
User: "ახსენი ეს middleware"

## რას აკეთებს
JWT Token-ს ვალიდაციას უკეთებს ყოველ request-ზე და User claims-ს ამატებს HttpContext-ში.

## Flow
```
HTTP Request
     │
     ▼
[Read Authorization Header]
     │
     ├─ No Token → 401 Unauthorized
     │
     ▼
[Validate JWT]
     │
     ├─ Invalid/Expired → 401
     │
     ▼
[Extract Claims]
     │
     ▼
[Set HttpContext.User]
     │
     ▼
next(context) → Controller
```

## Gotchas
- Token expired → refresh token flow უნდა გაეშვას client-ზე
- ClaimTypes.NameIdentifier → UserId, არა UserName
- Middleware-ის რიგი მნიშვნელოვანია - Auth უნდა იყოს CORS-ის შემდეგ
```
