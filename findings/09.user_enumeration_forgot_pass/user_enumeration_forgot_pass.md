
# 🚩 Finding 09 – User Enumeration via Forgot Password

---

## 🔍 Overview

During the **Forgot Password** process on Juice Shop (`http://192.168.0.105:3000/#/forgot`), an **information leakage vulnerability** was identified that allows an attacker to **enumerate valid users** based on the UI behavior of security question fields.

---

## 🎯 Steps to Reproduce

| Step | Action                                                 | Result                                                    |
| ---- | ------------------------------------------------------ | --------------------------------------------------------- |
| 1    | Navigate to Forgot Password page                       | `http://192.168.0.105:3000/#/forgot`                      |
| 2    | Enter a **valid email** (e.g., `admin@juice-sh.op`)    | Security question fields become **enabled and editable**  |
| 3    | Enter an **invalid email** (e.g., `test@notexist.com`) | Security question fields stay **greyed out and disabled** |

---

## ⚠️ Why This Matters

This subtle UI difference **exposes the existence of user accounts**, which:

* 💥 **Enables targeted phishing campaigns** by confirming valid emails
* 🔐 Facilitates **credential stuffing and brute-force attacks**
* 🕵️‍♂️ Leaks sensitive internal user data — a direct privacy risk

User enumeration vulnerabilities are **often overlooked but critical** entry points in web application security.

---

## 📷 Evidence
✅ Existing Email – Security Fields Enabled
<img src="../screenshots/existing-email.png" alt="Existing email input behavior" width="450" style="border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.2); margin-bottom: 20px;" />
❌ Non-existing Email – Security Fields Disabled
<img src="../screenshots/non-existing-email.png" alt="Non-existing email input behavior" width="450" style="border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.2);" />
*Note: Security question fields only become interactive for valid users.*

---

## 🧠 MITRE ATT\&CK Mapping

* **T1589.002** – Email Address Harvesting
* **T1110.003** – Credential Stuffing

---

## 🔧 Remediation Recommendations

* Display **generic error messages and UI responses** for all email inputs (e.g., "If the email exists, you will receive a reset link").
* Implement **rate limiting** on forgot password attempts to prevent brute forcing.
* Use **CAPTCHA or other bot-detection mechanisms** on sensitive flows.
* Monitor and log suspicious enumeration attempts for incident response.

---

