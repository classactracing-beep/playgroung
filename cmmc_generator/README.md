# CMMC Level 2 Policy, Procedure, and SPP Generator

A self-contained generator for a complete, branded CMMC Level 2
documentation set:

- One branded Standard Practices and Procedures (SPP) Word document,
  modeled on the AVASO Federal Solutions SPP 2026 template (cover page,
  logo placement, company name and address block, CAGE code, disclosure
  statement, Forward section, table of contents, header and footer
  style, section numbering, security program layout, and references)
- 14 branded domain policy Word documents, modeled on the AVASO
  Awareness and Training Policy template
- Procedure packages for all 14 CMMC Level 2 domains (52 documents:
  procedures, forms, logs, and checklists)
- A CMMC Level 2 Control Mapping Matrix covering all 110 NIST SP
  800-171 Rev. 2 requirements, exported as a Word table and an Excel
  spreadsheet
- SPP Appendix A: CMMC Level 2 Control Mapping Matrix
- SPP Appendix B: CMMC Level 2 Procedures, Forms, Logs, and Checklists
- An optional full binder export (zip)

Every document is branded from a single `company_profile.json` file, so
the whole set can be regenerated for any company.

## Requirements

```bash
pip install python-docx openpyxl
```

Python 3.9 or later. No network access is required; everything runs
locally.

## Quick start

1. Open `index.html` in a browser (it is fully self-contained and sends
   no data anywhere). Fill in your company fields and click "Download
   company_profile.json". Save the file into this folder, and copy your
   logo into `assets/`.

   Or edit `company_profile.json` directly in a text editor.

2. Generate documents into `./output`:

```bash
# The branded SPP (with Appendix A and Appendix B)
python generate.py spp

# One policy (domain codes: AC AT AU CM IA IR MA MP PS PE RA CA SC SI)
python generate.py policy --domain AC

# All 14 policies
python generate.py policy --all

# One procedure package (procedure + forms, logs, checklists)
python generate.py procedures --domain IR

# All 14 procedure packages
python generate.py procedures --all

# The control mapping matrix (Word table and Excel spreadsheet)
python generate.py matrix

# The full branded binder: SPP, 14 policies, 14 procedure packages,
# matrix in Word and Excel, plus a single zip archive
python generate.py binder

# List the 14 domains
python generate.py domains
```

Use `--profile path/to/profile.json` to brand for a different company
and `--out path` to change the output directory.

## company_profile.json fields

| Field | Description |
| --- | --- |
| company_legal_name | Full legal name used on covers and policy text |
| company_short_name | Abbreviation used in headers, footers, file names |
| logo_path | Path to the logo image (relative to the profile file) |
| address_line1 / address_line2 | Company address block on the cover |
| cage_code | CAGE code shown on the cover page |
| uei | Unique Entity Identifier |
| facility_clearance_level | FCL level (None, Secret, Top Secret) |
| storage_capability | Classified storage capability statement |
| smo_name / smo_title | Senior Management Official |
| fso_name | Facility Security Officer |
| afso_name | Assistant FSO |
| itpso_name | Insider Threat Program Senior Official |
| isr_name | Insider Threat Program Security Representative |
| dcsa_field_office | Cognizant DCSA field office |
| security_contact_email / security_contact_phone | Security contacts |
| document_year, spp_version, policy_version, approved_by | Optional metadata |

## Output layout

```
output/
  01_SPP/                       <ShortName>_SPP_<year>.docx
  02_Policies/                  14 policy .docx files
  03_Procedures/<domain>/       procedure + forms, logs, checklists
  04_Control_Matrix/            matrix .docx and .xlsx
  <ShortName>_CMMC_L2_Binder.zip  (binder command only)
```

## Procedure packages

| Domain | Procedure | Forms, Logs, Checklists |
| --- | --- | --- |
| Access Control | Access Authorization Procedure | Account Request Form; Access Review Checklist; User Access Termination Checklist |
| Awareness and Training | Security Training Procedure | Annual Training Log; New Hire Training Checklist; Training Acknowledgment Form |
| Audit and Accountability | Audit Log Review Procedure | Audit Review Log; Security Event Review Checklist |
| Configuration Management | Configuration Management Procedure | Change Request Form; Change Approval Log; Baseline Configuration Checklist |
| Identification and Authentication | Identification and Authentication Procedure | MFA Enrollment Checklist; Password Reset Log; Account Verification Checklist |
| Incident Response | Incident Response Procedure | Incident Report Form; Incident Handling Checklist; Incident Lessons Learned Form |
| Maintenance | System Maintenance Procedure | Maintenance Log; Remote Maintenance Approval Form |
| Media Protection | Media Protection Procedure | Media Inventory Log; Media Sanitization Log; Media Destruction Certificate |
| Personnel Security | Personnel Security Procedure | Pre-Access Screening Checklist; Offboarding Checklist; Access Removal Verification Form |
| Physical Protection | Physical Access Procedure | Visitor Log; Visitor Access Request Form; Physical Security Inspection Checklist |
| Risk Assessment | Risk Assessment Procedure | Risk Register; Risk Review Checklist |
| Security Assessment | Security Assessment Procedure | Self-Assessment Checklist; POA&M Tracker; Corrective Action Plan Form |
| System and Communications Protection | System and Communications Protection Procedure | Boundary Protection Checklist; Network Security Review Log |
| System and Information Integrity | System and Information Integrity Procedure | Vulnerability Tracking Log; Patch Management Log; Malicious Code Protection Checklist |

## Notes

- The Word table of contents is inserted as a field. After opening a
  generated document, right-click the TOC and choose "Update Field" (or
  press Ctrl+A then F9) to populate it.
- The control mapping matrix maps every requirement to its CMMC
  domain, CMMC practice ID, NIST SP 800-171 Rev. 2 requirement ID,
  requirement title, policy document, procedure document, evidence
  artifacts, responsible role, and review frequency.
- The two AVASO source documents used as style templates are kept in
  `templates/` for reference.
- `index.html` is a static page with a restrictive Content Security
  Policy. It performs no network requests; the profile JSON is built
  and downloaded entirely in the browser.
- The generated documents are starting points. Review and tailor them
  to your actual environment before relying on them for a CMMC
  assessment.
