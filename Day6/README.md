# HTTP Status Codes in FastAPI

HTTP status codes are three-digit numbers returned by an API to indicate the result of a client's request.

FastAPI uses standard HTTP status codes to communicate whether a request was successful, failed because of the client, or failed because of the server.

---

## HTTP Status Code Categories

| Range | Category | Meaning |
|------:|----------|---------|
| 1xx | Informational | Request is being processed |
| 2xx | Success | Request was successfully processed |
| 3xx | Redirection | Further action is required |
| 4xx | Client Error | Problem with the client's request |
| 5xx | Server Error | Problem occurred on the server |

---

# Important HTTP Status Codes for FastAPI

| Status Code | Name | Common FastAPI Use Case |
|-------------|------|--------------------------|
| `200` | OK | Successful GET, PUT or PATCH request |
| `201` | Created | Successfully created a new resource |
| `204` | No Content | Successful operation with no response body |
| `301` | Moved Permanently | Resource has permanently moved |
| `304` | Not Modified | Cached resource has not changed |
| `400` | Bad Request | Invalid or malformed request |
| `401` | Unauthorized | Authentication is required or credentials are invalid |
| `403` | Forbidden | User is authenticated but does not have permission |
| `404` | Not Found | Requested resource does not exist |
| `405` | Method Not Allowed | HTTP method is not supported for the endpoint |
| `409` | Conflict | Request conflicts with the current resource state |
| `415` | Unsupported Media Type | Unsupported request content type |
| `422` | Unprocessable Content | Request is valid but validation fails |
| `429` | Too Many Requests | Client exceeded the rate limit |
| `500` | Internal Server Error | Unexpected error on the server |
| `502` | Bad Gateway | Invalid response from another/upstream service |
| `503` | Service Unavailable | Server/service is temporarily unavailable |
| `504` | Gateway Timeout | Upstream service took too long to respond |



