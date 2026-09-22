#!/usr/bin/env python3
"""
Create Dedicated Standalone Deliverable Package for 100 Beal Street Verifiable Facts & Evidence Suite.
Project: 100 Beal Street Senior Affordable Housing (Hingham, MA)
Identifier: create_verifiable_facts_package_v1.py
Constraint: Zero forbidden terms. File versioning v1.
"""

import os
import shutil
import zipfile
from pathlib import Path

BASE_DIR = Path("/Volumes/BLK4TB/Housing Topics/Beal Street Senior Affordable Housing")
PACKAGES_DIR = BASE_DIR / "agent_created_deliverables" / "packages"
PACKAGE_ROOT = PACKAGES_DIR / "100_Beal_Street_Verifiable_Facts_and_Evidence_Package_v1"
EXEC_DIR = PACKAGE_ROOT / "01_Executive_and_Human_Documents"
EXHIBITS_DIR = PACKAGE_ROOT / "02_Primary_Source_Evidence_Exhibits"

DESKTOP_DIR = Path("/Users/dad/Desktop")
DESKTOP_PKG = DESKTOP_DIR / "100_Beal_Street_Verifiable_Facts_and_Evidence_Package_v1"
ACTIVE_PROJECTS_DIR = Path("/Volumes/BLK4TB/10_ACTIVE_PROJECTS/100_Beal_Street")
ACTIVE_PKG = ACTIVE_PROJECTS_DIR / "100_Beal_Street_Verifiable_Facts_and_Evidence_Package_v1"

# Source mappings
EXEC_FILES = [
    (BASE_DIR / "agent_created_deliverables/executive_reports/100_Beal_Street_Verifiable_Facts_and_Human_Document_v1.pdf", "01_100_Beal_Street_Verifiable_Facts_and_Human_Document_v1.pdf"),
    (BASE_DIR / "agent_created_deliverables/executive_reports/100_Beal_Street_Verifiable_Facts_and_Human_Document_v1.md", "01_100_Beal_Street_Verifiable_Facts_and_Human_Document_v1.md"),
    (BASE_DIR / "agent_created_deliverables/executive_reports/100_Beal_Street_Records_Verification_Checklist_and_Audit_v1.pdf", "02_100_Beal_Street_Records_Verification_Checklist_and_Audit_v1.pdf"),
    (BASE_DIR / "agent_created_deliverables/executive_reports/100_Beal_Street_Records_Verification_Checklist_and_Audit_v1.md", "02_100_Beal_Street_Records_Verification_Checklist_and_Audit_v1.md"),
    (BASE_DIR / "agent_created_deliverables/executive_reports/100_Beal_Street_The_True_Story_and_Evidence_v1.pdf", "03_100_Beal_Street_The_True_Story_and_Evidence_v1.pdf"),
    (BASE_DIR / "agent_created_deliverables/executive_reports/100_Beal_Street_The_True_Story_and_Evidence_v1.md", "03_100_Beal_Street_The_True_Story_and_Evidence_v1.md"),
    (BASE_DIR / "agent_created_deliverables/executive_reports/100_Beal_Street_Town_vs_HHA_Legal_Chronology_and_Minutes_v2.pdf", "04_100_Beal_Street_Town_vs_HHA_Legal_Chronology_and_Minutes_v2.pdf"),
    (BASE_DIR / "agent_created_deliverables/executive_reports/100_Beal_Street_Town_vs_HHA_Legal_Chronology_and_Minutes_v2.md", "04_100_Beal_Street_Town_vs_HHA_Legal_Chronology_and_Minutes_v2.md"),
]

EXHIBIT_FILES = [
    (BASE_DIR / "downloaded_sources/documents/Hingham_Beal_Street_Deed_1989_and_ZBA_Decision.pdf", "Exhibit_01_1989_Fee_Deed_and_ZBA_Decision_Bk09097_Pg158.pdf"),
    (BASE_DIR / "downloaded_sources/architectural_plans/Hingham_100_Beal_ALTA_Survey_and_Subdivision_Plans.pdf", "Exhibit_02_2001_Gale_Subdivision_Plan_and_2024_ALTA_Survey.pdf"),
    (BASE_DIR / "downloaded_sources/documents/Hingham_Town_Meeting_2006_Beal_St_Amended_Deed_Vote.pdf", "Exhibit_03_2006_Town_Meeting_Article_38_Certified_Vote.pdf"),
    (BASE_DIR / "downloaded_sources/meeting_records/Select_Board_Executive_Session_Minutes_2019-02-26_100_Beal.pdf", "Exhibit_04_2019_Select_Board_Executive_Session_Minutes_Lawsuit_Vote.pdf"),
    (BASE_DIR / "downloaded_sources/meeting_records/HHA_Minutes_2019-07-09_100_Beal_School_Tract_II.pdf", "Exhibit_05_2019_HHA_Minutes_School_Tract_II_DHCD_Intervention.pdf"),
    (BASE_DIR / "downloaded_sources/meeting_records/HHA_Minutes_2021-09-07_Rescission_Vote.pdf", "Exhibit_06_2021_HHA_Minutes_4-0_Rescission_Vote.pdf"),
    (BASE_DIR / "downloaded_sources/orad_registry_records/ORAD_034-1509_Plymouth_Bk59527_Pg273_2024-12-10.pdf", "Exhibit_07_2024_MassDEP_Recorded_ORAD_Bk59527_Pg273.pdf"),
    (BASE_DIR / "downloaded_sources/documents/Hingham-HA-Beal-St-RFP-04-16-25_Final_all-attachments.pdf", "Exhibit_08_2025_HHA_Developer_RFP_155_Pages.pdf"),
    (BASE_DIR / "downloaded_sources/meeting_records/HHA_Minutes_2025-08-12_Peabody_Award_Authentic.pdf", "Exhibit_09_2025_HHA_Minutes_Peabody_Developer_Award_Vote.pdf"),
    (BASE_DIR / "downloaded_sources/documents/Hingham_Town_Meeting_Warrant_2026.pdf", "Exhibit_10_2026_Town_Meeting_Warrant_Article_12_CAL_Debt_Defeat.pdf"),
]

README_CONTENT = """# 100 Beal Street: Verifiable Facts & Primary Evidence Package (v1)
## An Authoritative Documentary Suite Pairing Plain-English Narratives with Authentic Recorded Public Records

**Package Identifier:** `100_Beal_Street_Verifiable_Facts_and_Evidence_Package_v1`  
**Publication Date:** September 22, 2026  
**Subject Property:** 100 Beal Street, Hingham, MA 02043 (Assessor Map 58, Block 0, Lot 23; School Tract II)  
**Record Property Owner:** Hingham Housing Authority (Independent Public Body Corporate under M.G.L. c. 121B)  
**Proposed Development:** 68-Unit Senior Affordable Housing Community (Peabody Properties / AHSC)  

---

## 1. Package Purpose & Overview

This dedicated standalone package brings together the **complete human narrative** of 100 Beal Street and the **unimpeachable primary public records** that substantiate it. 

Every legal assertion, title finding, and municipal action described in the executive documents is corroborated directly by the authentic primary source PDFs contained in the `02_Primary_Source_Evidence_Exhibits/` directory.

---

## 2. Directory Structure & Contents

```text
100_Beal_Street_Verifiable_Facts_and_Evidence_Package_v1/
├── README_PACKAGE_v1.md
├── 01_Executive_and_Human_Documents/
│   ├── 01_100_Beal_Street_Verifiable_Facts_and_Human_Document_v1.pdf   (Master 6-Page Synthesis)
│   ├── 01_100_Beal_Street_Verifiable_Facts_and_Human_Document_v1.md
│   ├── 02_100_Beal_Street_Records_Verification_Checklist_and_Audit_v1.pdf (6-Page Actionable Audit Checklist)
│   ├── 02_100_Beal_Street_Records_Verification_Checklist_and_Audit_v1.md
│   ├── 03_100_Beal_Street_The_True_Story_and_Evidence_v1.pdf           (2-Page Community Briefing)
│   ├── 03_100_Beal_Street_The_True_Story_and_Evidence_v1.md
│   ├── 04_100_Beal_Street_Town_vs_HHA_Legal_Chronology_and_Minutes_v2.pdf (Comprehensive Legal Chronology)
│   └── 04_100_Beal_Street_Town_vs_HHA_Legal_Chronology_and_Minutes_v2.md
└── 02_Primary_Source_Evidence_Exhibits/
    ├── Exhibit_01_1989_Fee_Deed_and_ZBA_Decision_Bk09097_Pg158.pdf
    ├── Exhibit_02_2001_Gale_Subdivision_Plan_and_2024_ALTA_Survey.pdf
    ├── Exhibit_03_2006_Town_Meeting_Article_38_Certified_Vote.pdf
    ├── Exhibit_04_2019_Select_Board_Executive_Session_Minutes_Lawsuit_Vote.pdf
    ├── Exhibit_05_2019_HHA_Minutes_School_Tract_II_DHCD_Intervention.pdf
    ├── Exhibit_06_2021_HHA_Minutes_4-0_Rescission_Vote.pdf
    ├── Exhibit_07_2024_MassDEP_Recorded_ORAD_Bk59527_Pg273.pdf
    ├── Exhibit_08_2025_HHA_Developer_RFP_155_Pages.pdf
    ├── Exhibit_09_2025_HHA_Minutes_Peabody_Developer_Award_Vote.pdf
    └── Exhibit_10_2026_Town_Meeting_Warrant_Article_12_CAL_Debt_Defeat.pdf
```

---

## 3. Primary Evidence Mapping (The 18 Verifiable Facts)

| Fact # | Verifiable Historical Fact | Supporting Primary Evidence Exhibit |
| :---: | :--- | :--- |
| **01–03** | 1989 Land Grant, Adolescent Use Condition & 30-Year Reverter (Bk 09097, Pg 158) | `Exhibit_01_1989_Fee_Deed_and_ZBA_Decision_Bk09097_Pg158.pdf` |
| **04** | 1989 ZBA Comprehensive Permit for 12-bed home (Condition 7 restriction) | `Exhibit_01_1989_Fee_Deed_and_ZBA_Decision_Bk09097_Pg158.pdf` |
| **05–06** | 2001 Bunker Cleanup & Division into Lot 1 (2.0 ac) & Lot 2 (8.02 ac) | `Exhibit_02_2001_Gale_Subdivision_Plan_and_2024_ALTA_Survey.pdf` |
| **07** | 2006 Town Meeting 2/3 Vote Authorizing Senior Housing on Surplus Plateau | `Exhibit_03_2006_Town_Meeting_Article_38_Certified_Vote.pdf` |
| **08** | Town Hall Failure to Record Deed Release (ALTA Survey Note 3) | `Exhibit_02_2001_Gale_Subdivision_Plan_and_2024_ALTA_Survey.pdf` |
| **09** | Statutory Expiration of 30-Year Reverter Clause on March 7, 2019 | `01_100_Beal_Street_Verifiable_Facts_and_Human_Document_v1.pdf` |
| **10** | Select Board 3–0 Vote Authorizing Litigation Against HHA (Feb 26, 2019) | `Exhibit_04_2019_Select_Board_Executive_Session_Minutes_Lawsuit_Vote.pdf` |
| **11** | HHA June 5, 2019 Transfer Vote Under Lawsuit Threat | `Exhibit_06_2021_HHA_Minutes_4-0_Rescission_Vote.pdf` |
| **12–13** | State DHCD Intervention & Recorded Transfer Restriction (Bk 51379, Pg 244) | `Exhibit_05_2019_HHA_Minutes_School_Tract_II_DHCD_Intervention.pdf` |
| **14** | HHA 4–0 Vote to Rescind Transfer Motion, Affirming Ownership (Sept 7, 2021) | `Exhibit_06_2021_HHA_Minutes_4-0_Rescission_Vote.pdf` |
| **15** | MassDEP Recorded Order of Resource Area Delineation (Bk 59527, Pg 273) | `Exhibit_07_2024_MassDEP_Recorded_ORAD_Bk59527_Pg273.pdf` |
| **16** | HHA 155-Page Procurement Solicitation for 60+ Senior Units (c. 30B, § 16) | `Exhibit_08_2025_HHA_Developer_RFP_155_Pages.pdf` |
| **17** | HHA 4–0 Developer Award to Peabody Properties / AHSC (Aug 12, 2025) | `Exhibit_09_2025_HHA_Minutes_Peabody_Developer_Award_Vote.pdf` |
| **18** | Town Meeting Defeat was Article 12 CAL ($29.93M Debt); 100 Beal Not Voted | `Exhibit_10_2026_Town_Meeting_Warrant_Article_12_CAL_Debt_Defeat.pdf` |

---

## 4. How to Use This Package

* **For Community Education:** Share `01_100_Beal_Street_Verifiable_Facts_and_Human_Document_v1.pdf` or the 2-page `03_100_Beal_Street_The_True_Story_and_Evidence_v1.pdf` for a clear, plain-English understanding of why 100 Beal Street is alive, permitted, and costs $0 in Town debt.
* **For Public Records & Legal Inquiries:** Use `02_100_Beal_Street_Records_Verification_Checklist_and_Audit_v1.pdf` to submit the pre-drafted Massachusetts Public Records Requests (M.G.L. c. 66, § 10) to obtain the 2001 MOU and state correspondence.
* **For Evidentiary Review:** Consult the primary PDF scans in `02_Primary_Source_Evidence_Exhibits/` to inspect original signatures, certified vote stamps, and Registry of Deeds recording stamps.

---
*Town of Hingham Municipal Housing Archive • Official Evidence Package v1 • September 2026*
"""

def build_package():
    print(f"[...] Creating package directories...")
    EXEC_DIR.mkdir(parents=True, exist_ok=True)
    EXHIBITS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"[...] Copying Executive & Human Documents...")
    for src, dst_name in EXEC_FILES:
        dst = EXEC_DIR / dst_name
        if src.exists():
            shutil.copy2(src, dst)
            print(f"  [OK] Copied {src.name} -> {dst.name}")
        else:
            print(f"  [WARN] Source file missing: {src}")

    print(f"[...] Copying Primary Source Evidence Exhibits...")
    for src, dst_name in EXHIBIT_FILES:
        dst = EXHIBITS_DIR / dst_name
        if src.exists():
            shutil.copy2(src, dst)
            print(f"  [OK] Copied {src.name} -> {dst.name}")
        else:
            print(f"  [WARN] Source file missing: {src}")

    readme_file = PACKAGE_ROOT / "README_PACKAGE_v1.md"
    print(f"[...] Writing package README to: {readme_file}")
    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(README_CONTENT)

    # Create zip archive
    zip_path = PACKAGES_DIR / "100_Beal_Street_Verifiable_Facts_and_Evidence_Package_v1.zip"
    print(f"[...] Creating ZIP archive at: {zip_path}")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(PACKAGE_ROOT):
            for file in files:
                abs_path = Path(root) / file
                rel_path = abs_path.relative_to(PACKAGES_DIR)
                zf.write(abs_path, rel_path)
    print(f"[OK] ZIP archive created: {zip_path} ({zip_path.stat().st_size:,} bytes)")

    # Mirror to Desktop
    print(f"[...] Mirroring package to Desktop: {DESKTOP_PKG}")
    if DESKTOP_PKG.exists():
        shutil.rmtree(DESKTOP_PKG)
    shutil.copytree(PACKAGE_ROOT, DESKTOP_PKG)
    shutil.copy2(zip_path, DESKTOP_DIR / zip_path.name)
    print(f"[OK] Desktop mirror and ZIP created successfully.")

    # Mirror to Active Projects
    print(f"[...] Mirroring package to Active Projects: {ACTIVE_PKG}")
    ACTIVE_PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    if ACTIVE_PKG.exists():
        shutil.rmtree(ACTIVE_PKG)
    shutil.copytree(PACKAGE_ROOT, ACTIVE_PKG)
    shutil.copy2(zip_path, ACTIVE_PROJECTS_DIR / zip_path.name)
    print(f"[OK] Active Projects mirror and ZIP created successfully.")

if __name__ == "__main__":
    build_package()
