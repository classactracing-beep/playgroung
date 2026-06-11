"""SPP section content, modeled on the AVASO Federal Solutions SPP 2026.

Each section is (heading, blocks). Blocks are:
  ("p", text)        body paragraph
  ("ul", [items])    bulleted list
  ("h2", text)       subsection heading
Text supports {placeholders} from company_profile.json.
"""

FORWARD = [
    ("p", "{company_legal_name} has entered into agreements with the United States "
          "Government to protect classified information and Controlled Unclassified "
          "Information (CUI) entrusted to the company. Some of our programs and "
          "activities are vital parts of the defense and security systems of the "
          "United States."),
    ("p", "This Standard Practices and Procedures (SPP) adheres to the security "
          "requirements outlined in the National Industrial Security Program "
          "Operating Manual (NISPOM), codified at 32 CFR Part 117, the requirements "
          "of 32 CFR Part 2002 for CUI, and the Cybersecurity Maturity Model "
          "Certification (CMMC) Level 2 requirements derived from NIST SP 800-171 "
          "Rev. 2."),
    ("p", "Our company fully supports the National Industrial Security Program. All "
          "of us have an obligation to ensure that the security practices described "
          "in this SPP are carried out. Every employee, consultant, and "
          "subcontractor is expected to read this SPP and to understand his or her "
          "individual security responsibilities."),
    ("sig", [("{smo_name}", "{smo_title}, Senior Management Official"),
             ("{fso_name}", "Facility Security Officer")]),
]

SECTIONS = [
    ("Introduction", [
        ("p", "This Standard Practices and Procedures (SPP) describes "
              "{company_legal_name} ({company_short_name}) policies regarding the "
              "protection of classified information and Controlled Unclassified "
              "Information (CUI). It implements the National Industrial Security "
              "Program Operating Manual (NISPOM) rule at 32 CFR Part 117 and the "
              "CMMC Level 2 security requirements of NIST SP 800-171 Rev. 2."),
        ("p", "{company_short_name} employees must adhere to the security "
              "requirements outlined in this SPP as well as any additional policies "
              "and procedures issued by the Facility Security Officer (FSO). "
              "Violations of this SPP may result in administrative action up to and "
              "including termination of employment, and may be reportable to the "
              "U.S. Government."),
        ("p", "All employees are expected to read this SPP carefully to understand "
              "{company_short_name} security policies and their individual "
              "responsibilities. Questions should be directed to the FSO at "
              "{security_contact_email} or {security_contact_phone}."),
    ]),
    ("Facility Information", [
        ("p", "Company legal name: {company_legal_name}"),
        ("p", "Company short name: {company_short_name}"),
        ("p", "Address: {address_line1}, {address_line2}"),
        ("p", "CAGE Code: {cage_code}"),
        ("p", "Unique Entity Identifier (UEI): {uei}"),
        ("p", "Facility clearance level: {facility_clearance_level}"),
        ("p", "Storage capability: {storage_capability}"),
        ("p", "Cognizant DCSA field office: {dcsa_field_office}"),
        ("p", "Security contact: {security_contact_email} | {security_contact_phone}"),
    ]),
    ("Facility Clearance", [
        ("p", "A facility clearance (FCL) is an administrative determination that a "
              "facility is eligible for access to classified information at the same "
              "or lower classification level as the FCL granted. "
              "{company_short_name} holds a facility clearance at the "
              "{facility_clearance_level} level, sponsored through the Defense "
              "Counterintelligence and Security Agency (DCSA), {dcsa_field_office} "
              "field office."),
        ("p", "The FCL includes the execution of a Department of Defense Security "
              "Agreement (DD Form 441) and a Certificate Pertaining to Foreign "
              "Interests (SF 328). Changes affecting the FCL, including changes in "
              "ownership, key management personnel, or foreign ownership, control, "
              "or influence (FOCI), will be reported to DCSA in accordance with "
              "32 CFR Part 117.8."),
    ]),
    ("FSO Responsibilities", [
        ("p", "{fso_name} is the appointed Facility Security Officer (FSO) for "
              "{company_short_name}. {afso_name} serves as the Assistant Facility "
              "Security Officer (AFSO) and performs FSO duties in the FSO's "
              "absence. The FSO is a U.S. citizen, cleared to the level of the FCL, "
              "and has completed FSO training required by 32 CFR Part 117.12."),
        ("p", "Pursuant to 32 CFR Part 117.7(b)(3), the FSO will supervise and "
              "direct security measures necessary for implementing the NISPOM rule "
              "and related Federal requirements. FSO duties include:"),
        ("ul", [
            "Administering the personnel security clearance program and submitting "
            "investigation requests through the Defense Information System for "
            "Security (DISS) and NBIS",
            "Providing initial, refresher, insider threat, and debriefing security "
            "education to all cleared employees",
            "Conducting the annual self-inspection and supporting DCSA security "
            "reviews",
            "Submitting required reports, including adverse information, suspicious "
            "contacts, and changed conditions",
            "Maintaining this SPP, security records, and visit authorizations",
            "Overseeing the CUI program, including marking, handling, and incident "
            "response for CUI",
        ]),
    ]),
    ("SMO Responsibilities", [
        ("p", "The Senior Management Official (SMO) is the contractor official "
              "responsible for entity policy and strategy. {smo_name}, "
              "{smo_title}, is the SMO for {company_short_name} and can be reached "
              "through {security_contact_email}."),
        ("p", "Pursuant to 32 CFR Part 117.7(b)(2), the SMO will:"),
        ("ul", [
            "Ensure the company maintains a system of security controls in "
            "accordance with the NISPOM rule",
            "Appoint a contractor employee or employees, in writing, as the FSO and "
            "the Insider Threat Program Senior Official (ITPSO)",
            "Remain fully informed of the facility's classified operations",
            "Make decisions based on classified threat reporting and thorough "
            "knowledge, understanding, and appreciation of the threat information "
            "and the potential impacts caused by a loss of classified information",
            "Retain accountability for the management and operations of the "
            "facility without delegating that accountability",
        ]),
    ]),
    ("ITPSO Responsibilities", [
        ("p", "{itpso_name} is the appointed Insider Threat Program Senior Official "
              "(ITPSO) for {company_short_name}. The ITPSO is cleared to the level "
              "of the FCL and has completed required insider threat program "
              "training."),
        ("p", "{company_short_name} has established and will maintain an insider "
              "threat program in accordance with 32 CFR Part 117.7(c) to gather, "
              "integrate, and report relevant and available information indicative "
              "of a potential or actual insider threat. The Insider Threat Program "
              "Security Representative for this facility is {isr_name}."),
    ]),
    ("Storage Capability", [
        ("p", "The facility clearance level is separate from the storage capability "
              "level. {company_short_name} storage capability: "
              "{storage_capability}."),
        ("p", "Company personnel may access classified information only at "
              "locations approved for safeguarding at the appropriate level. Any "
              "change to storage capability requires prior DCSA approval and an "
              "update to this SPP."),
    ]),
    ("Cooperation with Federal Agencies", [
        ("p", "{company_short_name} will cooperate with Federal agencies and their "
              "officially credentialed U.S. Government or contractor "
              "representatives during official inspections, investigations "
              "concerning the protection of classified information and CUI, and "
              "personnel security investigations. Cooperation includes:"),
        ("ul", [
            "Providing suitable arrangements within the facility for conducting "
            "private interviews with employees during normal working hours",
            "Providing, when requested, relevant employment or personnel files, "
            "security records, supervisory files, and records pertinent to an "
            "investigation",
            "Providing access to employment and security records located at an "
            "offsite location",
            "Rendering other necessary assistance",
        ]),
    ]),
    ("Personnel Security Clearances", [
        ("p", "{company_short_name} employees will be processed for a personnel "
              "security clearance (PCL) only when a determination has been made "
              "that access is essential in the performance of tasks or services "
              "related to the fulfillment of a classified contract."),
        ("p", "Each applicant must provide valid proof of U.S. citizenship. The FSO "
              "will notify applicants in writing of the review and privacy "
              "provisions that apply to the SF-86, and the information provided "
              "will be used solely to determine the adequacy and completeness of "
              "the submission. The U.S. Government, not {company_short_name}, "
              "makes the clearance eligibility determination."),
        ("p", "Cleared employees are subject to Continuous Vetting, including FBI "
              "Rap Back enrollment, and must report relevant information as "
              "described in the reporting sections of this SPP. For security "
              "administration purposes, consultants are treated as employees and "
              "must comply with this SPP."),
    ]),
    ("Security Education", [
        ("p", "In accordance with 32 CFR Part 117.12, the FSO administers a "
              "security education program that includes:"),
        ("ul", [
            "Initial security briefings before access to classified information is "
            "granted, including a threat awareness briefing, a counterintelligence "
            "awareness briefing, an overview of the security classification "
            "system, employee reporting obligations, cybersecurity awareness, and "
            "security procedures specific to the employee's job",
            "Execution of the SF-312 Classified Information Nondisclosure "
            "Agreement prior to access",
            "Insider threat awareness training before access and annually "
            "thereafter",
            "Annual refresher briefings for all cleared employees",
            "Derivative classification training where applicable",
            "Debriefings upon termination of access or employment",
        ]),
        ("p", "Training completion is documented and retained by the FSO. The "
              "companion CMMC Awareness and Training Policy and Security Training "
              "Procedure govern training for users of systems that process CUI."),
    ]),
    ("Security Reviews and Self-Inspections", [
        ("p", "DCSA will conduct recurring security reviews of "
              "{company_short_name} in accordance with 32 CFR Part 117.7(h)(1). "
              "The FSO will support these reviews and the SMO will be advised of "
              "all results."),
        ("p", "The FSO will complete a formal self-inspection at intervals "
              "consistent with risk management principles, at least annually, in "
              "accordance with 32 CFR Part 117.7(h)(2). The self-inspection "
              "includes the review of classified activity, security education, "
              "reporting, and the CUI program. The SMO will certify completion of "
              "the self-inspection to DCSA via the annual senior officer "
              "certification."),
    ]),
    ("Individual and Company Reporting Responsibilities", [
        ("p", "All employees, regardless of clearance status, share responsibility "
              "for reporting information that may affect the protection of "
              "classified information or CUI. Reports are made to the FSO at "
              "{security_contact_email} or {security_contact_phone}. The FSO "
              "submits required reports to DCSA, the FBI, or the Government "
              "Contracting Activity as applicable under 32 CFR Part 117.8."),
        ("ul", [
            "Espionage, sabotage, terrorism, or subversive activities (reported to "
            "the FBI with a copy to DCSA)",
            "Suspicious contacts and attempted elicitation",
            "Adverse information concerning cleared employees",
            "Loss, compromise, or suspected compromise of classified information",
            "Security violations and administrative security incidents",
            "Changes in cleared personnel status and changed conditions affecting "
            "the FCL",
        ]),
    ]),
    ("SEAD 3 Reporting", [
        ("p", "Security Executive Agent Directive (SEAD) 3 establishes reporting "
              "requirements for all covered individuals who have access to "
              "classified information. {company_short_name} cleared employees must "
              "report the following to the FSO before participation or as soon as "
              "possible afterward:"),
        ("ul", [
            "Unofficial foreign travel (reported and approved in advance)",
            "Continuing association with known foreign nationals and foreign "
            "contacts involving bonds of affection, personal obligation, or "
            "intimate contact",
            "Foreign citizenship or foreign monetary interests, including foreign "
            "bank accounts and foreign property",
            "Adoption of non-U.S. citizen children, cohabitants, and marriage",
            "Arrests, bankruptcy or significant financial anomalies, alcohol and "
            "drug related treatment",
            "Media contacts where the media seeks access to classified or "
            "otherwise protected information",
        ]),
    ]),
    ("Foreign Travel", [
        ("p", "Cleared employees must report unofficial (personal) foreign travel "
              "to the FSO in advance of the travel, in accordance with SEAD 3. The "
              "FSO will record the itinerary, provide a defensive security "
              "pre-travel briefing covering threat awareness and emergency "
              "contacts, and conduct a post-travel debriefing upon return."),
        ("p", "Travel that is not reported in advance because of an emergency must "
              "be reported to the FSO no later than five business days after "
              "return. Suspicious incidents occurring during foreign travel must "
              "be reported immediately upon return."),
    ]),
    ("Foreign Contacts", [
        ("p", "Cleared employees must report to the FSO any continuing association "
              "with a foreign national that involves bonds of affection, personal "
              "obligation, or intimate contact, and any contact with a foreign "
              "national who requests classified, controlled, or proprietary "
              "information, or who makes the employee feel uncomfortable through "
              "persistent questioning about job duties."),
        ("p", "The FSO will document foreign contact reports and forward "
              "reportable contacts to DCSA through the appropriate channel."),
    ]),
    ("Adverse Information", [
        ("p", "In accordance with 32 CFR Part 117.8(c)(1), employees must report "
              "adverse information concerning any cleared employee, including "
              "themselves, that may reflect on trustworthiness or reliability. "
              "Examples include criminal conduct, excessive indebtedness, illegal "
              "drug use, excessive alcohol use affecting conduct, and unexplained "
              "affluence."),
        ("p", "Reports are made to the FSO, who will submit the report to DCSA via "
              "DISS. Reporting adverse information is a protective measure, not a "
              "punitive one, and reports made in good faith will not be the basis "
              "for retaliation."),
    ]),
    ("Cyber Incident Reporting", [
        ("p", "Pursuant to 32 CFR Part 117.8(f) and DFARS 252.204-7012, "
              "{company_short_name} will report cyber incidents that affect "
              "covered defense information, covered contractor information "
              "systems, or the ability to perform operationally critical "
              "contract requirements."),
        ("ul", [
            "Employees report suspected cyber incidents immediately to the ITPSO "
            "and FSO at {security_contact_email}",
            "Rapidly report qualifying incidents to the DoD at https://dibnet.dod.mil "
            "within 72 hours of discovery",
            "Preserve and protect images of affected systems and relevant "
            "monitoring data for at least 90 days",
            "Submit malicious software to the DoD Cyber Crime Center (DC3) when "
            "requested",
            "Coordinate with the Government Contracting Activity and DCSA as "
            "required",
        ]),
        ("p", "The Incident Response Policy and Incident Response Procedure in the "
              "CMMC documentation set provide the detailed internal handling "
              "steps."),
    ]),
    ("Controlled Unclassified Information (CUI)", [
        ("p", "CUI is information the Government creates or possesses, or that an "
              "entity creates or possesses for or on behalf of the Government, "
              "that a law, regulation, or Government-wide policy requires or "
              "permits an agency to handle using safeguarding or dissemination "
              "controls. {company_short_name} protects CUI in accordance with "
              "32 CFR Part 2002, applicable contract clauses, and NIST SP 800-171 "
              "Rev. 2 as assessed under CMMC Level 2."),
        ("p", "The FSO serves as the CUI program manager. All employees who "
              "handle CUI are responsible for proper marking, safeguarding, "
              "dissemination, and destruction as described in the following "
              "sections."),
    ]),
    ("CUI Training and Awareness", [
        ("p", "All employees with access to CUI complete initial CUI training "
              "before being granted access and annual refresher training "
              "thereafter. Training covers identifying CUI, marking, handling, "
              "storage, dissemination, decontrol, destruction, and incident "
              "reporting."),
        ("p", "Training completion records are retained by the FSO for the "
              "duration of employment plus two years. The Annual Training Log and "
              "Training Acknowledgment Form in the Awareness and Training "
              "procedure package are the records of completion."),
    ]),
    ("CUI Handling", [
        ("p", "Information owners and end users will:"),
        ("ul", [
            "Mark CUI with the appropriate banner markings and designation "
            "indicators before dissemination",
            "Store CUI in controlled environments that prevent access by "
            "unauthorized individuals, and apply at least one physical or "
            "electronic barrier when CUI is unattended",
            "Process CUI only on systems authorized in the System Security Plan",
            "Encrypt CUI in transit and at rest using FIPS-validated cryptography",
            "Share CUI only with individuals who have a lawful Government purpose "
            "and any required dissemination controls",
            "Destroy CUI so it is unreadable, indecipherable, and irrecoverable, "
            "using approved shredders or media sanitization per NIST SP 800-88",
        ]),
    ]),
    ("CUI Unauthorized Disclosure", [
        ("p", "An unauthorized disclosure occurs when CUI is provided to, or "
              "accessed by, a person who does not have a lawful Government purpose "
              "to receive it. CUI misuse occurs when CUI is handled in a manner "
              "inconsistent with applicable policy, including improper marking, "
              "storage, or destruction."),
        ("p", "Employees must report suspected unauthorized disclosure or misuse "
              "of CUI to the FSO immediately at {security_contact_email}. The FSO "
              "will assess the incident, notify the contracting officer and other "
              "Government stakeholders as required by contract, document the "
              "incident on an Incident Report Form, and direct corrective "
              "actions."),
    ]),
    ("CUI Self-Inspection", [
        ("p", "The FSO will include the CUI program in the annual self-inspection. "
              "The CUI self-inspection reviews marking practices, storage and "
              "handling, training records, incident reports, system authorization "
              "status, and destruction practices. Results are documented, briefed "
              "to the SMO, and tracked to closure on the POA&M Tracker from the "
              "Security Assessment procedure package."),
    ]),
    ("Information System Security", [
        ("p", "{company_short_name} systems that process, store, or transmit CUI "
              "are protected in accordance with the 110 security requirements of "
              "NIST SP 800-171 Rev. 2, implemented through the 14 CMMC Level 2 "
              "domain policies and procedure packages listed in Appendix B and "
              "mapped in Appendix A."),
        ("ul", [
            "A System Security Plan (SSP) describes the system boundary, "
            "environment of operation, and how each requirement is implemented",
            "Plans of Action and Milestones (POA&M) track and correct "
            "deficiencies",
            "The ITPSO, {itpso_name}, oversees information system security and "
            "incident response in coordination with the FSO",
            "Classified information will never be processed on "
            "{company_short_name} information systems",
        ]),
    ]),
    ("Visits and Meetings", [
        ("p", "Incoming visits: visit authorizations for classified visits are "
              "verified through DISS or by visit authorization letter before "
              "access is granted. Visitors are escorted, their activity is "
              "monitored, and they are recorded on the Visitor Log. Need-to-know "
              "is confirmed by the responsible program manager before any "
              "disclosure."),
        ("p", "Outgoing visits: the FSO submits visit requests through DISS or by "
              "visit authorization letter to the host facility. Employees must "
              "coordinate classified visits with the FSO in advance and comply "
              "with the security requirements of the host facility."),
    ]),
    ("Public Release and Disclosure", [
        ("p", "In accordance with 32 CFR Part 117.15, information related to "
              "classified contracts will not be released to the public without "
              "the prior review and written authorization of the Government "
              "Contracting Activity. This includes press releases, marketing "
              "material, conference papers, and website and social media "
              "content."),
        ("p", "CUI will not be posted on publicly accessible systems. Employees "
              "must route all proposed public releases related to Government "
              "contracts through the FSO for review. Improperly released "
              "classified information must be reported to the FSO immediately and "
              "will be handled in accordance with 32 CFR Part 117.13(g)."),
    ]),
    ("Emergency Procedures", [
        ("p", "In an emergency (fire, natural disaster, civil disturbance, or "
              "medical emergency), the protection of life always takes precedence "
              "over the protection of information. Employees should follow "
              "facility evacuation procedures and contact emergency services at "
              "911."),
        ("ul", [
            "Secure classified material and CUI only if it is safe to do so",
            "Report any potential compromise of classified information or CUI "
            "resulting from an emergency to the FSO as soon as practical",
            "FSO: {fso_name}, {security_contact_phone}, {security_contact_email}",
            "AFSO: {afso_name}",
            "ITPSO: {itpso_name}",
            "DCSA field office: {dcsa_field_office}",
        ]),
    ]),
    ("Definitions", [
        ("p", "Adverse Information: Any information that adversely reflects on the "
              "integrity or character of a cleared employee, that suggests that "
              "his or her ability to safeguard classified information may be "
              "impaired, or that his or her access to classified information "
              "clearly may not be in the interest of national security."),
        ("p", "Controlled Unclassified Information (CUI): Information that "
              "requires safeguarding or dissemination controls pursuant to and "
              "consistent with applicable law, regulations, and Government-wide "
              "policies but is not classified under Executive Order 13526."),
        ("p", "Cyber Incident: Actions taken through the use of computer networks "
              "that result in a compromise or an actual or potentially adverse "
              "effect on an information system and/or the information residing "
              "therein."),
        ("p", "Facility Clearance (FCL): An administrative determination that a "
              "facility is eligible for access to classified information."),
        ("p", "Insider Threat: The likelihood, risk, or potential that an insider "
              "will use his or her authorized access, wittingly or unwittingly, "
              "to do harm to the national security of the United States."),
        ("p", "Need-to-Know: A determination that a prospective recipient requires "
              "access to specific information in order to perform a lawful and "
              "authorized Government function."),
        ("p", "Personnel Security Clearance (PCL): An administrative determination "
              "that an individual is eligible for access to classified "
              "information."),
        ("p", "Security Violation: A failure to comply with the policy and "
              "procedures established by the NISPOM rule that reasonably could "
              "result in the loss or compromise of classified information."),
    ]),
    ("Abbreviations and Acronyms", [
        ("ul", [
            "AFSO: Assistant Facility Security Officer",
            "CAGE: Commercial and Government Entity",
            "CMMC: Cybersecurity Maturity Model Certification",
            "COMSEC: Communications Security",
            "CUI: Controlled Unclassified Information",
            "DCSA: Defense Counterintelligence and Security Agency",
            "DIBNET: Defense Industrial Base Network",
            "DISS: Defense Information System for Security",
            "FCL: Facility Clearance",
            "FSO: Facility Security Officer",
            "ISR: Insider Threat Program Security Representative",
            "ITPSO: Insider Threat Program Senior Official",
            "NISPOM: National Industrial Security Program Operating Manual",
            "NIST: National Institute of Standards and Technology",
            "PCL: Personnel Security Clearance",
            "POA&M: Plan of Action and Milestones",
            "SEAD: Security Executive Agent Directive",
            "SMO: Senior Management Official",
            "SPP: Standard Practices and Procedures",
            "SSP: System Security Plan",
            "UEI: Unique Entity Identifier",
        ]),
    ]),
    ("References", [
        ("ul", [
            "32 CFR Part 117, National Industrial Security Program Operating "
            "Manual (NISPOM)",
            "32 CFR Part 2002, Controlled Unclassified Information",
            "NIST SP 800-171 Rev. 2, Protecting Controlled Unclassified "
            "Information in Nonfederal Systems and Organizations",
            "NIST SP 800-171A, Assessing Security Requirements for Controlled "
            "Unclassified Information",
            "NIST SP 800-88 Rev. 1, Guidelines for Media Sanitization",
            "CMMC Model Overview, Version 2.0, Department of Defense",
            "DFARS 252.204-7012, Safeguarding Covered Defense Information and "
            "Cyber Incident Reporting",
            "DFARS 252.204-7021, Cybersecurity Maturity Model Certification "
            "Requirements",
            "Security Executive Agent Directive (SEAD) 3, Reporting Requirements "
            "for Personnel with Access to Classified Information",
            "Executive Order 13526, Classified National Security Information",
            "Executive Order 13556, Controlled Unclassified Information",
            "DoD Instruction 5200.48, Controlled Unclassified Information",
        ]),
    ]),
]
