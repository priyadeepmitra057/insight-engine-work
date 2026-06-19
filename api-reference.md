# Insight Engine API Reference

This API exposes spend analysis and a chatbot interface. It is completely stateless, relying on the `X-Merchant-Token` header for authentication and tenant isolation.

## Authentication

All endpoints require the `X-Merchant-Token` header.

```http
X-Merchant-Token: your-merchant-token
```

To obtain a token, contact your system administrator. Tokens are hashed on the backend to separate user sessions and contexts.

## Error Handling

All `4xx` and `5xx` errors return a uniform JSON error envelope:

```json
{
  "error": "machine_readable_error_code",
  "message": "Human-readable explanation of the error.",
  "request_id": "a1b2c3d4e5f6"
}
```

Recommended handling in JavaScript:
```javascript
if (!response.ok) {
  const err = await response.json();
  console.error(`[${err.error}] ${err.message} (Trace: ${err.request_id})`);
}
```

---

## Endpoints

### 1. Analyze Statement
**`POST /api/v1/insights/analyze`**

Accepts a CSV bank statement and returns unified spend and passion insights. This also automatically provisions the backend context required for the Chatbot.

**Headers:**
- `X-Merchant-Token` (required)

**Body:**
- `multipart/form-data` with a single `file` field containing the CSV.

**Response (200 OK):**
```json
{
  "run_id": "abcdef123456",
  "passion_status": "success",
  "spend_insights": {
    "insights": [
      {
        "text": "High spend observed in Groceries",
        "tip": "Consider setting a budget.",
        "type": "spending_spike",
        "score": 0.95
      }
    ],
    "stats": {
      "total_transactions": 150,
      "excluded_transactions": 10,
      "exclusion_rate": 0.06
    }
  },
  "passion_insights": {
    "enabled": true,
    "signal_count": 1,
    "signals": [
      {
        "category": "Hobbies",
        "subcategory": "Cycling",
        "display_label": "Cycling Enthusiast",
        "total_spend": 500.0,
        "spend_share_pct": 10.5,
        "merchant_count": 3,
        "active_months": 2,
        "trend": "up",
        "is_suppressed": false,
        "suppression_reason": "",
        "narrative": "Consistent spending on cycling gear."
      }
    ]
  }
}
```

**JavaScript Example (fetch):**
```javascript
const formData = new FormData();
formData.append("file", fileInput.files[0]);

const response = await fetch("/api/v1/insights/analyze", {
  method: "POST",
  headers: {
    "X-Merchant-Token": "user-auth-token-123"
  },
  body: formData
});

const data = await response.json();
console.log(data);
```

---

### 2. Start Chat Session
**`POST /api/v1/chat/start`**

Initialises a chat session using the context from the most recent analysis.

**Headers:**
- `X-Merchant-Token` (required)
- `Content-Type: application/json`

**Body:**
```json
{
  "run_id": "abcdef123456" // Optional: if omitted, uses the most recent run for this token.
}
```

**Response (200 OK):**
```json
{
  "session_id": "session_uuid_here",
  "run_id": "abcdef123456",
  "period": {
    "start_date": "2023-01-01",
    "end_date": "2023-01-31"
  },
  "turns_remaining": 20
}
```

**JavaScript Example (fetch):**
```javascript
const response = await fetch("/api/v1/chat/start", {
  method: "POST",
  headers: {
    "X-Merchant-Token": "user-auth-token-123",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ run_id: "abcdef123456" }) // Optional
});

const sessionData = await response.json();
console.log("Session started:", sessionData.session_id);
```

---

### 3. Send Chat Message
**`POST /api/v1/chat/message`**

Sends a message to the active chat session and returns the AI's response.

**Headers:**
- `X-Merchant-Token` (required)
- `Content-Type: application/json`

**Body:**
```json
{
  "session_id": "session_uuid_here",
  "message": "What did I spend the most on?"
}
```
*Note: `message` must be 512 characters or fewer.*

**Response (200 OK):**
```json
{
  "session_id": "session_uuid_here",
  "answer": "You spent the most on Groceries this month.",
  "turn_number": 1,
  "turns_remaining": 19
}
```

**JavaScript Example (fetch):**
```javascript
const response = await fetch("/api/v1/chat/message", {
  method: "POST",
  headers: {
    "X-Merchant-Token": "user-auth-token-123",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    session_id: "session_uuid_here",
    message: "How much did I spend on dining out?"
  })
});

const reply = await response.json();
console.log("AI says:", reply.answer);
```

---

### 4. Delete Chat Session
**`DELETE /api/v1/chat/session/{session_id}`**

Manually ends and cleans up a chat session.

**Headers:**
- `X-Merchant-Token` (required)

**Response (200 OK):**
```json
{
  "status": "deleted"
}
```

**JavaScript Example (fetch):**
```javascript
const sessionId = "session_uuid_here";
const response = await fetch(`/api/v1/chat/session/${sessionId}`, {
  method: "DELETE",
  headers: {
    "X-Merchant-Token": "user-auth-token-123"
  }
});

if (response.ok) {
  console.log("Session successfully deleted.");
}
```
