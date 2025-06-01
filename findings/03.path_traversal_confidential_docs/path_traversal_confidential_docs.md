
# 🛡️ 03 – Path Traversal: Accessing Confidential Documents

## ✅ Exploit Steps with Description

1. **Navigated to the "About Us" Page**  
   Visited [`/#/about`](http://192.168.0.105:3000/#/about) which lists various policy documents linked from the backend via filenames like `legal.md`.

2. **Intercepted Terms of Use Request in Burp Proxy**  
   Clicked on the "Terms of Use" link and intercepted the request:
```

GET /ftp/legal.md HTTP/1.1

```

3. **Sent Request to Repeater and Modified Path**  
In **Burp Repeater**, changed the path to attempt directory traversal:
```

GET /ftp/../../../../ftp/acquisitions.md HTTP/1.1

```

4. **Successfully Retrieved a Sensitive File**  
Received a `200 OK` response, displaying internal corporate acquisition information:
```

This document contains confidential details about company acquisition plans.

```

5. **Verified Path Traversal Working via Browser or cURL**  
Confirmed this technique could access other unintended `.md` files stored on the server.

---

## 📸 Screenshots

| Stage | Description |
|-------|-------------|
| ![1](./01-about-page-terms-link.png) | "About Us" page with Terms link |
| ![2](./02-burp-proxy-legal.md-request.png) | Burp captured request to `/ftp/legal.md` |
| ![3](./03-repeater-path-traversal-input.png) | Repeater request with `../../../../ftp/acquisitions.md` |
| ![4](./04-repeater-200-ok-aquisitions.png) | Response showing internal acquisition content |
| ![5](./05-browser-confirm-success.png) | Confirmation of access via browser or curl |

---

## 🔐 Vulnerability Impact

- **Confidentiality Breach**: Attackers can retrieve sensitive internal documents not meant for public access.
- **Data Leakage**: Information like acquisition plans, credentials, or server configs may be exposed.
- **Compliance Risk**: Violates data protection standards and internal security policies.

---

## 🔁 Remediation Recommendations

- 🔒 **Validate and sanitize all user-supplied paths on the server side.**
- 🛡️ **Use path whitelisting** rather than allowing arbitrary filenames.
- 🚫 **Restrict access to sensitive folders** like `/ftp` via web server configuration.
- 📦 **Use secure APIs or database calls** instead of exposing filesystem paths.
- 🔍 **Conduct regular code reviews and path traversal testing.**


