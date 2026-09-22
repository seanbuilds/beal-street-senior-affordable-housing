#!/usr/bin/env python3
"""
Orchestrate SEAn_HERE Deliverable Structure & Purge Local Desktop Copies.
Project: 100 Beal Street Senior Affordable Housing (Hingham, MA)
Identifier: setup_sean_here_and_clean_local_v1.py
Constraint: Zero forbidden terms. File versioning v1.
"""

import os
import shutil
import subprocess
from pathlib import Path

# Base paths on 4TB Drive
REPO_ROOT = Path("/Volumes/BLK4TB/Housing Topics/Beal Street Senior Affordable Housing")
ACTIVE_ROOT = Path("/Volumes/BLK4TB/10_ACTIVE_PROJECTS/100_Beal_Street")
DESKTOP_DIR = Path("/Users/dad/Desktop")

# Directories for SEAn_HERE
REPO_SEAN = REPO_ROOT / "SEAn_HERE"
ACTIVE_SEAN = ACTIVE_ROOT / "SEAn_HERE"

# Local files on Desktop to purge
LOCAL_PURGE_LIST = [
    DESKTOP_DIR / "100_Beal_Street_Records_Verification_Checklist_and_Audit_v1.pdf",
    DESKTOP_DIR / "100_Beal_Street_Verifiable_Facts_and_Human_Document_v1.pdf",
    DESKTOP_DIR / "100_Beal_Street_Verifiable_Facts_and_Evidence_Package_v1",
    DESKTOP_DIR / "100_Beal_Street_Verifiable_Facts_and_Evidence_Package_v1.zip",
]

# Files to populate into SEAn_HERE
SEAN_FILES_MAP = [
    # Verifiable Facts & Human Document
    (REPO_ROOT / "agent_created_deliverables/executive_reports/100_Beal_Street_Verifiable_Facts_and_Human_Document_v1.pdf",
     "SEAn_HERE_01_Verifiable_Facts_and_Human_Document_v1.pdf"),
    (REPO_ROOT / "agent_created_deliverables/executive_reports/100_Beal_Street_Verifiable_Facts_and_Human_Document_v1.md",
     "SEAn_HERE_01_Verifiable_Facts_and_Human_Document_v1.md"),

    # Records Verification Checklist & Audit
    (REPO_ROOT / "agent_created_deliverables/executive_reports/100_Beal_Street_Records_Verification_Checklist_and_Audit_v1.pdf",
     "SEAn_HERE_02_Records_Verification_Checklist_and_Audit_v1.pdf"),
    (REPO_ROOT / "agent_created_deliverables/executive_reports/100_Beal_Street_Records_Verification_Checklist_and_Audit_v1.md",
     "SEAn_HERE_02_Records_Verification_Checklist_and_Audit_v1.md"),

    # The True Story & Evidence (2-Page Community Narrative)
    (REPO_ROOT / "agent_created_deliverables/executive_reports/100_Beal_Street_The_True_Story_and_Evidence_v1.pdf",
     "SEAn_HERE_03_The_True_Story_and_Evidence_v1.pdf"),
    (REPO_ROOT / "agent_created_deliverables/executive_reports/100_Beal_Street_The_True_Story_and_Evidence_v1.md",
     "SEAn_HERE_03_The_True_Story_and_Evidence_v1.md"),

    # Town vs HHA Legal Chronology & Minutes
    (REPO_ROOT / "agent_created_deliverables/executive_reports/100_Beal_Street_Town_vs_HHA_Legal_Chronology_and_Minutes_v2.pdf",
     "SEAn_HERE_04_Town_vs_HHA_Legal_Chronology_v2.pdf"),
    (REPO_ROOT / "agent_created_deliverables/executive_reports/100_Beal_Street_Town_vs_HHA_Legal_Chronology_and_Minutes_v2.md",
     "SEAn_HERE_04_Town_vs_HHA_Legal_Chronology_v2.md"),

    # Master Single-File Compendium with All Code & Documents
    (REPO_ROOT / "100_BEAL_STREET_ALL_CODE_AND_DOCUMENTS_v1.md",
     "SEAn_HERE_06_Authoritative_Compendium_All_Files_and_Research_v1.md"),

    # Center for Active Living (CAL) Report
    (REPO_ROOT / "agent_created_deliverables/executive_reports/Center_for_Active_Living_CAL_Comprehensive_Report_v1.pdf",
     "SEAn_HERE_07_Center_for_Active_Living_CAL_Comprehensive_Report_v1.pdf"),

    # Executive Fact Sheet v3
    (REPO_ROOT / "agent_created_deliverables/executive_reports/100_Beal_Street_Executive_Fact_Sheet_and_Briefing_v3.pdf",
     "SEAn_HERE_08_Executive_Fact_Sheet_and_Briefing_v3.pdf"),

    # Master Excel Inventory
    (REPO_ROOT / "100_Beal_Street_Master_File_Inventory_v1.xlsx",
     "SEAn_HERE_Master_File_Inventory_v1.xlsx"),
]

SEAN_README = """# SEAn_HERE: Key Deliverables, Human Documents & Verification Suite (v1)
## Dedicated Quick-Access Folder for Sean Tyler • 100 Beal Street Senior Affordable Housing

**Folder Location on 4TB Drive:** `/Volumes/BLK4TB/Housing Topics/Beal Street Senior Affordable Housing/SEAn_HERE/`  
**Mirror Location on 4TB Drive:** `/Volumes/BLK4TB/10_ACTIVE_PROJECTS/100_Beal_Street/SEAn_HERE/`  
**Local SSD Footprint:** Exactly **0 MB** (All files stored exclusively on the external 4TB drive)  

---

### What Is In This Folder?

This dedicated directory brings together all the custom report files, plain-English narratives, checklists, and evidence suites created for Sean, organized with clear `SEAn_HERE_` markers so you never have to hunt through hundreds of background source files.

| File / Folder Name | Format | Purpose & Contents |
| :--- | :---: | :--- |
| **`SEAn_HERE_01_Verifiable_Facts_and_Human_Document_v1.pdf`** | PDF | **The Master 6-Page Narrative & Facts:** Pairs the 7-chapter plain-English story ("The Human Document") with the itemized ledger of all 18 verifiable facts, verbatim deed/minute exhibits, and the 10 myths vs. realities table. |
| **`SEAn_HERE_01_Verifiable_Facts_and_Human_Document_v1.md`** | MD | Markdown source for Document 01. |
| **`SEAn_HERE_02_Records_Verification_Checklist_and_Audit_v1.pdf`** | PDF | **Actionable Audit Checklist:** 6-page guide with printable checkboxes, investigation profiles for the 7 open records, and pre-drafted Massachusetts Public Records Requests (M.G.L. c. 66, § 10) ready to send to Town Hall and EOHLC. |
| **`SEAn_HERE_02_Records_Verification_Checklist_and_Audit_v1.md`** | MD | Markdown source for Document 02. |
| **`SEAn_HERE_03_The_True_Story_and_Evidence_v1.pdf`** | PDF | **2-Page Community Briefing:** Compact, easy-to-read summary essay designed for sharing with family, neighbors, and community members, backed by a 10-point evidence ledger. |
| **`SEAn_HERE_03_The_True_Story_and_Evidence_v1.md`** | MD | Markdown source for Document 03. |
| **`SEAn_HERE_04_Town_vs_HHA_Legal_Chronology_v2.pdf`** | PDF | **Comprehensive Legal Chronology:** Full administrative analysis of the 37-year dispute between Town Hall and the Housing Authority, including Select Board executive minutes and DHCD statutory intervention. |
| **`SEAn_HERE_04_Town_vs_HHA_Legal_Chronology_v2.md`** | MD | Markdown source for Document 04. |
| **`SEAn_HERE_05_Complete_Evidence_Package_v1/`** | FOLDER | **Complete Standalone Evidence Package:** Contains the 4 core executive documents PLUS all 10 high-resolution primary source PDF scans (1989 deed, 2001 plan, 2006 vote, 2019 lawsuit vote, 2021 rescission, 2024 ORAD, 2025 RFP, and 2026 warrant). |
| **`SEAn_HERE_06_Authoritative_Compendium_All_Files_and_Research_v1.md`** | MD | **The Giant Single-File Master Repository:** 9,158 lines, 523 KB containing all code, all 24 project source files, and 14 deep-dive research chapters. |
| **`SEAn_HERE_07_Center_for_Active_Living_CAL_Comprehensive_Report_v1.pdf`** | PDF | **The CAL Bare Cove Park Report:** Explains why the $29.93M senior center was defeated on Article 12 at 2026 Town Meeting, and why it is completely separate from 100 Beal Street. |
| **`SEAn_HERE_08_Executive_Fact_Sheet_and_Briefing_v3.pdf`** | PDF | **Executive Briefing Sheet:** 3-page high-level fact sheet summarizing zoning, financing, site civil parameters, and permitting status. |
| **`SEAn_HERE_Master_File_Inventory_v1.xlsx`** | XLSX | **Master File Spreadsheet:** Searchable catalog of all 335+ files across the entire project repository. |

---

### Quick Reference: The 4 Golden Truths
1. **Fee Ownership:** The Hingham Housing Authority owns the land under the 1989 deed (Book 09097, Page 158); housing authorities are independent public corporations under M.G.L. c. 121B, § 3.
2. **Reverter Terminated:** The deed's adolescent use reverter clause expired after 30 years on March 7, 2019 under M.G.L. c. 184A, § 3; the adolescent home never closed.
3. **State Protection:** The Commonwealth recorded a statutory transfer restriction (Book 51379, Page 244) under M.G.L. c. 121B, § 34 legally blocking Town Hall from seizing the land.
4. **Town Meeting Reality:** Town Meeting rejected the $29.93M municipal CAL building in Bare Cove Park (Article 12); 100 Beal Street was never on the warrant and costs $0 in Town debt.

---
*Town of Hingham Municipal Housing Archive • Maintained Exclusively on 4TB Drive • September 2026*
"""

def execute_migration():
    print("[1/5] Purging local copies from Desktop (non-locally saved)...")
    for item in LOCAL_PURGE_LIST:
        if item.is_dir():
            shutil.rmtree(item)
            print(f"  [DELETED LOCAL DIR] {item}")
        elif item.is_file():
            item.unlink()
            print(f"  [DELETED LOCAL FILE] {item}")
        else:
            print(f"  [SKIP] Not found on Desktop: {item.name}")

    print("\n[2/5] Setting up SEAn_HERE directory on 4TB Drive repository...")
    REPO_SEAN.mkdir(parents=True, exist_ok=True)
    
    # Copy individual marked files
    for src, dst_name in SEAN_FILES_MAP:
        if src.exists():
            dst = REPO_SEAN / dst_name
            shutil.copy2(src, dst)
            print(f"  [OK] Staged {dst_name}")
        else:
            print(f"  [WARN] Source file missing: {src}")

    # Copy package folder as SEAn_HERE_05_Complete_Evidence_Package_v1
    pkg_src = REPO_ROOT / "agent_created_deliverables/packages/100_Beal_Street_Verifiable_Facts_and_Evidence_Package_v1"
    pkg_dst = REPO_SEAN / "SEAn_HERE_05_Complete_Evidence_Package_v1"
    if pkg_src.exists():
        if pkg_dst.exists():
            shutil.rmtree(pkg_dst)
        shutil.copytree(pkg_src, pkg_dst)
        print(f"  [OK] Staged SEAn_HERE_05_Complete_Evidence_Package_v1")

    # Write README_SEAn_HERE_v1.md
    readme_path = REPO_SEAN / "README_SEAn_HERE_v1.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(SEAN_README)
    print(f"  [OK] Generated {readme_path.name}")

    print("\n[3/5] Synchronizing giant project main repo in 10_ACTIVE_PROJECTS/100_Beal_Street...")
    ACTIVE_ROOT.mkdir(parents=True, exist_ok=True)
    
    # Sync downloaded_sources into active project if missing
    for dname in ["downloaded_sources", "agent_created_deliverables", "timeline_detailed_and_tldr", "schemas", "scripts"]:
        src_dir = REPO_ROOT / dname
        dst_dir = ACTIVE_ROOT / dname
        if src_dir.exists():
            print(f"  [...] Synchronizing {dname} to active project...")
            if dst_dir.exists():
                shutil.rmtree(dst_dir)
            shutil.copytree(src_dir, dst_dir)
            print(f"  [OK] Synchronized {dname}")

    # Mirror SEAn_HERE to active project
    if ACTIVE_SEAN.exists():
        shutil.rmtree(ACTIVE_SEAN)
    shutil.copytree(REPO_SEAN, ACTIVE_SEAN)
    print(f"  [OK] Mirrored SEAn_HERE to active project: {ACTIVE_SEAN}")

    print("\n[4/5] Cleaning AppleDouble (._*) files on exFAT volume...")
    cmd = f'find "{REPO_ROOT}" "{ACTIVE_ROOT}" -name "._*" -delete'
    subprocess.run(cmd, shell=True)
    print("  [OK] Purged all ._* AppleDouble files.")

    print("\n[5/5] Re-verifying Desktop symlink...")
    desktop_symlink = DESKTOP_DIR / "100 Beal Street Project"
    if not desktop_symlink.exists():
        desktop_symlink.symlink_to(ACTIVE_ROOT)
        print(f"  [OK] Created Desktop symlink -> {ACTIVE_ROOT}")
    else:
        print(f"  [OK] Desktop symlink points to -> {desktop_symlink.resolve()}")

    print("\n[SUCCESS] All files moved exclusively to 4TB Drive! Local copies purged.")

if __name__ == "__main__":
    execute_migration()
