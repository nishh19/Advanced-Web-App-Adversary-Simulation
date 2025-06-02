
# 🛡️ 06 – CAPTCHA Bypass & Feedback Spam Automation

## ✅ Exploitation Steps

1. **Accessed the Feedback Form**  
   URL: [`http://192.168.0.105:3000/#/contact`](http://192.168.0.105:3000/#/contact)  
   The page includes a feedback form and a visible CAPTCHA.

2. **Intercepted Feedback Request**  
   Captured the HTTP POST request to `/api/Feedback/` using Burp Suite, noting that:
   - The CAPTCHA token field was present but not validated server-side.
   - Request did **not** enforce rate-limiting or CAPTCHA verification.

3. **Automated the Spam Submission**  
   Wrote a Python script to:
   - Forge feedback messages (e.g., `Fake Promo`, `Injected Review`)
   - Send 10+ requests rapidly in ~20 seconds
   - Completely bypass CAPTCHA and rate limits

4. **Forged Feedback Appeared in UI**  
   Verified spam content appeared on the front-end, proving a complete bypass and automation success.

---

## 📸 Screenshots

<div style="display: flex; flex-direction: column; gap: 10px;">

<img src="./01-original-feedback-form.png" alt="Original feedback form with CAPTCHA" style="border:1px solid #ccc; border-radius:10px; width:70%; max-width:600px;">

<img src="./02-burp-feedback-request.png" alt="Intercepted feedback POST request in Burp" style="border:1px solid #ccc; border-radius:10px; width:70%; max-width:600px;">

<img src="./03-kali-script-submitting.png" alt="Python script in Kali submitting spam requests" style="border:1px solid #ccc; border-radius:10px; width:70%; max-width:600px;">

<img src="./04-success-message-spam.png" alt="Forged feedback accepted and displayed" style="border:1px solid #ccc; border-radius:10px; width:70%; max-width:600px;">

</div>

---

## 🔐 Vulnerability Impact

- 🤖 **CAPTCHA Ineffectiveness**: Fails to prevent bot/spam abuse.
- 💬 **Reputation Risk**: Public feedback page can be flooded with malicious or fake content.
- 🧨 **Potential for Scripted Attacks**: Could be chained with XSS or social engineering.

---

## 🔁 Remediation Recommendations

- ✅ Enforce **server-side CAPTCHA validation** before accepting submissions.
- 🚫 Implement **rate limiting & anti-automation controls** on feedback APIs.
- 🛡️ Use **CSRF tokens** and **IP throttling** to slow automated submissions.
- 📊 Log and monitor suspicious request bursts.

---

> A single CAPTCHA means nothing without server validation. Bots aren’t fooled by visuals—your backend must validate all user interactions.

