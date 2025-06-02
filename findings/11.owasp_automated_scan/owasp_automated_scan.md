

# 🤖 11 – Automated Vulnerability Scan with OWASP ZAP (Active Scan Only)

> 🛡️ **Category:** Automated Reconnaissance
> 🎯 **Target:** [`http://192.168.0.105:3000`](http://192.168.0.105:3000)

---

## 🧰 Tool: OWASP ZAP – Active Scan Mode

**OWASP ZAP** (Zed Attack Proxy) is a flagship OWASP tool used to automatically find security vulnerabilities in web apps during penetration testing. In this case, only the **Active Scan** was performed — meaning no crawling (spider) phase was run. The attack relied on the user-provided entry points.

---

## 🖼️ Screenshots

### ⚙️ Active Scan Running

<img src="zap-active-scan-running.png" alt="OWASP ZAP Active Scan in Progress" width="700" style="border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.2);" />

---


## 📂 ZAP HTML Report

The full vulnerability scan output is included in this repo:

📁 [`zap_report/zap_scan_report.html`](../zap_report/zap_scan_report.html)

To view:

* Open the HTML file in a desktop browser (for best formatting)
* Supports sorting, filtering, and details per alert

---

## 🚨  Vulnerabilities Identified

| Alert Type                                   | Risk Level | Count   |
| -------------------------------------------- | ---------- | ------- |
| Content Security Policy (CSP) Header Not Set | 🟠 Medium  | 57      |
| Cross-Domain Misconfiguration                | 🟠 Medium  | 73      |
| Hidden File Found                            | 🟠 Medium  | 4       |
| Cross-Domain JavaScript File Inclusion       | 🟡 Low     | 98      |
| Timestamp Disclosure (Unix)                  | 🟡 Low     | 158     |
| Suspicious Comments (Information Disclosure) | 🔵 Info    | 2       |
| Modern Web Application Fingerprint           | 🔵 Info    | 50      |
| User Agent Fuzzer                            | 🔵 Info    | 24      |
| **Total Alerts**                             |            | **466** |


---

## 🧠 MITRE ATT\&CK Mapping

| MITRE ID  | Name                       | Relevance                              |
| --------- | -------------------------- | -------------------------------------- |
| T1595.002 | **Vulnerability Scanning** | Automated tools to find web weaknesses |
| T1595.001 | **Service Identification** | Passive clues from HTTP responses      |

---


