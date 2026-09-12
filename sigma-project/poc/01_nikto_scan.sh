#!/bin/bash
# =====================================================================
# PoC 1 — Web Scan with Nikto
# MITRE ATT&CK: T1033 (System Owner/User Discovery)
# Expected detection: Sigma Rule 100001 (Level 10)
# =====================================================================

# Replace <TARGET_IP> with your Ubuntu target machine IP
TARGET_IP="${1:-192.168.234.131}"

echo "[*] Starting Nikto scan against http://$TARGET_IP..."
nikto -h "http://$TARGET_IP"

echo "[+] Scan completed — Level 10 alert expected (rule 100001)"