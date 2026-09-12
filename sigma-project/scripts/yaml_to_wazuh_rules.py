#!/usr/bin/env python3
"""
Sigma (YAML) -> Wazuh (XML) converter
Project: SIGMA Rules Creation and Deployment with Wazuh
Authors: ABDELKHALEK EL IDRISSI, LILASS EL-KHABBAOUI
Supervisor: Pr. Sara DIOUANI
"""

import sys
import yaml
from xml.etree import ElementTree as ET
from xml.dom import minidom


def load_sigma_rule(yaml_file):
    """Load a Sigma rule in YAML format."""
    with open(yaml_file, 'r') as f:
        return yaml.safe_load(f)


def convert_to_wazuh(sigma_rule, rule_id=100001):
    """Convert a Sigma rule into a Wazuh XML rule."""
    rule = ET.Element("rule", id=str(rule_id), level="10")

    description = ET.SubElement(rule, "description")
    description.text = sigma_rule.get("title", "Sigma Rule")

    detection = sigma_rule.get("detection", {})
    selection = detection.get("selection", {})

    for key, values in selection.items():
        if isinstance(values, list):
            regex = "|".join(values)
            regex_elem = ET.SubElement(rule, "regex")
            regex_elem.text = regex

    tags = sigma_rule.get("tags", [])
    mitre_ids = [t.split(".")[1].upper() for t in tags if t.startswith("attack.t")]
    if mitre_ids:
        mitre = ET.SubElement(rule, "mitre")
        for tid in mitre_ids:
            id_elem = ET.SubElement(mitre, "id")
            id_elem.text = tid

    return rule


def save_xml(rule, output_file):
    """Save the XML rule with proper formatting."""
    xml_str = ET.tostring(rule, encoding="unicode")
    pretty = minidom.parseString(xml_str).toprettyxml(indent="  ")
    with open(output_file, 'w') as f:
        f.write(pretty)


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 yaml_to_wazuh_rules.py <input.yml> <output.xml>")
        sys.exit(1)

    yaml_file, xml_file = sys.argv[1], sys.argv[2]
    sigma_rule = load_sigma_rule(yaml_file)
    wazuh_rule = convert_to_wazuh(sigma_rule)
    save_xml(wazuh_rule, xml_file)
    print(f"[+] Rule converted: {yaml_file} -> {xml_file}")


if __name__ == "__main__":
    main()