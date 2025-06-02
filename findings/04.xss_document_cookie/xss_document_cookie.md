
# 🚨 Finding: Cross-Site Scripting (XSS) via Search Field – JavaScript Execution

## Summary

A **reflected Cross-Site Scripting (XSS)** vulnerability was discovered in the search functionality of OWASP Juice Shop. The application fails to sanitize user input before rendering it in the DOM, allowing attackers to inject and execute arbitrary JavaScript. This leads to full control over the victim's browser session within the application context.

> 🔥 **Business Impact**: If an attacker lures an authenticated user into clicking a malicious search link, they can steal session cookies, impersonate users, and perform unauthorized transactions—effectively bypassing authentication controls.

---

## 💡 Exploit Payload

```html
<iframe src=javascript:alert(document.cookie)>
````

* The payload abuses the unsanitized search parameter.
* It renders an iframe that triggers `alert(document.cookie)` in the victim’s browser.
* This demonstrates access to sensitive session data.

---

## 🛠️ Exploitation Steps

1. Navigate to:

   ```
   http://192.168.0.105:3000/#/search
   ```

2. Inject the payload in the search bar:

   ```
   <iframe src=javascript:alert(document.cookie)>
   ```

3. Observe the JavaScript execution—an alert box pops up with the document's cookies.

📸 Screenshot: `xss-success.png`

---

## 💣 Impact

| Vector                       | Risk                                                            |
| ---------------------------- | --------------------------------------------------------------- |
| 🕵️‍♀️ Session Hijack        | If cookies are not `HttpOnly`, attacker can hijack sessions.    |
| 🎭 Identity Impersonation    | Attacker can act as the victim inside the application.          |
| 📩 Phishing Payload Delivery | XSS can deliver phishing forms, keyloggers, or malware loaders. |
| 📉 Reputational Damage       | XSS can damage user trust, trigger legal actions (GDPR etc).    |

---

## 🎯 Real-World Attack Scenario

An attacker crafts this malicious search URL:

```
http://192.168.0.105:3000/#/search?q=<iframe src=javascript:alert(document.cookie)>
```

They send it via email or message. When a logged-in user clicks the link, their browser executes the script, exposing their session cookie.

> If the attacker replaces `alert()` with `fetch()` or uses an exfiltration endpoint, they can silently steal credentials, sessions, or PII.

---

## 🧪 Security Test Case

| Test Input                         | Expected Behavior            |
| ---------------------------------- | ---------------------------- |
| `<script>alert(1)</script>`        | Should be neutralized        |
| `<iframe src=javascript:alert(1)>` | Should be blocked or encoded |
| `<img src=x onerror=alert(1)>`     | Should not trigger           |
| `<svg onload=alert(1)>`            | Should not execute           |

All of these currently execute in Juice Shop — confirming a critical failure of input/output encoding.

---

## 🔐 Recommendations

1. **Contextual Output Encoding**
   Use libraries like DOMPurify or framework-native sanitizers to encode input before injecting into HTML/JS contexts.

2. **Input Validation**
   Block dangerous characters (`<`, `>`, `"`, `'`, `(`, `)`, `;`) where not necessary.

3. **Set Security Headers**

   * `Content-Security-Policy`: Prevent inline JS execution.
   * `X-XSS-Protection`: Mitigate older browser execution.
   * `HttpOnly`: Mark session cookies as `HttpOnly`.

4. **XSS Audits**
   Perform ongoing dynamic scans with tools like OWASP ZAP and Burp Suite.

---

## 🔗 References

* [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Prevention_Cheat_Sheet.html)
* [OWASP Juice Shop XSS Challenges](https://owasp.org/www-project-juice-shop/)

---

## 🧠 MITRE ATT\&CK Mapping

| ID        | Technique                                     |
| --------- | --------------------------------------------- |
| T1059.007 | Command and Scripting Interpreter: JavaScript |
| T1086     | Scripting                                     |

---

## 📚 OWASP Top 10 Mapping

| ID       | Category        |
| -------- | --------------- |
| A03:2021 | Injection (XSS) |

