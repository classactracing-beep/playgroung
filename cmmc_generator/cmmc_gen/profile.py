"""Load and validate company_profile.json.

The profile carries every branding field used across the SPP, policies,
procedures, and the control mapping matrix. Loading is strict: missing
required fields raise an error so a half-branded binder is never produced.
"""

import json
import os

REQUIRED_FIELDS = [
    "company_legal_name",
    "company_short_name",
    "logo_path",
    "address_line1",
    "address_line2",
    "cage_code",
    "uei",
    "facility_clearance_level",
    "storage_capability",
    "smo_name",
    "smo_title",
    "fso_name",
    "afso_name",
    "itpso_name",
    "isr_name",
    "dcsa_field_office",
    "security_contact_email",
    "security_contact_phone",
]

OPTIONAL_DEFAULTS = {
    "document_year": "",
    "spp_version": "1.0",
    "policy_version": "1.0",
    "approved_by": "",
}


def load_profile(path):
    if not os.path.isfile(path):
        raise FileNotFoundError(
            f"Company profile not found: {path}. "
            "Copy company_profile.json, fill in your fields, and pass it with --profile."
        )
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    missing = [f for f in REQUIRED_FIELDS if not str(data.get(f, "")).strip()]
    if missing:
        raise ValueError(
            "company_profile.json is missing required fields: " + ", ".join(missing)
        )

    for key, default in OPTIONAL_DEFAULTS.items():
        data.setdefault(key, default)

    # Resolve the logo relative to the profile file so the tool can run
    # from any working directory.
    logo = data["logo_path"]
    if logo and not os.path.isabs(logo):
        data["logo_path"] = os.path.normpath(
            os.path.join(os.path.dirname(os.path.abspath(path)), logo)
        )
    if data["logo_path"] and not os.path.isfile(data["logo_path"]):
        raise FileNotFoundError(f"Logo file not found: {data['logo_path']}")

    if not data["document_year"]:
        import datetime
        data["document_year"] = str(datetime.date.today().year)

    return data


def fill(text, profile):
    """Substitute {placeholders} in template text with profile values."""
    return text.format(**profile)
