#  PoC — Validation Scenarios for SIGMA Rules

Scripts used to validate detection of Sigma rules 100001 and 100002 in Wazuh.

 **Warning**: intended for **isolated lab environments only**.

##  Scenarios

| # | Script | Vector | MITRE | Triggered Rule |
|---|---|---|---|---|
| 1 | `01_nikto_scan.sh` | Web Reconnaissance | T1033 | 100001 |
| 2 | `02_dns_exfiltration.sh` | DNS Exfiltration | T1190 | 100002 |

##  Usage

```bash
# Web reconnaissance
bash 01_nikto_scan.sh <TARGET_IP>

# DNS exfiltration
bash 02_dns_exfiltration.sh