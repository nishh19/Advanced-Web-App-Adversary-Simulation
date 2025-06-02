# 🛡️ Advanced Web App Adversary Simulation: OWASP Juice Shop Exploitation

> A full-chain Red Team simulation using OWASP Top 10 + MITRE ATT\&CK mapped attack paths

![Red Team](https://img.shields.io/badge/type-Red%20Team-critical?style=for-the-badge\&logo=hackthebox)
![OWASP](https://img.shields.io/badge/OWASP-Top%2010-blueviolet?style=for-the-badge\&logo=owasp)
![MITRE ATT\&CK](https://img.shields.io/badge/MITRE%20ATT%26CK-Mapped-yellow?style=for-the-badge)

This project demonstrates a Red Team–style simulation against a deliberately vulnerable web application [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) highlighting real-world attack chains that map to **OWASP Top 10** and **MITRE ATT\&CK** tactics.

📍 **Target**: OWASP Juice Shop (Docker-hosted)
🖥️ **Attacker**: Kali Linux (Manual + Scripted Attacks)
🧪 **Approach**: Manual exploitation + Python automation + Burp Suite + ZAP scanning

---

## 🎯 Objectives

* Simulate a real-world adversary compromising a vulnerable e-commerce app.
* Chain OWASP Top 10 vulnerabilities for maximum impact.
* Document findings as a Red Team operator: screenshots, payloads, and mapped tactics.
* Include automation to demonstrate offensive scripting proficiency.

---

## 🔍 Key Exploitation Findings

| ID | Vulnerability                               | Impact                      | OWASP Mapping                      | MITRE ATT\&CK            |
| -- | ------------------------------------------- | --------------------------- | ---------------------------------- | ------------------------ |
| 01 | 🔓 **SQL Injection Login**                  | Admin Access                | A1: Injection                      | TA0001 Initial Access    |
| 02 | 🕵️ **IDOR - Basket Access**                | Customer Data Leakage       | A5: Broken Access Control          | TA0009 Collection        |
| 03 | 📥 **Path Traversal to Confidential Docs**  | Sensitive File Disclosure   | A5: Broken Access Control          | TA0006 Credential Access |
| 04 | 💥 **XSS to Steal `document.cookie`**       | Session Hijack              | A7: XSS                            | TA0006 Credential Access |
| 05 | 🔓 **Registration Logic Flaw**              | Bypasses Input Validation   | A1: Broken Access Control          | TA0003 Persistence       |
| 06 | 💣 **Captcha Bypass (Python)**              | Feedback Spam               | A2: Broken Auth                    | TA0002 Execution         |
| 07 | 💸 **Price Manipulation (Negative Qty)**    | Fraudulent Credit           | A4: Insecure Design                | TA0040 Impact            |
| 08 | 🧨 **FTP - Malware URLs Discovered**        | Malware Hosting Discovery   | A6: Security Misconfig             | TA0011 Command & Control |
| 09 | 📧 **User Enumeration via Forgot Password** | Valid Usernames Identified  | A7: Identification & Auth Failures | TA0001 Initial Access    |
| 10 | 🛡️ **Missing Security Headers (CURL)**     | Defense Evasion Opportunity | A6: Security Misconfig             | TA0005 Defense Evasion   |
| 11 | 🧪 **OWASP ZAP Full Scan**                  | Vulnerability Landscape     | All Categories                     | TA0001 Reconnaissance    |

---

## 📂 Repository Structure

```plaintext
📁 Advanced-Web-App-Adversary-Simulation
├── 📁 [findings](findings/)
│   ├── [01-sqli-login](findings/01-sqli-login/)
│   ├── [02-idor-basket-access](findings/02-idor-basket-access/)
│   ├── [03-path-traversal-confidential-docs](findings/03-path-traversal-confidential-docs/)
│   ├── [04-xss-document-cookie](findings/04-xss-document-cookie/)
│   ├── [05-registration-logic-flaw](findings/05-registration-logic-flaw/)
│   ├── [06-captcha-bypass-feedback-spam](findings/06-captcha-bypass-feedback-spam/)
│   ├── [07-price-manipulation-rich-order](findings/07-price-manipulation-rich-order/)
│   ├── [08-ftp-malware-links](findings/08-ftp-malware-links/)
│   ├── [09-user-enumeration-forgot-pass](findings/09-user-enumeration-forgot-pass/)
│   ├── [10-missing-security-headers](findings/10-missing-security-headers/)
│   └── [11-owasp-zap-automated-scan](findings/11-owasp-zap-automated-scan/)
├── 📁 [automation](automation/)
│   └── feedback_spam_script.py
├── 📁 [zap_reports](zap_reports/)
│   ├── zap_scan_report.html
│   ├── normalize.css
│   ├── main.css
│   └── colors.css
├── README.md
```

Each `findings/` subfolder contains:

* ✅ Exploit steps with description
* 📸 Screenshots
* 🔐 Vulnerability impact
* 🔁 Remediation recommendations

---

## ⚙️ Tool Stack

* 🔎 [Burp Suite](https://portswigger.net/burp): Intercept, manipulate HTTP requests
* 🐍 [Python Requests](https://pypi.org/project/requests/): Automated feedback spam via CAPTCHA bypass
* ⚔️ Kali Linux: Attack platform
* 🛡️ [OWASP ZAP](https://www.zaproxy.org/): Automated security scanning
* 🐳 [Docker](https://www.docker.com/): Hosting Juice Shop locally
* 📸 Manual Testing: UI and DevTools based findings

---

## 💡 Why This Project Stands Out

* Shows practical offensive security skills with **clear mapping to OWASP & MITRE**.
* Includes **custom Python automation** to bypass frontend restrictions.
* Structured like a **real-world Red Team report**, not just a CTF dump.
* 100% reproducible using open-source tools.

---

## 🧭 How to Reproduce

1. Run Juice Shop via Docker:
   `docker run -d -p 3000:3000 bkimminich/juice-shop`
2. Attack from Kali Linux via browser, Burp, or script.
3. Capture screenshots, logs, tokens, responses for each vulnerability.
4. Automate when possible to simulate adversary behavior.

---

## 📈 Key Takeaways

* Chaining low/medium vulnerabilities can simulate high-impact breaches.
* OWASP Juice Shop is perfect for red team skill demonstration.
* MITRE ATT\&CK mapping elevates technical findings to strategic context.
* Reproducible format highlights both manual and automated attacker behaviors.

---

This simulation reflects how overlooked web flaws—when chained together—can lead to significant business impact. In a real-world scenario, these could compromise **PII**, **revenue**, and **system trust**.

> ✅ Built to demonstrate practical security testing, automation, and reporting proficiency—all in one project.

---

Here's your updated executive summary with the contact email added at the end:

---

## 📬 Contact

Feel free to connect if you'd like to discuss this project, red teaming, or offensive web app security.
📧 **Email**: [pashtenisha33@gmail.com](mailto:pashtenisha33@gmail.com)



