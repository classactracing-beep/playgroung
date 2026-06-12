"""CMMC Level 2 procedure package specifications for all 14 domains.

Structure modeled on the AVASO Access Management Procedures template:
a procedure document opens with supporting controls, then numbered
sections each with a Purpose line and procedure steps. Forms, logs, and
checklists are generated from field, column, and item specs.

Document kinds:
  procedure: {"sections": [(title, purpose, [steps])]}
  form:      {"fields": [...]}            signature-style fill-in form
  log:       {"columns": [...]}           landscape-style tracking table
  checklist: {"items": [...]}             checkbox list with sign-off
Text supports {placeholders} from company_profile.json.
"""

PACKAGES = {
    "AC": {
        "procedure": {
            "title": "Access Authorization Procedure",
            "controls": ["3.1.1", "3.1.2", "3.1.5", "3.9.2"],
            "sections": [
                ("User Access Authorization and Control",
                 "Restrict system access to only authorized users based on job "
                 "roles and the principle of least privilege.",
                 ["All users must complete an Account Request Form specifying the "
                  "system and role required.",
                  "Approval is required from the direct manager and the IT "
                  "security lead, depending on data sensitivity.",
                  "IT assigns each user a unique, traceable user ID. Shared "
                  "accounts are prohibited on systems containing CUI.",
                  "Default access is limited to the user's job function. "
                  "Additional access requires a new request and approval.",
                  "Login credentials must comply with the Identification and "
                  "Authentication Policy, including MFA for CUI systems."]),
                ("Privileged Access",
                 "Limit and control accounts that can change security settings "
                 "or access security functions.",
                 ["Privileged access requires written justification and "
                  "dual-level approval (manager plus ITPSO or IT security lead).",
                  "Privileged users receive separate administrative accounts and "
                  "use non-privileged accounts for routine work.",
                  "Privileged access is time-bound and reviewed every 6 months "
                  "using the Access Review Checklist."]),
                ("Periodic Access Review",
                 "Verify that access remains appropriate over time.",
                 ["The IT security lead performs an access review quarterly "
                  "using the Access Review Checklist.",
                  "Managers confirm each direct report still requires the access "
                  "held.",
                  "Discrepancies are corrected within 5 business days and "
                  "documented."]),
                ("Access Termination",
                 "Protect CUI and company systems during offboarding or role "
                 "changes.",
                 ["HR notifies IT of terminations at least 48 hours in advance "
                  "when possible, and immediately for involuntary separations.",
                  "IT disables accounts and revokes credentials by close of "
                  "business on the final workday using the User Access "
                  "Termination Checklist.",
                  "Physical access items (badges, keys, tokens) are collected "
                  "immediately.",
                  "Remote access, VPN, and certificates are disabled without "
                  "delay.",
                  "For transfers, old access rights are revoked before new "
                  "permissions are granted."]),
            ],
        },
        "documents": [
            {"kind": "form", "title": "Account Request Form",
             "fields": ["Requestor name", "Job title", "Department",
                        "Manager name", "System(s) requested",
                        "Role / access level requested",
                        "Business justification",
                        "CUI access required (Yes/No)",
                        "Privileged access required (Yes/No)",
                        "Requested start date",
                        "Manager approval (signature / date)",
                        "IT security approval (signature / date)",
                        "Account created by / date"]},
            {"kind": "checklist", "title": "Access Review Checklist",
             "items": ["Current user list exported from each in-scope system",
                       "Each account matched to an active employee or contractor",
                       "Orphaned and inactive accounts identified and disabled",
                       "Privileged accounts reviewed and justification confirmed",
                       "Access levels match documented job roles",
                       "Shared or generic accounts identified and removed",
                       "Service accounts reviewed and documented",
                       "Separation of duties conflicts checked",
                       "Findings documented and corrective actions assigned",
                       "Review results reported to the ITPSO"]},
            {"kind": "checklist", "title": "User Access Termination Checklist",
             "items": ["HR termination notification received and dated",
                       "Network / domain account disabled",
                       "Email account disabled or forwarded per policy",
                       "VPN and remote access revoked",
                       "MFA tokens and authenticators deactivated",
                       "Cloud application accounts disabled",
                       "Badge and physical keys collected",
                       "Company devices and media collected",
                       "Shared passwords known to the user rotated",
                       "CUI files owned by the user reassigned",
                       "Completion verified and signed by IT security lead"]},
        ],
    },
    "AT": {
        "procedure": {
            "title": "Security Training Procedure",
            "controls": ["3.2.1", "3.2.2", "3.2.3"],
            "sections": [
                ("New Hire Security Training",
                 "Ensure every user is aware of security risks and duties "
                 "before receiving system access.",
                 ["HR notifies the FSO of every new hire and contractor start.",
                  "The new user completes security awareness and CUI training "
                  "before credentials are issued, tracked on the New Hire "
                  "Training Checklist.",
                  "The user signs the Training Acknowledgment Form, which is "
                  "retained by the FSO."]),
                ("Annual Refresher Training",
                 "Keep all users current on threats, policies, and reporting "
                 "duties.",
                 ["The FSO schedules annual security awareness training for all "
                  "employees and contractors.",
                  "Training covers phishing and social engineering, acceptable "
                  "use, CUI handling, incident reporting, and insider threat "
                  "indicators.",
                  "Completion is recorded on the Annual Training Log.",
                  "Logical access is revoked for users who fail to complete "
                  "required training within 30 days of the due date."]),
                ("Role-Based Training",
                 "Train personnel for their specific security "
                 "responsibilities.",
                 ["IT administrators, the FSO, the ITPSO, and incident "
                  "responders receive role-based training annually.",
                  "Training needs are reassessed when staff change jobs.",
                  "Role-based completion is recorded on the Annual Training "
                  "Log."]),
                ("Insider Threat Awareness",
                 "Ensure users can recognize and report potential insider "
                 "threat indicators.",
                 ["Insider threat awareness content is included in initial and "
                  "annual training.",
                  "Users are instructed to report indicators to the ITPSO, "
                  "{itpso_name}, at {security_contact_email}."]),
            ],
        },
        "documents": [
            {"kind": "log", "title": "Annual Training Log",
             "columns": ["Employee name", "Role", "Training type",
                         "Training date", "Trainer / source",
                         "Acknowledgment on file (Y/N)", "Next due date"]},
            {"kind": "checklist", "title": "New Hire Training Checklist",
             "items": ["Security awareness training completed",
                       "CUI identification and handling training completed",
                       "Insider threat awareness training completed",
                       "Acceptable use policy reviewed and signed",
                       "Incident reporting contacts provided",
                       "Password and MFA requirements explained",
                       "Physical security and visitor rules explained",
                       "Training Acknowledgment Form signed and filed",
                       "FSO notified that training is complete",
                       "System access authorized only after all items checked"]},
            {"kind": "form", "title": "Training Acknowledgment Form",
             "fields": ["Employee name", "Job title", "Department",
                        "Training completed (list courses)",
                        "Date(s) completed",
                        "I acknowledge that I have completed the training listed "
                        "above, understand my security responsibilities, and "
                        "agree to comply with {company_short_name} security "
                        "policies (initials)",
                        "Employee signature / date",
                        "FSO signature / date"]},
        ],
    },
    "AU": {
        "procedure": {
            "title": "Audit Log Review Procedure",
            "controls": ["3.3.1", "3.3.2", "3.3.3", "3.3.5", "3.3.8"],
            "sections": [
                ("Audit Log Collection",
                 "Create and retain the records needed to investigate "
                 "unauthorized activity.",
                 ["All CUI systems generate audit logs capturing user ID, "
                  "timestamp, event type, and outcome.",
                  "System clocks synchronize to an authoritative NTP source.",
                  "Logs are retained for at least 90 days online and 1 year in "
                  "archive, or as required by contract.",
                  "Audit logs and tools are restricted to designated privileged "
                  "users."]),
                ("Scheduled Review",
                 "Detect unlawful, unauthorized, suspicious, or unusual "
                 "activity.",
                 ["The IT security lead reviews audit logs at least weekly, or "
                  "uses automated alerting with daily triage.",
                  "Reviews focus on failed logons, privilege use, account "
                  "changes, access to CUI repositories, and after-hours "
                  "activity.",
                  "Each review is recorded on the Audit Review Log.",
                  "The set of logged events is reviewed and updated at least "
                  "annually or after major system changes."]),
                ("Event Escalation",
                 "Route findings to incident response quickly.",
                 ["Suspicious events are assessed with the Security Event "
                  "Review Checklist.",
                  "Confirmed or suspected incidents are escalated under the "
                  "Incident Response Procedure immediately.",
                  "Audit logging process failures generate alerts to the IT "
                  "security lead, who restores logging within 24 hours."]),
            ],
        },
        "documents": [
            {"kind": "log", "title": "Audit Review Log",
             "columns": ["Review date", "Reviewer", "Systems / log sources "
                         "reviewed", "Period covered", "Anomalies found (Y/N)",
                         "Summary of findings", "Escalated to IR (Y/N)",
                         "Follow-up actions"]},
            {"kind": "checklist", "title": "Security Event Review Checklist",
             "items": ["Event source, time, and affected system identified",
                       "User account(s) involved identified",
                       "Event correlated against other log sources",
                       "Failed logon patterns checked for brute force activity",
                       "Privileged function use verified as authorized",
                       "Account creation and permission changes verified",
                       "Access to CUI repositories verified against need",
                       "Determination recorded (benign, suspicious, incident)",
                       "Incident Response Procedure invoked if suspicious",
                       "Review documented on the Audit Review Log"]},
        ],
    },
    "CM": {
        "procedure": {
            "title": "Configuration Management Procedure",
            "controls": ["3.4.1", "3.4.2", "3.4.3", "3.4.4", "3.4.6"],
            "sections": [
                ("Baseline Configurations",
                 "Establish and maintain known-good configurations and "
                 "inventories.",
                 ["IT maintains a hardware and software inventory of all "
                  "in-scope systems, reviewed quarterly.",
                  "Secure configuration baselines (hardening guides, CIS "
                  "Benchmarks, or DISA STIGs) are documented for each platform.",
                  "Baseline compliance is verified annually with the Baseline "
                  "Configuration Checklist.",
                  "Systems are configured for least functionality; nonessential "
                  "programs, ports, protocols, and services are disabled."]),
                ("Change Management",
                 "Track, review, approve, and log changes to systems.",
                 ["All changes to production CUI systems require a Change "
                  "Request Form.",
                  "The requester documents the change, rollback plan, and a "
                  "security impact analysis before approval.",
                  "Changes are approved by the IT security lead or change "
                  "advisory function and recorded on the Change Approval Log.",
                  "Emergency changes may proceed with verbal approval and must "
                  "be documented within 2 business days."]),
                ("Software Restriction",
                 "Prevent the use of unauthorized software.",
                 ["Only software on the approved software list may be "
                  "installed.",
                  "User-installed software is controlled and monitored; local "
                  "administrator rights are restricted.",
                  "Application allowlisting or blocklisting is applied per the "
                  "Configuration Management Policy."]),
            ],
        },
        "documents": [
            {"kind": "form", "title": "Change Request Form",
             "fields": ["Change request number", "Requested by / date",
                        "System(s) affected", "Description of change",
                        "Reason for change", "Security impact analysis summary",
                        "CUI affected (Yes/No)", "Rollback plan",
                        "Scheduled implementation date",
                        "Approved by (signature / date)",
                        "Implemented by / date", "Post-change verification"]},
            {"kind": "log", "title": "Change Approval Log",
             "columns": ["Change number", "Date requested", "System",
                         "Description", "Security impact reviewed (Y/N)",
                         "Approved by", "Date implemented", "Verified by"]},
            {"kind": "checklist", "title": "Baseline Configuration Checklist",
             "items": ["Hardware inventory current and complete",
                       "Software inventory current and complete",
                       "Documented baseline exists for each platform",
                       "Operating system hardening settings applied",
                       "Unnecessary services, ports, and protocols disabled",
                       "Default passwords changed on all devices",
                       "Local administrator rights restricted",
                       "Approved software list current",
                       "Deviation(s) from baseline documented and approved",
                       "Checklist results filed with configuration records"]},
        ],
    },
    "IA": {
        "procedure": {
            "title": "Identification and Authentication Procedure",
            "controls": ["3.5.1", "3.5.2", "3.5.3", "3.5.7", "3.5.10"],
            "sections": [
                ("User Identification",
                 "Ensure every user, process, and device is uniquely "
                 "identified.",
                 ["Each user receives a unique user ID tied to one individual.",
                  "Device identities are registered before network access is "
                  "granted.",
                  "Identifiers are not reused for at least 2 years and are "
                  "disabled after 90 days of inactivity."]),
                ("Multifactor Authentication",
                 "Require MFA where mandated by NIST SP 800-171.",
                 ["MFA is required for all network access to privileged and "
                  "non-privileged accounts and for local access to privileged "
                  "accounts.",
                  "New users are enrolled using the MFA Enrollment Checklist "
                  "before first CUI system access.",
                  "Lost or compromised authenticators are reported immediately "
                  "and revoked."]),
                ("Password Management",
                 "Enforce strong, protected passwords.",
                 ["Passwords meet the complexity and length settings in the "
                  "Identification and Authentication Policy.",
                  "Password reuse is prohibited for the configured number of "
                  "generations.",
                  "Temporary passwords are single-use and require an immediate "
                  "change at first logon.",
                  "Passwords are stored and transmitted only in "
                  "cryptographically protected form.",
                  "Password resets require identity verification and are "
                  "recorded on the Password Reset Log."]),
                ("Account Verification",
                 "Confirm account integrity on a recurring basis.",
                 ["Quarterly, the IT security lead completes the Account "
                  "Verification Checklist for all CUI systems.",
                  "Verification confirms unique IDs, MFA enrollment, inactivity "
                  "disablement, and authenticator hygiene."]),
            ],
        },
        "documents": [
            {"kind": "checklist", "title": "MFA Enrollment Checklist",
             "items": ["User identity verified in person or by approved remote "
                       "method",
                       "Account request approval on file",
                       "Authenticator type issued (app, token, smart card) "
                       "recorded",
                       "Authenticator registered to the user's unique ID",
                       "Backup / recovery method configured per policy",
                       "User briefed on protecting the authenticator",
                       "Test login with MFA completed successfully",
                       "Enrollment recorded by IT"]},
            {"kind": "log", "title": "Password Reset Log",
             "columns": ["Date / time", "User name", "System",
                         "Identity verified by (method)", "Reset performed by",
                         "Temporary password forced change (Y/N)", "Notes"]},
            {"kind": "checklist", "title": "Account Verification Checklist",
             "items": ["All accounts mapped to unique individuals",
                       "No shared or group credentials on CUI systems",
                       "MFA enrollment confirmed for all required accounts",
                       "Inactive identifiers (90+ days) disabled",
                       "Identifier reuse rules enforced",
                       "Password policy settings verified on each system",
                       "Stored credentials confirmed encrypted / hashed",
                       "Authentication feedback obscured on logon screens",
                       "Exceptions documented and approved",
                       "Results filed and reported to the ITPSO"]},
        ],
    },
    "IR": {
        "procedure": {
            "title": "Incident Response Procedure",
            "controls": ["3.6.1", "3.6.2", "3.6.3"],
            "sections": [
                ("Preparation",
                 "Maintain an operational incident-handling capability.",
                 ["The ITPSO, {itpso_name}, leads incident response with the "
                  "FSO, {fso_name}, and the IT security lead.",
                  "Contact lists, escalation paths, and response tools are "
                  "reviewed quarterly.",
                  "All users are trained to report suspected incidents "
                  "immediately to {security_contact_email} or "
                  "{security_contact_phone}."]),
                ("Detection and Analysis",
                 "Identify and assess potential incidents quickly.",
                 ["Reports from users, audit log reviews, and security tooling "
                  "are triaged using the Incident Handling Checklist.",
                  "The responder records facts on the Incident Report Form: "
                  "what happened, when, systems and data affected, and whether "
                  "CUI is involved.",
                  "Severity is assigned and the SMO is notified of any incident "
                  "involving CUI."]),
                ("Containment, Eradication, and Recovery",
                 "Limit damage and restore normal operations.",
                 ["Affected systems are isolated; credentials suspected of "
                  "compromise are reset.",
                  "Malware is removed, vulnerabilities closed, and systems "
                  "restored from known-good sources.",
                  "Evidence, system images, and packet captures are preserved "
                  "for at least 90 days."]),
                ("Reporting",
                 "Meet internal and external reporting obligations.",
                 ["Cyber incidents affecting covered defense information are "
                  "reported to DoD at https://dibnet.dod.mil within 72 hours, "
                  "per DFARS 252.204-7012.",
                  "The FSO reports to DCSA and the contracting officer as "
                  "required by 32 CFR Part 117.8 and contract clauses.",
                  "All incidents are tracked to closure on the Incident Report "
                  "Form."]),
                ("Lessons Learned and Testing",
                 "Improve the capability over time.",
                 ["A lessons learned session is held within 2 weeks of closing "
                  "significant incidents, captured on the Incident Lessons "
                  "Learned Form.",
                  "The incident response capability is tested at least annually "
                  "through a tabletop exercise; results are documented."]),
            ],
        },
        "documents": [
            {"kind": "form", "title": "Incident Report Form",
             "fields": ["Incident number", "Date / time detected",
                        "Reported by", "Date / time of occurrence (if known)",
                        "Systems and locations affected",
                        "CUI involved (Yes/No/Unknown)",
                        "Incident description", "Initial severity",
                        "Containment actions taken",
                        "External reporting required (DIBNET / DCSA / GCA)",
                        "External report date and tracking number",
                        "Resolution summary", "Date closed",
                        "ITPSO signature / date"]},
            {"kind": "checklist", "title": "Incident Handling Checklist",
             "items": ["Report received and Incident Report Form opened",
                       "Severity and CUI involvement assessed",
                       "ITPSO and FSO notified",
                       "Affected systems identified and isolated",
                       "Evidence preserved (images, logs, 90-day retention)",
                       "Credentials reset where compromise suspected",
                       "Malicious code removed / vulnerability closed",
                       "Systems restored and validated",
                       "DIBNET 72-hour report filed if required",
                       "DCSA / contracting officer notified if required",
                       "Users debriefed and incident closed",
                       "Lessons learned scheduled"]},
            {"kind": "form", "title": "Incident Lessons Learned Form",
             "fields": ["Incident number", "Date of review", "Participants",
                        "What happened (summary)", "What worked well",
                        "What did not work well",
                        "Root cause", "Detection gap identified",
                        "Policy or procedure changes recommended",
                        "Corrective actions and owners",
                        "Target completion dates",
                        "ITPSO approval (signature / date)"]},
        ],
    },
    "MA": {
        "procedure": {
            "title": "System Maintenance Procedure",
            "controls": ["3.7.1", "3.7.2", "3.7.3", "3.7.5", "3.7.6"],
            "sections": [
                ("Routine Maintenance",
                 "Keep organizational systems maintained and documented.",
                 ["Scheduled maintenance (patching, hardware service, "
                  "firmware updates) is planned and recorded on the "
                  "Maintenance Log.",
                  "Maintenance tools and media are inspected for malicious "
                  "code before use on CUI systems.",
                  "Only authorized personnel perform maintenance; personnel "
                  "without access authorization are supervised at all times."]),
                ("Off-Site and Vendor Maintenance",
                 "Protect CUI when equipment leaves the facility.",
                 ["Equipment is sanitized of CUI per NIST SP 800-88 before "
                  "off-site maintenance, and the sanitization is recorded.",
                  "Vendor maintenance personnel are escorted and their work "
                  "recorded on the Maintenance Log."]),
                ("Remote (Nonlocal) Maintenance",
                 "Control maintenance performed over a network.",
                 ["Remote maintenance requires prior approval using the Remote "
                  "Maintenance Approval Form.",
                  "Sessions require multifactor authentication and are "
                  "monitored.",
                  "Connections are terminated immediately when the maintenance "
                  "session is complete."]),
            ],
        },
        "documents": [
            {"kind": "log", "title": "Maintenance Log",
             "columns": ["Date", "System / equipment", "Maintenance performed",
                         "Performed by", "Escorted / supervised by",
                         "Media or tools checked (Y/N)",
                         "Sanitized before off-site (Y/N/NA)", "Notes"]},
            {"kind": "form", "title": "Remote Maintenance Approval Form",
             "fields": ["Request date", "Requested by",
                        "Vendor / technician name and company",
                        "System(s) to be accessed", "Purpose of maintenance",
                        "Access method and tools",
                        "MFA method to be used",
                        "Session monitoring by (name)",
                        "Scheduled date / time window",
                        "Approved by (signature / date)",
                        "Session start / end time",
                        "Connection terminated and verified by"]},
        ],
    },
    "MP": {
        "procedure": {
            "title": "Media Protection Procedure",
            "controls": ["3.8.1", "3.8.2", "3.8.3", "3.8.5", "3.8.7"],
            "sections": [
                ("Media Control and Storage",
                 "Physically control and securely store media containing CUI.",
                 ["All media containing CUI (paper and digital) is marked with "
                  "required CUI markings.",
                  "CUI media is stored in locked containers or controlled "
                  "rooms when not in use.",
                  "Access to CUI media is limited to authorized users.",
                  "All CUI media is tracked on the Media Inventory Log."]),
                ("Media Transport",
                 "Maintain accountability outside controlled areas.",
                 ["CUI on digital media in transport is encrypted with "
                  "FIPS-validated cryptography or protected by approved "
                  "physical safeguards.",
                  "Transport custody is recorded on the Media Inventory Log.",
                  "Removable media use is restricted to approved, owned, and "
                  "inventoried devices; unowned devices are prohibited."]),
                ("Sanitization and Destruction",
                 "Render CUI unrecoverable before disposal or reuse.",
                 ["Media is sanitized per NIST SP 800-88 (clear, purge, or "
                  "destroy) appropriate to the media type.",
                  "Each sanitization action is recorded on the Media "
                  "Sanitization Log.",
                  "Destroyed media is certified on the Media Destruction "
                  "Certificate, signed by the performer and a witness.",
                  "Backups containing CUI are protected at all storage "
                  "locations."]),
            ],
        },
        "documents": [
            {"kind": "log", "title": "Media Inventory Log",
             "columns": ["Media ID", "Type (HDD/SSD/USB/paper/tape)",
                         "Description / contents", "CUI (Y/N)", "Location",
                         "Custodian", "Date issued", "Date returned / disposed",
                         "Status"]},
            {"kind": "log", "title": "Media Sanitization Log",
             "columns": ["Date", "Media ID", "Media type",
                         "Sanitization method (clear/purge/destroy)",
                         "Tool / technique used", "Performed by",
                         "Verified by", "Final disposition"]},
            {"kind": "form", "title": "Media Destruction Certificate",
             "fields": ["Certificate number", "Date of destruction",
                        "Media ID(s) and description",
                        "Media type(s)", "Contained CUI (Yes/No)",
                        "Destruction method (shred/degauss/disintegrate/other)",
                        "Destruction location / vendor",
                        "Performed by (signature / date)",
                        "Witnessed by (signature / date)",
                        "FSO acknowledgment (signature / date)"]},
        ],
    },
    "PS": {
        "procedure": {
            "title": "Personnel Security Procedure",
            "controls": ["3.9.1", "3.9.2"],
            "sections": [
                ("Pre-Access Screening",
                 "Ensure only vetted personnel gain access to CUI.",
                 ["HR completes the Pre-Access Screening Checklist for every "
                  "employee and contractor before CUI system access is "
                  "authorized.",
                  "Screening includes identity verification, employment "
                  "history, criminal history check, and clearance validation "
                  "where applicable.",
                  "Screening records are stored securely by HR; access is "
                  "granted only after screening completion is confirmed to "
                  "IT."]),
                ("Terminations and Transfers",
                 "Protect systems containing CUI during and after personnel "
                 "actions.",
                 ["HR initiates the Offboarding Checklist for every departure "
                  "and the access review for every transfer.",
                  "IT disables logical access by close of business on the "
                  "final workday; physical access is revoked immediately.",
                  "The Access Removal Verification Form is completed and "
                  "signed within 3 business days of departure.",
                  "Departing personnel are reminded of continuing obligations "
                  "regarding CUI and proprietary information."]),
            ],
        },
        "documents": [
            {"kind": "checklist", "title": "Pre-Access Screening Checklist",
             "items": ["Government-issued photo identification verified",
                       "Employment eligibility (I-9 / E-Verify) completed",
                       "Employment history verified",
                       "Criminal background check completed and adjudicated",
                       "Security clearance verified in DISS (if applicable)",
                       "Non-disclosure agreement signed",
                       "Screening results filed securely by HR",
                       "IT notified that screening is complete",
                       "CUI access authorized by manager and FSO"]},
            {"kind": "checklist", "title": "Offboarding Checklist",
             "items": ["Resignation / termination documented by HR",
                       "IT notified with final work date",
                       "Exit interview and security debrief completed",
                       "Continuing CUI obligations acknowledged in writing",
                       "Company property returned (devices, media, badge, keys)",
                       "Logical access disabled (see User Access Termination "
                       "Checklist)",
                       "Physical access revoked",
                       "Payroll and benefits notified",
                       "Access Removal Verification Form completed"]},
            {"kind": "form", "title": "Access Removal Verification Form",
             "fields": ["Employee / contractor name", "Department",
                        "Last day of access", "Reason (termination/transfer)",
                        "Accounts disabled (list systems)",
                        "Date / time each account disabled",
                        "Physical access revoked (badge, keys) date",
                        "Equipment and media returned (Y/N, list)",
                        "CUI files reassigned to",
                        "Verified by IT (signature / date)",
                        "Verified by HR (signature / date)",
                        "FSO review (signature / date)"]},
        ],
    },
    "PE": {
        "procedure": {
            "title": "Physical Access Procedure",
            "controls": ["3.10.1", "3.10.2", "3.10.3", "3.10.4", "3.10.5"],
            "sections": [
                ("Facility Access Control",
                 "Limit physical access to systems and operating environments "
                 "to authorized individuals.",
                 ["Access to {company_short_name} work areas at "
                  "{address_line1} is controlled by badge, key, or access "
                  "code.",
                  "Physical access devices (badges, keys, codes) are issued by "
                  "the FSO and inventoried; codes are changed when personnel "
                  "depart or a device is lost.",
                  "Server rooms and network closets are locked and restricted "
                  "to authorized IT personnel.",
                  "Physical access logs are maintained and retained for at "
                  "least 1 year."]),
                ("Visitor Control",
                 "Escort visitors and monitor visitor activity.",
                 ["Visits are requested in advance using the Visitor Access "
                  "Request Form.",
                  "All visitors sign the Visitor Log on arrival and departure "
                  "and wear a visitor badge.",
                  "Visitors are escorted at all times in areas where CUI is "
                  "processed or stored.",
                  "Employees challenge unescorted unfamiliar persons and "
                  "report them to the FSO."]),
                ("Monitoring and Inspection",
                 "Protect and monitor the facility and support "
                 "infrastructure.",
                 ["Alarm, lock, and camera systems (where installed) are "
                  "checked as part of the quarterly Physical Security "
                  "Inspection Checklist.",
                  "CUI safeguarding at alternate work sites follows the "
                  "teleworking provisions of the Physical Protection Policy."]),
            ],
        },
        "documents": [
            {"kind": "log", "title": "Visitor Log",
             "columns": ["Date", "Visitor name", "Organization",
                         "Purpose of visit", "Person visited / escort",
                         "Time in", "Time out", "Badge number"]},
            {"kind": "form", "title": "Visitor Access Request Form",
             "fields": ["Visit date(s)", "Visitor name", "Organization",
                        "Citizenship", "Purpose of visit",
                        "Areas to be accessed", "CUI areas involved (Yes/No)",
                        "Sponsoring employee / escort",
                        "Sponsor signature / date",
                        "FSO approval (signature / date)"]},
            {"kind": "checklist", "title": "Physical Security Inspection Checklist",
             "items": ["Exterior doors and locks functioning",
                       "Badge reader / access control system functioning",
                       "Access device inventory reconciled (badges, keys)",
                       "Departed personnel removed from access systems",
                       "Visitor Log current and properly completed",
                       "Server room / network closet locked and access list "
                       "current",
                       "CUI storage containers locked and in good repair",
                       "Alarm and camera systems tested (where installed)",
                       "Clean desk spot-check for unattended CUI",
                       "Findings documented and corrective actions assigned"]},
        ],
    },
    "RA": {
        "procedure": {
            "title": "Risk Assessment Procedure",
            "controls": ["3.11.1", "3.11.2", "3.11.3"],
            "sections": [
                ("Periodic Risk Assessment",
                 "Assess risk to operations, assets, and individuals from the "
                 "operation of systems handling CUI.",
                 ["The ITPSO leads a documented risk assessment at least "
                  "annually and after significant changes.",
                  "Threats, vulnerabilities, likelihood, and impact are "
                  "evaluated for each in-scope system.",
                  "Identified risks are recorded in the Risk Register with an "
                  "owner and treatment decision."]),
                ("Vulnerability Scanning",
                 "Find and fix vulnerabilities before they are exploited.",
                 ["Authenticated vulnerability scans run at least monthly on "
                  "in-scope systems and after new vulnerabilities affecting "
                  "them are identified.",
                  "Scan results are triaged by severity: critical within 7 "
                  "days, high within 30 days, moderate within 90 days, or as "
                  "documented in the risk assessment.",
                  "Remediation is tracked on the Vulnerability Tracking Log "
                  "(System and Information Integrity package)."]),
                ("Risk Review",
                 "Keep the risk picture current.",
                 ["The Risk Register is reviewed quarterly using the Risk "
                  "Review Checklist.",
                  "Accepted risks are re-approved by the SMO annually.",
                  "Risk assessment results feed the POA&M and the System "
                  "Security Plan."]),
            ],
        },
        "documents": [
            {"kind": "log", "title": "Risk Register",
             "columns": ["Risk ID", "Date identified", "Description",
                         "Asset / system", "Likelihood", "Impact",
                         "Risk level", "Treatment "
                         "(mitigate/accept/transfer/avoid)", "Owner",
                         "Status", "Review date"]},
            {"kind": "checklist", "title": "Risk Review Checklist",
             "items": ["All open risks reviewed for current accuracy",
                       "New threats and vulnerabilities considered",
                       "Recent incidents reviewed for new risks",
                       "Vulnerability scan trends reviewed",
                       "System and environment changes assessed",
                       "Mitigation progress verified for each open risk",
                       "Accepted risks re-validated with the SMO",
                       "Risk Register updated with review date",
                       "POA&M updated where mitigation requires action",
                       "Summary reported to the SMO"]},
        ],
    },
    "CA": {
        "procedure": {
            "title": "Security Assessment Procedure",
            "controls": ["3.12.1", "3.12.2", "3.12.3", "3.12.4"],
            "sections": [
                ("Annual Self-Assessment",
                 "Determine whether security controls are effective.",
                 ["The ITPSO conducts an annual self-assessment of all 110 "
                  "NIST SP 800-171 requirements using NIST SP 800-171A "
                  "assessment objectives and the Self-Assessment Checklist.",
                  "Results are scored using the DoD Assessment Methodology and "
                  "reported to the Supplier Performance Risk System (SPRS) as "
                  "required.",
                  "The SMO reviews and approves the assessment results."]),
                ("Plan of Action and Milestones",
                 "Correct deficiencies and reduce vulnerabilities.",
                 ["Each deficiency is entered on the POA&M Tracker with a "
                  "responsible owner, milestones, and target date.",
                  "Significant deficiencies receive a Corrective Action Plan "
                  "Form documenting root cause and the fix.",
                  "The POA&M is reviewed monthly until all items close."]),
                ("Continuous Monitoring and SSP Maintenance",
                 "Keep controls effective and documentation current.",
                 ["Key controls (audit review, access review, scanning, "
                  "training) are monitored on their defined schedules.",
                  "The System Security Plan is reviewed and updated at least "
                  "annually and after significant changes."]),
            ],
        },
        "documents": [
            {"kind": "checklist", "title": "Self-Assessment Checklist",
             "items": ["Assessment scope and system boundary confirmed",
                       "Current SSP available and reviewed",
                       "All 14 domain policies reviewed for currency",
                       "Each of the 110 requirements assessed against "
                       "800-171A objectives",
                       "Evidence collected for each implemented requirement",
                       "Deficiencies documented with requirement IDs",
                       "DoD Assessment Methodology score calculated",
                       "SPRS score submitted / updated",
                       "POA&M Tracker updated with all open items",
                       "Results briefed to the SMO"]},
            {"kind": "log", "title": "POA&M Tracker",
             "columns": ["POA&M ID", "Requirement (NIST ID)",
                         "Weakness description", "Severity", "Owner",
                         "Milestones", "Resources required",
                         "Scheduled completion", "Status", "Date closed"]},
            {"kind": "form", "title": "Corrective Action Plan Form",
             "fields": ["CAP number", "Related POA&M ID / requirement",
                        "Deficiency description", "Root cause",
                        "Corrective action(s)", "Interim mitigation",
                        "Responsible owner", "Resources required",
                        "Milestone dates", "Completion criteria / evidence",
                        "Approved by (signature / date)",
                        "Verified closed by (signature / date)"]},
        ],
    },
    "SC": {
        "procedure": {
            "title": "System and Communications Protection Procedure",
            "controls": ["3.13.1", "3.13.6", "3.13.8", "3.13.11", "3.13.16"],
            "sections": [
                ("Boundary Protection",
                 "Monitor, control, and protect communications at system "
                 "boundaries.",
                 ["Firewalls deny all inbound traffic by default and permit "
                  "only documented exceptions.",
                  "Publicly accessible components are separated from internal "
                  "networks (DMZ or cloud segmentation).",
                  "Boundary devices and rules are verified quarterly with the "
                  "Boundary Protection Checklist.",
                  "Remote access terminates at managed access control points; "
                  "split tunneling is disabled on VPN clients."]),
                ("Encryption of CUI",
                 "Protect CUI in transit and at rest.",
                 ["CUI in transit is protected with FIPS-validated "
                  "cryptography (TLS 1.2 or higher with FIPS-validated "
                  "modules).",
                  "CUI at rest is encrypted on servers, workstations, and "
                  "mobile devices.",
                  "Cryptographic keys are generated, stored, rotated, and "
                  "destroyed under documented key management."]),
                ("Network Security Review",
                 "Verify ongoing protection of communications.",
                 ["The IT security lead performs a quarterly network security "
                  "review recorded on the Network Security Review Log.",
                  "The review covers firewall rules, VPN configuration, "
                  "wireless security, session termination settings, and "
                  "collaborative device controls."]),
            ],
        },
        "documents": [
            {"kind": "checklist", "title": "Boundary Protection Checklist",
             "items": ["Firewall default-deny inbound policy verified",
                       "Firewall rule set reviewed; unused rules removed",
                       "Public-facing systems segmented from internal network",
                       "VPN requires MFA and FIPS-validated encryption",
                       "Split tunneling disabled on remote clients",
                       "Wireless networks use WPA2/WPA3 enterprise "
                       "authentication and encryption",
                       "Session timeout / termination settings verified",
                       "Network diagram current and matches deployment",
                       "Findings documented and corrective actions assigned"]},
            {"kind": "log", "title": "Network Security Review Log",
             "columns": ["Review date", "Reviewer", "Scope (devices/segments)",
                         "Firewall rules reviewed (Y/N)",
                         "Encryption verified (Y/N)",
                         "Wireless reviewed (Y/N)", "Findings",
                         "Corrective actions", "Closure date"]},
        ],
    },
    "SI": {
        "procedure": {
            "title": "System and Information Integrity Procedure",
            "controls": ["3.14.1", "3.14.2", "3.14.3", "3.14.5", "3.14.6"],
            "sections": [
                ("Flaw Remediation",
                 "Identify, report, and correct system flaws in a timely "
                 "manner.",
                 ["Security advisories (CISA, vendor bulletins) are monitored "
                  "and actioned.",
                  "Patches are tested and deployed: critical within 7 days, "
                  "high within 30 days, others within 90 days.",
                  "Patch status is recorded on the Patch Management Log."]),
                ("Malicious Code Protection",
                 "Protect designated locations from malicious code.",
                 ["Anti-malware is deployed on all endpoints, servers, and "
                  "email gateways, with signatures updated automatically.",
                  "Real-time scanning is enabled for files from external "
                  "sources; periodic full scans run at least weekly.",
                  "Protection settings are verified quarterly using the "
                  "Malicious Code Protection Checklist."]),
                ("Monitoring",
                 "Detect attacks and unauthorized use.",
                 ["Inbound and outbound traffic and system logs are monitored "
                  "for indicators of attack.",
                  "Alerts are triaged under the Audit Log Review Procedure and "
                  "escalated to incident response when warranted.",
                  "Vulnerabilities from scans and advisories are tracked to "
                  "closure on the Vulnerability Tracking Log."]),
            ],
        },
        "documents": [
            {"kind": "log", "title": "Vulnerability Tracking Log",
             "columns": ["Vuln ID / CVE", "Date identified", "Source "
                         "(scan/advisory)", "Affected system(s)", "Severity",
                         "Remediation action", "Owner", "Due date",
                         "Status", "Date closed"]},
            {"kind": "log", "title": "Patch Management Log",
             "columns": ["Date", "Patch / update ID", "Vendor",
                         "Systems applied to", "Severity", "Tested (Y/N)",
                         "Applied by", "Verified by", "Notes"]},
            {"kind": "checklist", "title": "Malicious Code Protection Checklist",
             "items": ["Anti-malware installed on all in-scope endpoints",
                       "Anti-malware installed on servers and email gateway",
                       "Signature updates automatic and current (check dates)",
                       "Real-time / on-access scanning enabled",
                       "Weekly full scans scheduled and completing",
                       "External file and download scanning verified",
                       "Quarantine alerts routed to IT security",
                       "Exclusions reviewed and justified",
                       "Tamper protection enabled",
                       "Results documented and exceptions remediated"]},
        ],
    },
}

# Policy document names used across the matrix and appendices.
POLICY_NAMES = {
    "AC": "Access Control Policy",
    "AT": "Awareness and Training Policy",
    "AU": "Audit and Accountability Policy",
    "CM": "Configuration Management Policy",
    "IA": "Identification and Authentication Policy",
    "IR": "Incident Response Policy",
    "MA": "Maintenance Policy",
    "MP": "Media Protection Policy",
    "PS": "Personnel Security Policy",
    "PE": "Physical Protection Policy",
    "RA": "Risk Assessment Policy",
    "CA": "Security Assessment Policy",
    "SC": "System and Communications Protection Policy",
    "SI": "System and Information Integrity Policy",
}

# Responsible role and review frequency per domain for the matrix.
DOMAIN_GOVERNANCE = {
    "AC": ("IT Security Lead", "Quarterly"),
    "AT": ("FSO", "Annual"),
    "AU": ("IT Security Lead", "Weekly"),
    "CM": ("IT Security Lead", "Quarterly"),
    "IA": ("IT Security Lead", "Quarterly"),
    "IR": ("ITPSO", "Annual (tested)"),
    "MA": ("IT Security Lead", "Per event"),
    "MP": ("FSO", "Quarterly"),
    "PS": ("HR / FSO", "Per personnel action"),
    "PE": ("FSO", "Quarterly"),
    "RA": ("ITPSO", "Annual / Quarterly review"),
    "CA": ("ITPSO", "Annual / Monthly POA&M"),
    "SC": ("IT Security Lead", "Quarterly"),
    "SI": ("IT Security Lead", "Monthly"),
}


def evidence_for(domain):
    """Primary evidence artifacts (non-procedure docs) for a domain."""
    docs = PACKAGES[domain]["documents"]
    return "; ".join(d["title"] for d in docs)


# Plain-English guidance shown to end users and embedded in documents:
# what each package is for, the evidence an assessor will ask to see,
# and common assessor questions for the domain.
DOMAIN_GUIDANCE = {
    "AC": {
        "what": "Controls who can use your systems and what they can do. "
                "It proves that only approved people can reach CUI.",
        "evidence": [
            "Completed Account Request Forms for a sample of current users",
            "The most recent completed Access Review Checklist",
            "User Access Termination Checklists for recent departures",
            "A system-generated user list showing unique accounts"],
        "questions": [
            "How does a new employee get access to systems that hold CUI?",
            "Show me how access was removed for your last departed employee.",
            "Who has administrator rights, and why?"],
    },
    "AT": {
        "what": "Makes sure everyone is trained on security and CUI "
                "handling before they get access, and every year after.",
        "evidence": [
            "The Annual Training Log for the current year",
            "Signed Training Acknowledgment Forms",
            "New Hire Training Checklists for recent hires",
            "Training material covering insider threat awareness"],
        "questions": [
            "When was your last company-wide security training?",
            "How do you train new hires before they touch CUI?",
            "How would an employee recognize an insider threat?"],
    },
    "AU": {
        "what": "Keeps records of what happens on your systems so "
                "suspicious activity can be spotted and investigated.",
        "evidence": [
            "Completed Audit Review Log entries showing regular reviews",
            "Sample audit logs from CUI systems",
            "A completed Security Event Review Checklist",
            "Evidence of alerting when logging fails"],
        "questions": [
            "Who reviews your audit logs, and how often?",
            "How long do you keep logs?",
            "Show me how a failed logon attempt appears in your logs."],
    },
    "CM": {
        "what": "Keeps systems configured securely and makes sure changes "
                "are approved and documented before they happen.",
        "evidence": [
            "The hardware and software inventory",
            "Completed Change Request Forms and the Change Approval Log",
            "The most recent Baseline Configuration Checklist",
            "The approved software list"],
        "questions": [
            "How do you decide and document what software is allowed?",
            "Walk me through your last system change.",
            "How do you know your systems match the secure baseline?"],
    },
    "IA": {
        "what": "Makes sure every person and device proves who they are, "
                "with MFA and strong passwords, before getting in.",
        "evidence": [
            "MFA Enrollment Checklists and MFA configuration screenshots",
            "Password policy settings exported from each system",
            "The Password Reset Log",
            "The most recent Account Verification Checklist"],
        "questions": [
            "Show me MFA working on a CUI system.",
            "What are your password length and complexity settings?",
            "How do you verify identity before resetting a password?"],
    },
    "IR": {
        "what": "Defines how you detect, contain, and report security "
                "incidents, including the 72-hour DoD reporting rule.",
        "evidence": [
            "Completed Incident Report Forms (or a tested blank process)",
            "The Incident Handling Checklist",
            "Evidence of the annual incident response test or tabletop",
            "Incident Lessons Learned Forms"],
        "questions": [
            "Who do employees call when something looks wrong?",
            "When must you report a cyber incident to the DoD, and how?",
            "When did you last test your incident response plan?"],
    },
    "MA": {
        "what": "Controls who maintains your systems and how, so repairs "
                "and updates do not expose CUI.",
        "evidence": [
            "The Maintenance Log showing recent maintenance",
            "Approved Remote Maintenance Approval Forms",
            "Sanitization records for equipment sent off site"],
        "questions": [
            "How do you supervise an outside technician in your facility?",
            "What happens before a laptop is sent out for repair?",
            "How is remote vendor maintenance approved and monitored?"],
    },
    "MP": {
        "what": "Protects USB drives, disks, paper, and backups that hold "
                "CUI, from creation to certified destruction.",
        "evidence": [
            "The Media Inventory Log",
            "The Media Sanitization Log",
            "Signed Media Destruction Certificates",
            "Encryption settings for removable media"],
        "questions": [
            "How do you track USB drives that contain CUI?",
            "Show me how you destroyed your last retired hard drive.",
            "How is CUI protected when media leaves the building?"],
    },
    "PS": {
        "what": "Makes sure people are screened before they get access to "
                "CUI and that access ends cleanly when they leave.",
        "evidence": [
            "Completed Pre-Access Screening Checklists",
            "Offboarding Checklists for recent departures",
            "Signed Access Removal Verification Forms"],
        "questions": [
            "What screening happens before someone can access CUI?",
            "Walk me through your last employee departure.",
            "How fast is access removed after a termination?"],
    },
    "PE": {
        "what": "Controls who can physically enter areas where CUI is "
                "processed, and keeps records of visitors.",
        "evidence": [
            "The Visitor Log",
            "Approved Visitor Access Request Forms",
            "The quarterly Physical Security Inspection Checklist",
            "The badge / key inventory"],
        "questions": [
            "How do visitors get into your facility, and who escorts them?",
            "Show me your visitor log for last month.",
            "What happens to a badge when an employee leaves?"],
    },
    "RA": {
        "what": "Identifies what could go wrong, scans for "
                "vulnerabilities, and makes sure risks get fixed or "
                "formally accepted.",
        "evidence": [
            "The current Risk Register",
            "Recent vulnerability scan reports",
            "The quarterly Risk Review Checklist",
            "Evidence of remediation within defined timeframes"],
        "questions": [
            "When was your last risk assessment, and who did it?",
            "How often do you scan for vulnerabilities?",
            "Show me a vulnerability you found and how you fixed it."],
    },
    "CA": {
        "what": "Checks your own compliance: the annual self-assessment, "
                "the SPRS score, the SSP, and the POA&M that tracks gaps.",
        "evidence": [
            "The completed Self-Assessment Checklist",
            "The current System Security Plan",
            "The POA&M Tracker and Corrective Action Plan Forms",
            "The SPRS submission confirmation"],
        "questions": [
            "Where is your System Security Plan, and when was it updated?",
            "What is on your POA&M right now?",
            "How was your SPRS score calculated?"],
    },
    "SC": {
        "what": "Protects your network boundary and encrypts CUI in "
                "transit and at rest using FIPS-validated cryptography.",
        "evidence": [
            "The quarterly Boundary Protection Checklist",
            "The Network Security Review Log",
            "Firewall rule exports showing deny-by-default",
            "FIPS validation certificates for encryption in use"],
        "questions": [
            "Show me your firewall's default inbound policy.",
            "How is CUI encrypted in transit and at rest?",
            "Is your VPN configured to block split tunneling?"],
    },
    "SI": {
        "what": "Keeps systems patched, runs anti-malware everywhere, and "
                "watches for attacks.",
        "evidence": [
            "The Patch Management Log",
            "The Vulnerability Tracking Log",
            "The quarterly Malicious Code Protection Checklist",
            "Anti-malware console screenshots showing coverage"],
        "questions": [
            "How fast do you apply critical patches?",
            "Show me that anti-malware is on every endpoint and current.",
            "How would you detect an attack in progress?"],
    },
}
