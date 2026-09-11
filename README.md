#  SIGMA Rules Creation and Deployment with Wazuh

![Wazuh](https://img.shields.io/badge/Wazuh-SIEM-blue)
![Sigma](https://img.shields.io/badge/Sigma-Rules-orange)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

> Design of **SIGMA** detection rules (portable YAML format), automated conversion to **Wazuh XML** via a Python script, and validation through real attack scenarios (Web Reconnaissance, DNS Exfiltration).

---

##  Context

Project carried out as part of the **Networks & Internet Protocols** module of the **Master in Intelligent Cybersecurity and Emerging Technologies** at **Mohammed V University of Rabat — Faculty of Sciences**.

**Team:**
- ILLASS EL-KHABBAOUI
- ABDELKHALEK EL IDRISSI

**Supervisor:** Pr. Sara DIOUANI

**Defense date:** January 13, 2026

---

##  Objectives

- Design **portable** detection rules using the **SIGMA** standard (SIEM-independent).
- Automate **SIGMA → Wazuh** conversion via a Python script.
- Deploy a **SIEM** architecture with Wazuh (Manager + Agent).
- Validate detection through **real attack scenarios** (PoC).
- Map rules to the **MITRE ATT&CK** framework.

---

##  Lab Architecture

| Component | Role |
|---|---|
| **Attacker Machine** | Kali Linux — simulates the threat actor |
| **Target + Monitoring Machine** | Ubuntu Server/Desktop — hosts Wazuh Manager + Agent (all-in-one) |
| **VMware Workstation** | Type 2 hypervisor (NAT/Bridged) |

---

##  Implemented Detection Rules

###  Rule 1 — Web & Network Reconnaissance Detection

**Sigma file:** `rules/sigma/web_recon.yml`

Detects web/network reconnaissance tools based on User-Agent signatures:

| Tool | Description |
|---|---|
| **Nikto** | Open-source web vulnerability scanner |
| **sqlmap** | Automated SQL injection exploitation |
| **Nmap** | Port and service scanner |
| **masscan** | Ultra-fast port scanner |
| **gobuster** | Web directory/file brute-force |

**MITRE ATT&CK:** T1033 (System Owner/User Discovery), attack.discovery

**Alert level:** High

---

###  Rule 2 — DNS Exfiltration (Out-of-Band) Detection

**Sigma file:** `rules/sigma/dns_interaction.yml`

Detects DNS queries to domains known to host malicious interaction services:

| Domain | Service |
|---|---|
| `burpcollaborator.net` | Burp Suite Collaborator |
| `canarytokens.com` | Intrusion detection tokens |
| `ceye.io` | DNS/HTTP out-of-band monitoring |
| `interact.sh` | Open-source OAST service |
| `oast.fun`, `oast.live` | OAST services |
| `oastify.com` | Burp Suite Collaborator |
| `requestbin.net` | HTTP/DNS request capture |
| `dnslog.cn` | DNS logging service |

**MITRE ATT&CK:** T1190 (Exploit Public-Facing Application)

**Alert level:** High

---

## 🔄 Full Detection Pipeline: From Sigma to Wazuh
