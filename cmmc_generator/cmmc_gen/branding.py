"""Shared python-docx helpers that reproduce the AVASO template look.

Style cues taken from the AVASO Federal Solutions SPP 2026 and the AVASO
Awareness and Training Policy: a centered cover page with the company
logo, name, address block, and CAGE code; a Forward section; a field-code
Table of Contents; numbered Heading 1 sections; and a footer with the
document title and page numbers.
"""

import datetime

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

HEADING_COLOR = RGBColor(0x1F, 0x38, 0x64)
BODY_FONT = "Calibri"
TITLE_FONT = "Calibri Light"


def new_document():
    doc = Document()
    styles = doc.styles
    normal = styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = Pt(11)
    for level, size in (("Heading 1", 16), ("Heading 2", 13), ("Heading 3", 12)):
        st = styles[level]
        st.font.name = TITLE_FONT
        st.font.size = Pt(size)
        st.font.color.rgb = HEADING_COLOR
        st.font.bold = True
    title = styles["Title"]
    title.font.name = TITLE_FONT
    title.font.size = Pt(28)
    title.font.color.rgb = HEADING_COLOR
    return doc


def _set_cell_shading(cell, hex_color):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), hex_color)
    cell._tc.get_or_add_tcPr().append(shd)


def add_page_number_footer(doc, left_text):
    """Footer styled after the AVASO template: doc title left, page X right."""
    footer = doc.sections[0].footer
    footer.is_linked_to_previous = False
    para = footer.paragraphs[0]
    para.text = ""
    tab_stops = para.paragraph_format.tab_stops
    tab_stops.add_tab_stop(Inches(6.5), 2)  # right aligned tab stop
    run = para.add_run(left_text + "\t")
    run.font.size = Pt(9)
    run.font.name = BODY_FONT
    page_run = para.add_run()
    page_run.font.size = Pt(9)
    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = "PAGE"
    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    page_run._r.append(fld_begin)
    page_run._r.append(instr)
    page_run._r.append(fld_end)


def add_header(doc, profile, doc_title):
    header = doc.sections[0].header
    header.is_linked_to_previous = False
    para = header.paragraphs[0]
    para.text = ""
    para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = para.add_run(f"{profile['company_short_name']} | {doc_title}")
    run.font.size = Pt(9)
    run.font.name = BODY_FONT
    run.font.color.rgb = RGBColor(0x59, 0x59, 0x59)


def add_cover_page(doc, profile, doc_title, subtitle=""):
    """Cover page per the AVASO SPP: logo, title, company block, CAGE code."""
    if profile.get("logo_path"):
        logo_para = doc.add_paragraph()
        logo_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        logo_para.add_run().add_picture(profile["logo_path"], width=Inches(2.5))

    title_para = doc.add_paragraph(style="Title")
    title_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_para.add_run(doc_title)

    if subtitle:
        sub = doc.add_paragraph()
        sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = sub.add_run(subtitle)
        r.font.size = Pt(14)
        r.font.color.rgb = HEADING_COLOR

    doc.add_paragraph()
    for line in (
        profile["company_legal_name"],
        profile["address_line1"],
        profile["address_line2"],
        f"CAGE CODE: {profile['cage_code']}",
        f"UEI: {profile['uei']}",
    ):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(line)
        r.font.size = Pt(12)
        if line == profile["company_legal_name"]:
            r.bold = True
            r.font.size = Pt(14)

    doc.add_paragraph()
    date_para = doc.add_paragraph()
    date_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    date_para.add_run(datetime.date.today().strftime("%B %d, %Y")).font.size = Pt(11)


def add_disclosure_statement(doc, profile):
    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(
        "DISCLOSURE STATEMENT: This document is the property of "
        f"{profile['company_legal_name']} and contains company sensitive "
        "information. It is provided for official use by employees, "
        "consultants, and authorized government representatives only. "
        "Reproduction or further distribution outside "
        f"{profile['company_short_name']} requires the written approval of "
        "the Facility Security Officer."
    )
    run.font.size = Pt(9)
    run.italic = True


def add_page_break(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def add_toc(doc):
    """Insert a TOC field. Word populates it on open (References > Update Table)."""
    h = doc.add_paragraph()
    r = h.add_run("Table of Contents")
    r.font.name = TITLE_FONT
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = HEADING_COLOR

    para = doc.add_paragraph()
    run = para.add_run()
    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = 'TOC \\o "1-3" \\h \\u'
    fld_sep = OxmlElement("w:fldChar")
    fld_sep.set(qn("w:fldCharType"), "separate")
    placeholder = OxmlElement("w:t")
    placeholder.text = ("Right-click and choose Update Field to build the "
                        "Table of Contents with page numbers.")
    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    run._r.append(fld_begin)
    run._r.append(instr)
    run._r.append(fld_sep)
    run._r.append(placeholder)
    run._r.append(fld_end)


def add_document_history_table(doc, profile):
    """Document History table styled after the AVASO policy template."""
    doc.add_paragraph().add_run("Document History").bold = True
    table = doc.add_table(rows=2, cols=6)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Version Number", "Author", "Revision Date", "Approved by",
               "Approval Date", "Reason/Description of Changes"]
    for cell, text in zip(table.rows[0].cells, headers):
        cell.text = ""
        run = cell.paragraphs[0].add_run(text)
        run.bold = True
        run.font.size = Pt(9)
        _set_cell_shading(cell, "D9E2F3")
    today = datetime.date.today().strftime("%m/%d/%Y")
    values = [profile.get("policy_version", "1.0"),
              profile.get("fso_name", ""),
              today,
              profile.get("approved_by") or profile.get("smo_name", ""),
              today,
              "Initial release"]
    for cell, text in zip(table.rows[1].cells, values):
        cell.text = ""
        cell.paragraphs[0].add_run(text).font.size = Pt(9)


def styled_table(doc, headers, shade="1F3864", font_color=RGBColor(0xFF, 0xFF, 0xFF)):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    for cell, text in zip(table.rows[0].cells, headers):
        cell.text = ""
        run = cell.paragraphs[0].add_run(text)
        run.bold = True
        run.font.size = Pt(9)
        run.font.color.rgb = font_color
        _set_cell_shading(cell, shade)
    return table


def add_table_row(table, values, size=9):
    row = table.add_row()
    for cell, text in zip(row.cells, values):
        cell.text = ""
        cell.paragraphs[0].add_run(str(text)).font.size = Pt(size)
    return row


def add_signature_block(doc, lines):
    """lines: list of (name, title) tuples, each given a signature rule."""
    doc.add_paragraph()
    for name, title in lines:
        doc.add_paragraph("_" * 40)
        p = doc.add_paragraph()
        p.add_run(name).bold = True
        doc.add_paragraph(title)
        doc.add_paragraph()


def add_approval_block(doc, profile):
    """Approval table: prepared by FSO, approved by SMO, effective date."""
    table = styled_table(doc, ["Role", "Name", "Signature", "Date"],
                         shade="D9E2F3", font_color=RGBColor(0x1F, 0x38, 0x64))
    effective = profile.get("effective_date") or \
        datetime.date.today().strftime("%m/%d/%Y")
    add_table_row(table, ["Prepared by (FSO)", profile.get("fso_name", ""),
                          "", ""], size=10)
    add_table_row(table, ["Approved by (SMO)",
                          profile.get("approved_by") or profile.get("smo_name", ""),
                          "", ""], size=10)
    p = doc.add_paragraph()
    p.add_run(f"Effective date: {effective}").bold = True
    return table


def add_checkbox_item(doc, text):
    p = doc.add_paragraph()
    p.add_run("☐  ")
    p.add_run(text)
    return p
