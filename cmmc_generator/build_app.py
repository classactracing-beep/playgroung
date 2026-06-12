#!/usr/bin/env python3
"""Build the self-contained HTML app (index.html).

Injects the document content data from the Python modules into
app_template.html so the browser app and the python-docx generator stay
in sync from a single content source. Run after editing any content in
cmmc_gen/, then commit the regenerated index.html.

Usage: python build_app.py
"""

import base64
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from cmmc_gen.practices import DOMAINS, practices
from cmmc_gen.procedures_data import (DOMAIN_GOVERNANCE, DOMAIN_GUIDANCE,
                                      PACKAGES, POLICY_NAMES)
from cmmc_gen.references import COMPLIANCE_REFERENCES, COMPLIANCE_STATEMENT
from cmmc_gen import spp_content

APP_VERSION = "2.0.0"


def _packages_json():
    out = {}
    for code, pkg in PACKAGES.items():
        out[code] = {
            "procedure": {
                "title": pkg["procedure"]["title"],
                "controls": pkg["procedure"]["controls"],
                "sections": [list(s) for s in pkg["procedure"]["sections"]],
            },
            "documents": pkg["documents"],
        }
    return out


def _spp_json():
    def blocks(blks):
        return [list(b) for b in blks]
    return {
        "forward": blocks(spp_content.FORWARD),
        "sections": [[title, blocks(blks)]
                     for title, blks in spp_content.SECTIONS],
    }


def _sample_logo():
    path = os.path.join(HERE, "assets", "sample_logo.png")
    if not os.path.isfile(path):
        return ""
    with open(path, "rb") as fh:
        return "data:image/png;base64," + base64.b64encode(fh.read()).decode()


def main():
    data = {
        "version": APP_VERSION,
        "domains": DOMAINS,
        "policyNames": POLICY_NAMES,
        "governance": DOMAIN_GOVERNANCE,
        "practices": practices(),
        "packages": _packages_json(),
        "guidance": DOMAIN_GUIDANCE,
        "spp": _spp_json(),
        "references": COMPLIANCE_REFERENCES,
        "complianceStatement": COMPLIANCE_STATEMENT,
        "sampleLogo": _sample_logo(),
    }
    blob = json.dumps(data, separators=(",", ":"))
    # Keep the inline JSON safe inside a <script> block.
    blob = blob.replace("</", "<\\/")
    if "—" in blob:
        raise SystemExit("em dash found in content data; remove it first")

    with open(os.path.join(HERE, "app_template.html"), encoding="utf-8") as fh:
        template = fh.read()
    if "__CMMC_DATA__" not in template:
        raise SystemExit("placeholder __CMMC_DATA__ missing from template")
    html = template.replace("__CMMC_DATA__", blob)

    out = os.path.join(HERE, "index.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Wrote {out} ({len(html) / 1024:.0f} KB), app version {APP_VERSION}")


if __name__ == "__main__":
    main()
