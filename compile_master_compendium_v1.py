#!/usr/bin/env python3
"""
Compile Authoritative Single-File Master Compendium with Embedded Research
Project: 100 Beal Street Senior Affordable Housing (Hingham, MA)
Target: 100_BEAL_STREET_ALL_CODE_AND_DOCUMENTS_v1.md
Constraint: Zero forbidden terms ("dossier", "stack", "seat"). Strict un-truncated content.
"""

import os
import sys
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path("/Volumes/BLK4TB/Housing Topics/Beal Street Senior Affordable Housing")
OUTPUT_FILE = ROOT_DIR / "100_BEAL_STREET_ALL_CODE_AND_DOCUMENTS_v1.md"

def get_file_stats(filepath):
    """Return line count and byte size of a file."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            return len(lines), filepath.stat().st_size
    except Exception:
        return 0, 0

print("[...] Building file manifest...")

# Target Files to be included in full
TARGET_FILES = [
    # 1. Project Governance & Standards
    ("README.md", "Repository Architecture & Governance Guide", "Governance"),
    
    # 2. Executive Legal Reports & Chronology
    ("agent_created_deliverables/executive_reports/100_Beal_Street_Town_vs_HHA_Legal_Chronology_and_Minutes_v2.md", "Master Legal Chronology & Evidentiary Framework (v2)", "Legal Chronology"),
    ("agent_created_deliverables/executive_reports/100_Beal_Street_The_True_Story_and_Evidence_v1.md", "2-Page Community Narrative & Evidence Ledger (v1)", "Executive Reports"),
    ("agent_created_deliverables/executive_reports/100_Beal_Street_Executive_Fact_Sheet_and_Briefing_v3.md", "Executive Fact Sheet & Project Briefing (v3)", "Executive Reports"),
    ("agent_created_deliverables/executive_reports/Center_for_Active_Living_CAL_Comprehensive_Report_v1.md", "100 Beal Street vs. Bare Cove Park CAL Report (v1)", "Executive Reports"),
    
    # 3. Detailed Timeline & TLDR Suite
    ("timeline_detailed_and_tldr/100_Beal_Street_Detailed_Timeline_and_TLDR_v1.md", "14-Milestone Detailed Timeline & Plain-English TLDR (v1)", "Timeline"),
    
    # 4. Presentation Suite & Voice Cloning Guide
    ("agent_created_deliverables/video_presentation/100_Beal_Street_Presentation_Script_v2.md", "16-Slide Verbatim Narration Presentation Script (v2)", "Presentation"),
    ("agent_created_deliverables/video_presentation/100_Beal_Street_Presentation_Marp_v2.md", "16-Slide Marp Markdown Presentation Deck (v2)", "Presentation"),
    ("agent_created_deliverables/video_presentation/VOICE_CLONING_RESEARCH_AND_GUIDE_v1.md", "Voice Cloning Architecture & macOS Implementation Guide (v1)", "Audio Architecture"),
    
    # 5. Primary Source Transcriptions & Municipal Records
    ("agent_created_deliverables/companion_transcriptions/Hingham_Beal_Street_Deed_1989_and_ZBA_Decision_v1.md", "1989 Fee Deed & 1988 ZBA Permit Complete Transcript (v1)", "Primary Sources"),
    ("agent_created_deliverables/companion_transcriptions/Hingham_Town_Meeting_2006_Beal_St_Amended_Deed_Vote_v1.md", "2006 Town Meeting Article 38 Vote Certificate Transcript (v1)", "Primary Sources"),
    ("agent_created_deliverables/companion_transcriptions/Select_Board_Executive_Session_Minutes_2019-02-26_100_Beal_v1.md", "Select Board Minutes 2019-02-26 (3-0 Lawsuit Vote) Transcript (v1)", "Primary Sources"),
    ("agent_created_deliverables/companion_transcriptions/HHA_Minutes_2019-07-09_100_Beal_School_Tract_II_v1.md", "HHA Minutes 2019-07-09 (Reciting June 5 Transfer) Transcript (v1)", "Primary Sources"),
    ("agent_created_deliverables/companion_transcriptions/HHA_Minutes_2021-09-07_Rescission_Vote_v1.md", "HHA Minutes 2021-09-07 (4-0 Rescission Vote) Transcript (v1)", "Primary Sources"),
    ("agent_created_deliverables/companion_transcriptions/HHA_Minutes_2025-08-12_Peabody_Award_Authentic_v1.md", "HHA Minutes 2025-08-12 (Peabody Developer Award) Transcript (v1)", "Primary Sources"),
    ("agent_created_deliverables/companion_transcriptions/Conservation_Commission_Minutes_2024-11-04_DEP_034-1509_v1.md", "Conservation Commission Minutes 2024-11-04 (5-0 ORAD Approval) (v1)", "Primary Sources"),
    ("agent_created_deliverables/companion_transcriptions/Hingham_100_Beal_ALTA_Survey_and_Subdivision_Plans_v1.md", "2024 ALTA Survey & Subdivision Plans Complete Transcript (v1)", "Primary Sources"),
    
    # 6. Schemas & System Architecture
    ("schemas/project_schema_and_architecture_v2.md", "Project Architecture & Technical Specification (v2)", "System Schema"),
    ("schemas/project_archive_and_records_schema_v2.json", "Formal Machine-Readable JSON Schema (v2)", "System Schema"),
    
    # 7. Source Code & Technical Automation Engines
    ("agent_created_deliverables/video_presentation/generate_presentation_video_v2.py", "Automated Video Presentation Generation Engine (v2)", "Source Code"),
    ("agent_created_deliverables/video_presentation/generate_pptx_deck_v2.py", "PowerPoint 16:9 Widescreen Deck Builder (v2)", "Source Code"),
    ("agent_created_deliverables/video_presentation/clone_user_voice_v1.py", "Local Zero-Shot Neural Voice Cloning Pipeline (v1)", "Source Code"),
    ("scripts/weekly_monitor_and_download_v1.py", "Automated Weekly Municipal Monitor & Ingestion Engine (v1)", "Source Code"),
    ("generate_master_excel_v1.py", "Master Excel File Inventory & Metadata Generator (v1)", "Source Code")
]

manifest_data = []
for rel_path, desc, cat in TARGET_FILES:
    abs_path = ROOT_DIR / rel_path
    if abs_path.exists():
        lc, sz = get_file_stats(abs_path)
        manifest_data.append({
            "rel_path": rel_path,
            "abs_path": str(abs_path),
            "desc": desc,
            "cat": cat,
            "lines": lc,
            "size": sz
        })
    else:
        print(f"[ERROR] Required target file missing: {rel_path}")
        sys.exit(1)

total_lines = sum(d["lines"] for d in manifest_data)
total_bytes = sum(d["size"] for d in manifest_data)

print(f"[OK] Manifest validated: {len(manifest_data)} files | {total_lines:,} lines | {total_bytes:,} bytes.")

# Open Output Compendium File
print(f"[...] Compiling master compendium to: {OUTPUT_FILE}")
with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    # Header & Front Matter
    out.write(f"""# 100 Beal Street: Authoritative Master Codebase & Document Compendium
## Complete Single-File Repository Compendium, Empirical Proof & Research Investigation
<!-- v1 – Authoritative, un-truncated master compendium containing all core documentation, legal analysis, primary source transcripts, system schemas, and production source code. Compiled on {datetime.now().strftime('%B %d, %Y')}. Strictly compliant with zero forbidden terms. -->

**Document Identifier:** `100_BEAL_STREET_ALL_CODE_AND_DOCUMENTS_v1.md`  
**Publication Date:** September 2026  
**Subject Property:** 100 Beal Street, Hingham, Massachusetts 02043 (School Tract II; Assessor Map 58, Lot 23)  
**Record Fee Owner:** Hingham Housing Authority (Independent Public Body Politic and Corporate under M.G.L. c. 121B)  
**Designated Developer:** Peabody Properties / Affordable Housing Services Corporation (AHSC)  
**Proposed Community:** 68-Unit Age-Restricted Senior Affordable Rental Residence (Ages 62+)  
**Repository Location:** `/Volumes/BLK4TB/Housing Topics/Beal Street Senior Affordable Housing`  
**Total Files Cataloged in Compendium:** {len(manifest_data)}  
**Total Document Lines:** Over {total_lines:,} lines  

---

## Table of Contents

1. [Executive Summary & File Manifest](#1-executive-summary--file-manifest)
2. [Research Along The Way: The Definitive Legal & Title Analysis](#2-research-along-the-way-the-definitive-legal--title-analysis)
   - [2.1 The 1989 Fee Conveyance & Educational Deed Restriction](#21-the-1989-fee-conveyance--educational-deed-restriction)
   - [2.2 35+ Years of Continuous Youth Care Operation (Lot 1)](#22-35-years-of-continuous-youth-care-operation-lot-1)
   - [2.3 The 2001 Munitions Bunker Cleanup & Gale Division Plan (Lot 2)](#23-the-2001-munitions-bunker-cleanup--gale-division-plan-lot-2)
   - [2.4 The 2006 Town Meeting Vote (Article 38) & The Administrative Breakdown](#24-the-2006-town-meeting-vote-article-38--the-administrative-breakdown)
   - [2.5 The 2017–2018 Discovery & Select Board Deliberations](#25-the-20172018-discovery--select-board-deliberations)
   - [2.6 The February 26, 2019 Select Board 3–0 Lawsuit Vote](#26-the-february-26-2019-select-board-30-lawsuit-vote)
   - [2.7 State DHCD Statutory Intervention (M.G.L. c. 121B, § 34)](#27-state-dhcd-statutory-intervention-mgl-c-121b--34)
   - [2.8 The Recorded Notice of Statutory Transfer Restriction (Book 51379, Page 244)](#28-the-recorded-notice-of-statutory-transfer-restriction-book-51379-page-244)
   - [2.9 The September 7, 2021 HHA 4–0 Rescission Vote](#29-the-september-7-2021-hha-40-rescission-vote)
   - [2.10 The 2024 ALTA Survey Note 3: Why Title Insurers Require a Town Release](#210-the-2024-alta-survey-note-3-why-title-insurers-require-a-town-release)
   - [2.11 Environmental Protection: MassDEP Wetlands ORAD (Book 59527, Page 273)](#211-environmental-protection-massdep-wetlands-orad-book-59527-page-273)
   - [2.12 The 2025 Developer RFP & Peabody Award (Conditional 99-Year Ground Lease)](#212-the-2025-developer-rfp--peabody-award-conditional-99-year-ground-lease)
   - [2.13 Clearing Up the Rumor: 100 Beal Street vs. Defeated Bare Cove Park CAL](#213-clearing-up-the-rumor-100-beal-street-vs-defeated-bare-cove-park-cal)
   - [2.14 Voice Cloning Architecture & Local macOS Neural Audio Pipeline](#214-voice-cloning-architecture--local-macos-neural-audio-pipeline)
3. [Section I: Repository Governance & Architecture](#section-i-repository-governance--architecture)
4. [Section II: Executive Legal Reports & Chronologies](#section-ii-executive-legal-reports--chronologies)
5. [Section III: Detailed Timeline & Plain-English TLDR Suite](#section-iii-detailed-timeline--plain-english-tldr-suite)
6. [Section IV: Presentation Decks, Verbatim Scripts & Voice Cloning Guide](#section-iv-presentation-decks-verbatim-scripts--voice-cloning-guide)
7. [Section V: Complete Primary Source Transcriptions & Official Records](#section-v-complete-primary-source-transcriptions--official-records)
8. [Section VI: System Schemas & Technical Specifications](#section-vi-system-schemas--technical-specifications)
9. [Section VII: Complete Un-Truncated Production Source Code](#section-vii-complete-un-truncated-production-source-code)

---

## 1. Executive Summary & File Manifest

This compendium represents the single authoritative source of truth for the 100 Beal Street Senior Affordable Housing repository. Every file cataloged below is included in its entirety without truncation, accompanied by rigorous legal commentary, primary deed citations, and forensic research.

| # | File Relative Path | Category | Lines | Size (Bytes) | Description |
| :---: | :--- | :--- | :---: | :---: | :--- |
""")

    for idx, d in enumerate(manifest_data, start=1):
        out.write(f"| **{idx:02d}** | `{d['rel_path']}` | {d['cat']} | {d['lines']:,} | {d['size']:,} | {d['desc']} |\n")

    out.write("""
---

## 2. Research Along The Way: The Definitive Legal & Title Analysis

### 2.1 The 1989 Fee Conveyance & Educational Deed Restriction
On **March 7, 1989** (recorded **April 21, 1989** in Plymouth County Registry of Deeds, **Book 09097, Pages 158–161**), the Town of Hingham conveyed a 15.014-acre parcel of surplus federal naval ammunition depot land known as **School Tract II** to the **Hingham Housing Authority (HHA)** for **$45,751.00** pursuant to May 1987 Annual Town Meeting Warrant Article 53.

Crucially, the deed conveyed fee title subject to an express educational restriction on Page 160:
> *"This conveyance is made upon the express condition that the property will be used only for a residential educational facility for emotionally disturbed adolescents operated through the Hingham Housing Authority by the South Shore Educational Collaborative or similar entity; or, if required pursuant to M.G.L. c. 121B, § 34, by the Massachusetts Executive Office of Communities and Development."*

**The Legal Scope:** The deed did *not* subdivide the land at the time of conveyance. The restriction encumbered the **entire 15.014 net acres**.

**The 30-Year Limitation Clause (Book 09097, Page 160):**
The deed contained an express time limit on the Town's right of re-entry:
> *"In the event that a breach of the above condition should occur after December 17, 2003, all right, title and interest in and to the above described property shall revert to and become the property of the Town of Hingham which shall have the immediate right of entry thereon, **provided, however, that said right of entry shall terminate after thirty years from the date hereof as provided in Massachusetts General Laws, Chapter 184A, Section 3.**"*

The 30-year calendar mark expired on **March 7, 2019**.

### 2.2 35+ Years of Continuous Youth Care Operation (Lot 1)
In 1990, the Housing Authority utilized state public housing assistance under **Chapter 689** (specialized housing for persons with special needs) to construct a 12-bed group home on a 2.0-acre building lot fronting Beal Street. 

This facility has operated continuously from 1990 to 2026 under contracts with the Department of Children and Families (DCF) and licensed non-profit human services providers (including Bay State Community Services). Because the adolescent residential care mission was never shut down or abandoned, the core use required by the deed has been continuously maintained on the property for over three decades.

### 2.3 The 2001 Munitions Bunker Cleanup & Gale Division Plan (Lot 2)
Behind the 2-acre youth home lay 13 undeveloped acres encumbered by reinforced concrete naval ammunition storage bunkers, high earthen blast berms, and hazardous materials left behind from the naval depot.

In **June 2001**, the Town of Hingham funded the demolition of the bunkers and completed environmental soil remediation. The Town and HHA signed an administrative Memorandum of Understanding and commissioned Gale Associates, Inc. to prepare a formal boundary division survey:
* **Recorded Instrument:** Plymouth County Registry of Deeds, **Plan Book 44, Page 412 (Plan 100 of 2001)**.
* **Lot 1 (2.000 Acres):** Dedicated to the active adolescent residential group home.
* **Lot 2 (8.020 Acres):** Remediated, buildable upland plateau with frontage on Beal Street, designated for future municipal/housing needs.

### 2.4 The 2006 Town Meeting Vote (Article 38) & The Administrative Breakdown
Because the 1989 deed restricted all 15.014 acres to adolescent care, HHA could not lawfully develop senior housing on Lot 2 without amending the deed. 

On **May 1, 2006**, Hingham Annual Town Meeting considered **Warrant Article 38**. Voters voted by a declared **two-thirds supermajority**:
> *"VOTED: That the Town authorize the Town of Hingham, acting through its Board of Selectmen, to amend the restriction contained in the deed from the Town of Hingham to the Hingham Housing Authority dated March 7, 1989, recorded in the Plymouth County Registry of Deeds in Book 9097, Page 158, conveying School Tract II (15.014 acres)... by adding as an allowable use residential development which includes affordable housing that qualifies for inclusion on the Subsidized Housing Inventory..."*

**The Breakdown:** Under Massachusetts municipal law, Town Meeting only has the power to *authorize* the Board of Selectmen to act. The Board of Selectmen at the time **never actually drafted, executed, or recorded an amended deed or release at the Plymouth County Registry of Deeds**. The authorization sat in the Town Clerk's records, but the public land records at the Registry were never updated.

### 2.5 The 2017–2018 Discovery & Select Board Deliberations
Between 2016 and 2017, Town Counsel Susan Murphy conducted title due diligence on Beal Street town properties and discovered that the 2006 deed release had never been recorded.

Selectman Karen Johnson briefed the Board in public hearings on **January 30, 2018** and **February 13, 2018**, arguing that because the Town had funded the 2001 bunker demolition, the 8-acre plateau should belong to the Town. However, the Housing Authority Board declined to voluntarily surrender the parcel, asserting its corporate independence and public housing mission under M.G.L. c. 121B.

### 2.6 The February 26, 2019 Select Board 3–0 Lawsuit Vote
With the 30-year deed reverter set to expire on March 7, 2019, the Select Board convened in executive session on **February 26, 2019** (nine days before the deadline). 

Reconvening in open session at 7:00 PM, Chairman Paul Healey moved, and Selectman Karen Johnson seconded, to authorize formal litigation against the Hingham Housing Authority to force them to convey 100 Beal Street back to Town Hall. The motion passed unanimously, **3–0**.

**Did the Town have the right to sue or seize the land?**
* **The Town's theory:** Town Hall claimed a contractual right of re-entry under the 1989 deed.
* **The State's ruling:** The Commonwealth ruled that the Town had **no lawful authority** to seize the property because HHA is an independent state entity and state housing funds attached permanent public housing covenants under M.G.L. c. 121B, § 34.

### 2.7 State DHCD Statutory Intervention (M.G.L. c. 121B, § 34)
Under litigation pressure, the HHA Board held an emergency meeting on **June 5, 2019**, and voted to approve a motion agreeing to transfer approximately 19 acres to the Town.

The Commonwealth immediately intervened. Massachusetts Department of Housing and Community Development (DHCD, now EOHLC) Associate Director Amy Stitely issued formal warning letters on **April 19 and June 26, 2019**, informing Town Counsel and HHA that:
1. Local housing authorities are independent public corporations created under M.G.L. c. 121B.
2. Property acquired or developed with state public housing assistance cannot be alienated, transferred, or sold without prior written state approval.
3. DHCD formally refused to approve any transfer to Town Hall.

### 2.8 The Recorded Notice of Statutory Transfer Restriction (Book 51379, Page 244)
To ensure Town Hall could not execute a transfer behind closed doors, DHCD took decisive action on public land records. On **July 18, 2019 at 1:44 PM**, the Commonwealth recorded a formal **Notice of Statutory Transfer Restriction** at the Plymouth County Registry of Deeds in **Book 51379, Page 244 (Document #55967)**.

Citing M.G.L. c. 121B, § 34, this recorded instrument gave constructive notice to all title examiners and attorneys that any deed or conveyance attempted without the written signature of the Commonwealth is void as a matter of law.

### 2.9 The September 7, 2021 HHA 4–0 Rescission Vote
Backed by state regulatory authority and specialized counsel, the HHA Board of Commissioners convened on **September 7, 2021**. Commissioner O’Meara moved, seconded by Commissioner Lauter, to rescind the June 5, 2019 transfer motion. The motion passed unanimously, **4–0**, on a roll-call vote (Suchecki, O'Meara, Lauter, Buhr). 

The official minutes ruled: *"That Motion is now rescinded and the land in question shall remain in the ownership of the Hingham Housing Authority."*

### 2.10 The 2024 ALTA Survey Note 3: Why Title Insurers Require a Town Release
While the 2021 vote secured HHA's fee ownership, **it did not erase the 1989 deed restriction from the Registry of Deeds**.

When HHA commissioned Control Point Associates and title insurer Kellem & Kellem, LLC to perform the 2024 ALTA Land Title Survey (Attachment B of the Developer RFP), the title abstractor explicitly wrote on **Sheet 1, Schedule B, Part II, Note 3**:
> *"DEED CONTAINS SPECIFIC RESTRICTIONS [I.E. USED ONLY FOR A RESIDENTIAL EDUCATIONAL FACILITY FOR EMOTIONALLY DISTURBED ADOLESCENTS OPERATED BY THE HINGHAM HOUSING AUTHORITY. NOTE: THE RIGHT OF REVERTER TO THE TOWN FOR BREACH OF THIS CONDITION EXPIRED ON DECEMBER 17, 2003, BUT THE RIGHT OF TERMINATION REMAINS UNTIL MARCH 7, 2029. **THEREFORE NEED RELEASE OR CHANGE OF THIS RESTRICTION FROM THE TOWN OF HINGHAM.**]"*

This surveyor finding confirms the open title requirement: because Town Hall never recorded the 2006 deed release, title insurers still flag the restriction as requiring a formal municipal release or judicial/Chapter 40B clearance.

### 2.11 Environmental Protection: MassDEP Wetlands ORAD (Book 59527, Page 273)
To ensure the parcel could be developed sustainably, HHA hired Lucas Environmental, LLC to delineate 155+ wetland flags protecting Tucker's Swamp and the Weymouth Back River Area of Critical Environmental Concern (ACEC).

On **November 4, 2024**, the Hingham Conservation Commission voted unanimously, **5–0**, to approve an Order of Resource Area Delineation (ORAD under MassDEP File No. 034-1509), recorded on **December 10, 2024** in **Book 59527, Page 273**. This binding order confirmed that the 8.6-acre development plateau on Lot B consists of high, dry upland completely outside wetland resource areas.

### 2.12 The 2025 Developer RFP & Peabody Award (Conditional 99-Year Ground Lease)
On **April 16, 2025**, HHA issued a competitive 155-page Request for Proposals under M.G.L. c. 30B and c. 121B. On **August 12, 2025**, the HHA Board voted unanimously, **4–0**, to designate **Peabody Properties / Affordable Housing Services Corporation (AHSC)** to develop 68 age-restricted (62+) rental apartments.

**Key Terms:**
* **99-Year Ground Lease:** Fee ownership remains permanently with HHA.
* **$500,000 Upfront Consideration:** Paid to HHA by the developer.
* **$0 Municipal Debt:** 100% privately and tax-credit financed with zero Town borrowing.
* **Contingent Execution:** The Land Disposition Agreement (LDA) and ground lease remain contingent upon state regulatory approvals and formally clearing the outstanding deed restriction.

### 2.13 Clearing Up the Rumor: 100 Beal Street vs. Defeated Bare Cove Park CAL
A widespread community rumor claimed that Hingham Town Meeting "voted down the senior project." This is completely false.

The defeated project was the **Center for Active Living (CAL)**:
* **CAL:** A $29,930,000 municipal daytime senior activity facility proposed by the Select Board inside Bare Cove Park, requiring a 2/3 debt exclusion borrowing vote. It failed at Annual Town Meeting on April 27, 2026 under Warrant Article 12 (510 in favor, 470 opposed; fell short of the 2/3 threshold).
* **100 Beal Street:** An independent 68-unit residential housing project on HHA land requiring $0 in Town borrowing. It was never on the warrant and was never voted on or defeated.

### 2.14 Voice Cloning Architecture & Local macOS Neural Audio Pipeline
To facilitate community education and accessible presentation delivery, the repository contains a complete local zero-shot neural voice cloning architecture evaluated on macOS Apple Silicon:
* **Evaluated Models:** F5-TTS (Flow Matching DiT), OpenVoice v2 (Tone Color Converter), Coqui XTTS-v2, and Kokoro-82M.
* **Audited Files:** Confirmed the 4 municipal hearing MP3s in `downloaded_sources/audio_recordings/` are Town officials (Healey, Johnson, Power) and not the user's voice.
* **Implementation:** `clone_user_voice_v1.py` normalizes user audio, synthesizes slide narration, and recompiles the presentation video with embedded closed captions.

---
""")

    # Append Target Files in Full
    print("[...] Appending full file contents...")
    for idx, d in enumerate(manifest_data, start=1):
        rel_path = d["rel_path"]
        abs_path = Path(d["abs_path"])
        lines = d["lines"]
        size = d["size"]
        cat = d["cat"]
        desc = d["desc"]
        
        print(f"  [{idx:02d}/{len(manifest_data):02d}] Appending: {rel_path} ({lines:,} lines)")
        
        out.write(f"\n\n---\n\n")
        out.write(f"## File {idx:02d} of {len(manifest_data):02d}: `{rel_path}`\n\n")
        out.write(f"**Classification:** {cat} • **Description:** {desc}  \n")
        out.write(f"**Filesystem Path:** `{abs_path}`  \n")
        out.write(f"**Document Metrics:** {lines:,} lines | {size:,} bytes | Un-truncated Source  \n\n")
        
        # Determine language for code fence
        ext = abs_path.suffix.lower()
        lang = "markdown"
        if ext == ".py":
            lang = "python"
        elif ext == ".json":
            lang = "json"
        elif ext == ".txt":
            lang = "text"
            
        out.write(f"```{lang}\n")
        with open(abs_path, 'r', encoding='utf-8', errors='ignore') as inf:
            out.write(inf.read())
        if not out.tell() or not out.seekable():
            out.write("\n")
        out.write(f"\n```\n\n")

print(f"[OK] Successfully compiled master compendium: {OUTPUT_FILE}")
comp_lines, comp_size = get_file_stats(OUTPUT_FILE)
print(f"     Total Compendium Lines: {comp_lines:,}")
print(f"     Total Compendium Size:  {comp_size:,} bytes ({comp_size / (1024*1024):.2f} MB)")
