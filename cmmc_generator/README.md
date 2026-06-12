# CMMC Level 2 Documentation Studio

A professional CMMC Level 2 documentation assistant for first-time FSOs
and security managers. It generates a complete, branded documentation
set:

- One branded Standard Practices and Procedures (SPP), modeled on the
  AVASO Federal Solutions SPP 2026 template, with Appendix A (control
  mapping matrix) and Appendix B (procedures, forms, logs, checklists)
- 14 branded domain policies covering all 110 NIST SP 800-171 Rev. 2
  requirements
- Procedure packages for all 14 domains (52 procedures, forms, logs,
  and checklists)
- A CMMC Level 2 Control Mapping Matrix (Word, Excel, and CSV)
- A CMMC Level 2 Evidence Checklist (what an assessor will ask to see)
- A full binder export

Every generated document includes a cover page, document history,
approval block, purpose, scope, roles and responsibilities, policy or
procedure steps, evidence records, review frequency, references, and a
signature block, plus plain-English "What this document is for",
"Assessment evidence needed", and "Common assessor questions" sections.

## Compliance requirement

All generated documents must be aligned with applicable CMMC and DFARS
requirements. Every document (SPP, policies, procedures, evidence
checklist, and control mapping matrix) carries a compliance references
section covering:

- 32 CFR Part 170, CMMC Program Rule
- CMMC Level 2 requirements
- NIST SP 800-171 Rev. 2, all 110 security requirements
- DFARS 252.204-7012, Safeguarding Covered Defense Information and
  Cyber Incident Reporting
- DFARS 252.204-7019, NIST SP 800-171 DoD Assessment Requirements
- DFARS 252.204-7020, NIST SP 800-171 DoD Assessment Requirements
- DFARS 252.204-7021, Cybersecurity Maturity Model Certification
  Requirements
- DoD CUI Registry requirements
- Any applicable contract, DD Form 254, SOW, security classification
  guide, or CUI handling instruction

## Two ways to use the tool

### Option 1: The self-contained HTML app (no install)

Open **`index.html`** in any modern browser. It is fully
self-contained: no installation, no server, no network requests. Your
data stays in your browser.

User instructions:

1. **Welcome screen.** Click "Start guided setup" (or "Explore with
   sample profile" to see everything filled in first).
2. **Setup wizard, 5 steps.**
   - Step 1: Company profile (legal name, short name, address, CAGE,
     UEI)
   - Step 2: Security roles (SMO, FSO, AFSO, ITPSO, ISR)
   - Step 3: Facility and CUI details (clearance level, storage
     capability, DCSA field office, security contacts)
   - Step 4: Logo and branding (logo upload, version, effective date,
     approver)
   - Step 5: Review and generate
   Hover any "?" icon for a plain-English explanation of SMO, FSO,
   AFSO, ITPSO, ISR, CAGE, UEI, CUI, SSP, and POA&M. Required fields
   are marked with * and warn when empty. Answers save automatically;
   use "Save profile JSON" / "Load profile JSON" to back up or move
   profiles, "Use sample profile" to demo, and "Reset all" to start
   over.
3. **Watch the readiness score** in the navigation bar and on the
   dashboard. It reaches 100% when every field is complete.
4. **Dashboard.** Six cards: SPP Generator, Policy Generator,
   Procedure Package Generator, Control Mapping Matrix, Evidence
   Checklist, and Full Binder Export. Each card explains what the
   document is for. Click **Preview** to read any document before
   downloading, then **Download Word** (a .doc file that opens in
   Microsoft Word with your logo embedded) or **Print / Save as PDF**
   from the preview.
5. **Validation.** Before any export the app checks for missing
   company name, CAGE, UEI, SMO, FSO, ITPSO, logo, effective date, and
   approval name, and offers to take you back to the wizard.
6. **Export options.** Single document (Word), all policies (zip), a
   procedure package (zip), all procedures (zip), the full binder
   (zip of everything plus matrix CSV and your profile JSON), control
   matrix CSV, company_profile.json, and print/PDF.
7. **Finish in Word.** Review each document, tailor it to your real
   environment, and have your SMO sign the approval block. Use the
   Help panel (top right) any time.

### Option 2: The Python generator (native .docx and .xlsx)

```bash
pip install python-docx openpyxl
```

Edit `company_profile.json` (or export it from the HTML app), then:

```bash
python generate.py spp                    # the branded SPP
python generate.py policy --domain AC     # one policy
python generate.py policy --all           # all 14 policies
python generate.py procedures --domain IR # one procedure package
python generate.py procedures --all       # all 14 packages
python generate.py matrix                 # matrix as .docx and .xlsx
python generate.py evidence               # the evidence checklist
python generate.py binder                 # everything + zip
python generate.py domains                # list domain codes
```

Use `--profile path.json` to brand for another company and `--out dir`
to change the output directory. Output lands in `./output/01_SPP`,
`02_Policies`, `03_Procedures/<domain>`, `04_Control_Matrix`, and
`05_Evidence`.

Note: the Word table of contents in .docx output is a field; in Word,
right-click it and choose "Update Field".

## company_profile.json fields

| Field | Description |
| --- | --- |
| company_legal_name / company_short_name | Names used on covers, headers, file names |
| logo_path (Python) / logo_data (HTML app) | Company logo |
| address_line1 / address_line2 | Address block on the cover |
| cage_code / uei | CAGE code and Unique Entity Identifier |
| facility_clearance_level / storage_capability | FCL and safeguarding capability |
| smo_name, smo_title, fso_name, afso_name, itpso_name, isr_name | Security roles |
| dcsa_field_office | Cognizant DCSA field office |
| security_contact_email / security_contact_phone | Security contacts |
| effective_date, approved_by | Approval block on every document |
| document_year, spp_version, policy_version | Versioning metadata |

## Project layout

```
index.html          self-contained HTML app (generated by build_app.py)
app_template.html   app shell and logic (edit this, not index.html)
build_app.py        injects content data from cmmc_gen/ into index.html
generate.py         Python CLI
company_profile.json  branding profile (sample values included)
cmmc_gen/           content: practices, SPP sections, procedures,
                    guidance, compliance references, docx builders
templates/          the AVASO source documents used as style templates
assets/             sample logo
```

After editing any content in `cmmc_gen/`, run `python build_app.py` to
regenerate `index.html` so both generators stay in sync.

## Disclaimer

Generated documents are professional starting points aligned to CMMC
Level 2 and DFARS requirements. Review and tailor them to your actual
environment, contracts, and DD Form 254s before relying on them in an
assessment. This tool is not legal or certification advice.
