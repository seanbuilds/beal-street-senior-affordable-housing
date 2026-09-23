#!/usr/bin/env python3
"""
Compile 100 Beal Street 1-Page Printable Timeline, Status & Components Executive Briefing.
Project: 100 Beal Street Senior Affordable Housing (Hingham, MA)
Identifier: compile_one_page_timeline_and_components_pdf_v1.py
Constraint: Must strictly compile to exactly 1 page (8.5x11 Letter). Zero forbidden terms.
"""

import sys
import subprocess
import shutil
from pathlib import Path

BASE_DIR = Path("/Volumes/BLK4TB/Housing Topics/Beal Street Senior Affordable Housing")
SEAN_HERE_DIR = BASE_DIR / "SEAn_HERE"
ACTIVE_PROJECTS_SEAN_DIR = Path("/Volumes/BLK4TB/10_ACTIVE_PROJECTS/100_Beal_Street/SEAn_HERE")
REPORTS_DIR = BASE_DIR / "agent_created_deliverables" / "executive_reports"

MD_OUT = SEAN_HERE_DIR / "SEAn_HERE_09_One_Page_Timeline_Status_and_Components_v1.md"
PDF_OUT = SEAN_HERE_DIR / "SEAn_HERE_09_One_Page_Timeline_Status_and_Components_v1.pdf"
HTML_TMP = BASE_DIR / "temp_one_page_render_v1.html"

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>100 Beal Street: Timeline, Current Status & Project Components</title>
<style>
    @page {
        size: letter;
        margin: 0.28in 0.32in 0.25in 0.32in;
        @bottom-left {
            content: "Official Municipal Housing Record • Town of Hingham, MA • Hingham Housing Authority";
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 6.5pt;
            color: #718096;
        }
        @bottom-right {
            content: "Plymouth Registry Books 9516/291 & 51379/244 • 1-Page Master • Page 1 of 1";
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 6.5pt;
            font-weight: 700;
            color: #1A365D;
        }
    }

    * {
        box-sizing: border-box;
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #2D3748;
        line-height: 1.22;
        font-size: 7.2pt;
        margin: 0;
        padding: 0;
    }

    /* HEADER BAR */
    .header-box {
        background: linear-gradient(135deg, #0F2942 0%, #1A365D 50%, #2B6CB0 100%);
        color: #FFFFFF;
        padding: 8px 12px;
        border-radius: 4px;
        margin-bottom: 6px;
    }

    .header-table {
        width: 100%;
        border-collapse: collapse;
    }

    .header-title {
        font-size: 13.5pt;
        font-weight: 800;
        letter-spacing: 0.02em;
        color: #FFFFFF;
        margin: 0 0 2px 0;
        text-transform: uppercase;
    }

    .header-sub {
        font-size: 7.8pt;
        font-weight: 500;
        color: #E2E8F0;
        margin: 0;
    }

    .header-badge {
        text-align: right;
        font-size: 6.8pt;
        color: #FEFCBF;
        font-weight: 600;
        vertical-align: middle;
    }

    .badge-pill {
        display: inline-block;
        background: rgba(255, 255, 255, 0.18);
        border: 1px solid rgba(255, 255, 255, 0.4);
        padding: 3px 8px;
        border-radius: 3px;
        color: #FFFFFF;
        font-size: 6.6pt;
        font-weight: 700;
        letter-spacing: 0.03em;
        text-transform: uppercase;
    }

    /* SECTION TITLES */
    .section-title {
        font-size: 8.2pt;
        font-weight: 800;
        color: #1A365D;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        border-bottom: 1.5px solid #2B6CB0;
        padding-bottom: 2px;
        margin: 5px 0 4px 0;
        display: flex;
        justify-content: space-between;
    }

    .section-title span.tag {
        float: right;
        font-size: 6.4pt;
        font-weight: 600;
        color: #4A5568;
        text-transform: none;
        letter-spacing: normal;
    }

    /* WHERE WE ARE TODAY: 4-COLUMN METRICS */
    .status-grid {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 6px;
    }

    .status-grid td {
        width: 25%;
        padding: 4px 5px;
        vertical-align: top;
        background: #F7FAFC;
        border: 1px solid #CBD5E0;
    }

    .status-grid td:nth-child(1) {
        border-left: 3px solid #2B6CB0;
        border-radius: 3px 0 0 3px;
    }
    .status-grid td:nth-child(2) {
        border-left: 3px solid #319795;
    }
    .status-grid td:nth-child(3) {
        border-left: 3px solid #38A169;
    }
    .status-grid td:nth-child(4) {
        border-left: 3px solid #805AD5;
        border-radius: 0 3px 3px 0;
    }

    .status-card-header {
        font-size: 7.0pt;
        font-weight: 800;
        color: #1A365D;
        text-transform: uppercase;
        margin-bottom: 2px;
        line-height: 1.15;
    }

    .status-card-highlight {
        font-size: 8.0pt;
        font-weight: 800;
        margin-bottom: 2px;
        line-height: 1.15;
    }
    .c1 { color: #2B6CB0; }
    .c2 { color: #2C7A7B; }
    .c3 { color: #276749; }
    .c4 { color: #6B46C1; }

    .status-card-body {
        font-size: 6.5pt;
        color: #4A5568;
        line-height: 1.18;
    }

    /* TIMELINE: 10-MILESTONE 2-COLUMN TABLE */
    .timeline-table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 6px;
    }

    .timeline-table th {
        background: #EDF2F7;
        color: #2D3748;
        font-size: 6.6pt;
        font-weight: 800;
        text-transform: uppercase;
        padding: 3px 5px;
        border: 1px solid #CBD5E0;
        text-align: left;
    }

    .timeline-table td {
        padding: 2.8px 5px;
        border: 1px solid #E2E8F0;
        font-size: 6.6pt;
        line-height: 1.18;
        vertical-align: top;
    }

    .timeline-table tr:nth-child(even) td {
        background: #F8FAFC;
    }

    .t-date {
        font-weight: 800;
        color: #1A365D;
        white-space: nowrap;
        width: 12%;
    }

    .t-event {
        font-weight: 700;
        color: #2B6CB0;
        width: 25%;
    }

    .t-cite {
        color: #4A5568;
        font-style: italic;
        width: 28%;
    }

    .t-signif {
        color: #2D3748;
        width: 35%;
    }

    /* COMPONENTS: 6-BOX GRID (3x2) */
    .comp-grid {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 4px;
    }

    .comp-grid td {
        width: 33.33%;
        padding: 4px 6px;
        vertical-align: top;
        border: 1px solid #CBD5E0;
        background: #FFFFFF;
    }

    .comp-card-title {
        font-size: 7.2pt;
        font-weight: 800;
        color: #1A365D;
        margin-bottom: 2px;
        display: flex;
        align-items: center;
        border-bottom: 1px solid #E2E8F0;
        padding-bottom: 1px;
    }

    .comp-num {
        display: inline-block;
        background: #1A365D;
        color: #FFFFFF;
        width: 12px;
        height: 12px;
        line-height: 12px;
        text-align: center;
        border-radius: 50%;
        font-size: 6.0pt;
        font-weight: 700;
        margin-right: 4px;
    }

    .comp-list {
        margin: 2px 0 0 0;
        padding-left: 11px;
        font-size: 6.4pt;
        color: #334155;
        line-height: 1.20;
    }

    .comp-list li {
        margin-bottom: 1.5px;
    }

    .comp-list li strong {
        color: #0F172A;
    }

    /* BOTTOM SUMMARY / CALLOUT */
    .callout-bar {
        background: #F0F4F8;
        border: 1px solid #CBD5E0;
        border-left: 4px solid #1A365D;
        padding: 4px 8px;
        border-radius: 3px;
        margin-top: 4px;
        font-size: 6.4pt;
        color: #334155;
        line-height: 1.20;
    }

    .callout-bar strong {
        color: #1A365D;
    }
</style>
</head>
<body>

<!-- HEADER -->
<div class="header-box">
    <table class="header-table">
        <tr>
            <td>
                <div class="header-title">100 Beal Street Senior Affordable Housing</div>
                <div class="header-sub">Executive 1-Page Master Briefing: 37-Year Timeline, Current Posture & Project Architecture</div>
            </td>
            <td class="header-badge">
                <span class="badge-pill">September 2026 Status</span><br>
                <span style="font-size: 6.2pt; color: #E2E8F0;">Town of Hingham, MA • HHA & Peabody</span>
            </td>
        </tr>
    </table>
</div>

<!-- SECTION 1: WHERE WE ARE TODAY -->
<div class="section-title">
    1. Where We Are Today: Current Status Snapshot
    <span class="tag">Governed by M.G.L. c. 121B & Plymouth Registry Records</span>
</div>

<table class="status-grid">
    <tr>
        <td>
            <div class="status-card-header">Fee Simple Ownership</div>
            <div class="status-card-highlight c1">HHA Owns Lot B</div>
            <div class="status-card-body">
                HHA holds unencumbered fee simple title to 8.6-acre Lot B (Bk 9516, Pg 291). Encumbered by recorded Mass EOHLC c. 121B § 34 restriction (Bk 51379, Pg 244) legally barring any general municipal diversion.
            </div>
        </td>
        <td>
            <div class="status-card-header">Developer Partner</div>
            <div class="status-card-highlight c2">Peabody Properties</div>
            <div class="status-card-body">
                Designated developer under a 99-year ground lease and Land Disposition & Development Agreement (LDDA). Includes $500,000 upfront lease payment to HHA; public permanently retains land ownership.
            </div>
        </td>
        <td>
            <div class="status-card-header">Fiscal / Tax Impact</div>
            <div class="status-card-highlight c3">$0 Town Tax Dollars</div>
            <div class="status-card-body">
                $0 municipal debt, $0 town borrowing, and $0 capital outlay. 100% privately financed via Low-Income Housing Tax Credits (LIHTC), state subsidies, and private capital. Generates net revenue for HHA.
            </div>
        </td>
        <td>
            <div class="status-card-header">Permitting Track</div>
            <div class="status-card-highlight c4">MassHousing & Ch. 40B</div>
            <div class="status-card-body">
                Active MassHousing Project Eligibility Letter (PEL) submission, followed by Chapter 40B Comprehensive Permit filing with Hingham ZBA. Environmental lines secured via finalized MassDEP ORAD #034-1509.
            </div>
        </td>
    </tr>
</table>

<!-- SECTION 2: 37-YEAR TIMELINE -->
<div class="section-title">
    2. 37-Year Chronological Timeline: 1989 to 2026
    <span class="tag">Primary-Source Municipal & Registry Chronology</span>
</div>

<table class="timeline-table">
    <thead>
        <tr>
            <th style="width: 11%;">Date</th>
            <th style="width: 25%;">Decisive Event</th>
            <th style="width: 28%;">Governing Source & Citation</th>
            <th style="width: 36%;">Legal & Practical Significance</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="t-date">Dec 1989</td>
            <td class="t-event">Town Conveys Lot B to HHA</td>
            <td class="t-cite">Town Deed (Bk 9516, Pg 291)</td>
            <td class="t-signif">Conveys School Tract II (8.6 acres) to HHA with a 30-year youth home restriction.</td>
        </tr>
        <tr>
            <td class="t-date">Feb 2001</td>
            <td class="t-event">Remediation & 2001 MOU</td>
            <td class="t-cite">Selectmen & HHA MOU; Plan 155 of 2001</td>
            <td class="t-signif">Underground ammo bunker removed; ANR subdivides Lot A (Town DPW) and Lot B (HHA).</td>
        </tr>
        <tr>
            <td class="t-date">Apr–May 2006</td>
            <td class="t-event">Town 2/3 Senior Housing Vote</td>
            <td class="t-cite">2006 ATM Art. 22; Selectmen Vote</td>
            <td class="t-signif">Town Meeting authorizes senior housing; Selectmen vote deed release (remained unrecorded).</td>
        </tr>
        <tr>
            <td class="t-date">Feb 12, 2019</td>
            <td class="t-event">Select Board Litigation Vote</td>
            <td class="t-cite">Select Board Exec. Session (3–0 Vote)</td>
            <td class="t-signif">Town votes to authorize lawsuit against HHA to enforce 2001 MOU municipal co-determination.</td>
        </tr>
        <tr>
            <td class="t-date">Mar 19, 2019</td>
            <td class="t-event">30-Year Reverter Expires</td>
            <td class="t-cite">M.G.L. c. 184A, § 7 (Statutory Limit)</td>
            <td class="t-signif">1989 deed reverter and youth home restriction expire automatically by operation of state law.</td>
        </tr>
        <tr>
            <td class="t-date">Jul 19, 2019</td>
            <td class="t-event">State Statutory Restriction</td>
            <td class="t-cite">DHCD Recorded Notice (Bk 51379, Pg 244)</td>
            <td class="t-signif">State registers c. 121B § 34 restriction; locks parcel for state-regulated housing exclusively.</td>
        </tr>
        <tr>
            <td class="t-date">Sep 21, 2021</td>
            <td class="t-event">HHA Board Rescinds 2001 MOU</td>
            <td class="t-cite">HHA Board Resolution (4–0 Vote)</td>
            <td class="t-signif">Rescinded after DHCD legal opinion confirms MOU unlawfully divested Housing Authority authority.</td>
        </tr>
        <tr>
            <td class="t-date">Dec 16, 2024</td>
            <td class="t-event">MassDEP ORAD Approved</td>
            <td class="t-cite">ConCom Order (MassDEP #034-1509)</td>
            <td class="t-signif">5–0 vote establishes binding wetland line; confirms Depression D is non-jurisdictional upland.</td>
        </tr>
        <tr>
            <td class="t-date">Aug 19, 2025</td>
            <td class="t-event">Peabody Properties Selected</td>
            <td class="t-cite">HHA Board Designation & LDDA</td>
            <td class="t-signif">Selected via public RFP for 68 senior units; 99-year lease provides $500k upfront fee to HHA.</td>
        </tr>
        <tr>
            <td class="t-date">Apr–Sep 2026</td>
            <td class="t-event">CAL Defeated; 40B PEL Active</td>
            <td class="t-cite">2026 ATM Art. 14; MassHousing PEL</td>
            <td class="t-signif">Town CAL senior center defeated on Town Lot A; HHA independent senior housing advances on Lot B.</td>
        </tr>
    </tbody>
</table>

<!-- SECTION 3: ALL PROJECT COMPONENTS -->
<div class="section-title">
    3. Project Architecture: Core Components Breakdown
    <span class="tag">6-Pillar Operational & Technical Matrix</span>
</div>

<table class="comp-grid">
    <tr>
        <td>
            <div class="comp-card-title"><span class="comp-num">1</span> Site & Land Layout</div>
            <ul class="comp-list">
                <li><strong>Parcel:</strong> 8.6-acre Lot B at 100 Beal Street.</li>
                <li><strong>Upland Plateau:</strong> Building strictly sited on ~3.5-acre level, previously disturbed upland area.</li>
                <li><strong>Conservation Buffer:</strong> 100% of construction sits outside the 100-ft wetland buffer.</li>
                <li><strong>Flood Zone:</strong> 0 acres within 100-year FEMA flood plain.</li>
            </ul>
        </td>
        <td>
            <div class="comp-card-title"><span class="comp-num">2</span> Building Program</div>
            <ul class="comp-list">
                <li><strong>Scale:</strong> 3-story residential facility; 68 units.</li>
                <li><strong>Demographic:</strong> Independent seniors (Ages 62+).</li>
                <li><strong>Accessibility:</strong> 100% elevator-served, ADA/universal design, wide corridors, zero-step entries.</li>
                <li><strong>Amenities:</strong> Community hall, wellness exam room, library, on-site management, patio/gardens.</li>
            </ul>
        </td>
        <td>
            <div class="comp-card-title"><span class="comp-num">3</span> Affordability & Mix</div>
            <ul class="comp-list">
                <li><strong>100% Affordable:</strong> All 68 units count toward Hingham's Subsidized Housing Inventory (SHI).</li>
                <li><strong>Income Tiers:</strong> Restricted from 30% to 80% AMI to serve low- and moderate-income seniors.</li>
                <li><strong>Local Preference:</strong> Maximum ~70% statutory preference for Hingham residents, veterans, town staff.</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>
            <div class="comp-card-title"><span class="comp-num">4</span> Financing & Fiscal Impact</div>
            <ul class="comp-list">
                <li><strong>$0 Municipal Debt:</strong> Zero town borrowing or capital appropriations; zero municipal tax impact.</li>
                <li><strong>Private Capital:</strong> Peabody funds 100% via LIHTC equity, EOHLC subsidies, and private debt.</li>
                <li><strong>HHA Revenue:</strong> Generates $500,000 upfront lease payment to HHA to support local public housing.</li>
            </ul>
        </td>
        <td>
            <div class="comp-card-title"><span class="comp-num">5</span> Governance & Legal Title</div>
            <ul class="comp-list">
                <li><strong>99-Year Ground Lease:</strong> HHA retains permanent public fee ownership of the underlying land.</li>
                <li><strong>State Oversight:</strong> M.G.L. c. 121B and EOHLC ensure housing covenant perpetuity.</li>
                <li><strong>Title Resolution:</strong> Ministerial recording of 2006 Selectmen vote clears unrecorded title cloud.</li>
            </ul>
        </td>
        <td>
            <div class="comp-card-title"><span class="comp-num">6</span> Watershed Protection</div>
            <ul class="comp-list">
                <li><strong>Tucker's Swamp:</strong> Zero construction or direct runoff into peat bog or Hockley Run headwaters.</li>
                <li><strong>Depression D:</strong> Confirmed non-jurisdictional isolated depression under MassDEP ORAD #034-1509.</li>
                <li><strong>Stormwater:</strong> Modern closed-loop subsurface recharge system cleans and infiltrates 100% of on-site runoff.</li>
            </ul>
        </td>
    </tr>
</table>

<!-- FOOTER / CALLOUT BAR -->
<div class="callout-bar">
    <strong>Key Takeaway:</strong> 100 Beal Street Lot B is an independent, state-regulated 68-unit senior affordable housing initiative on Housing Authority land. It requires <strong>$0 in Town tax dollars</strong>, preserves natural buffers to Bare Cove Park, and provides critical, accessible homes for Hingham elders with <strong>~70% local preference</strong>.
</div>

</body>
</html>
"""

def main():
    print("Writing temporary HTML template...")
    HTML_TMP.write_text(HTML_CONTENT, encoding="utf-8")

    print(f"Compiling PDF via WeasyPrint: {PDF_OUT} ...")
    cmd = ["weasyprint", str(HTML_TMP), str(PDF_OUT)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error compiling PDF: {res.stderr}", file=sys.stderr)
        sys.exit(1)
    
    print("Compilation successful. Checking page count...")
    info_cmd = ["pdfinfo", str(PDF_OUT)]
    info_res = subprocess.run(info_cmd, capture_output=True, text=True)
    print(info_res.stdout)

    # Verify Pages: 1
    if "Pages:           1" not in info_res.stdout:
        print("WARNING: Document did not compile to exactly 1 page!", file=sys.stderr)
        for line in info_res.stdout.splitlines():
            if "Pages:" in line:
                print(f"Actual page count: {line.strip()}", file=sys.stderr)
        sys.exit(2)
    else:
        print("PASS: Verified exactly 1 page output.")

    # Mirror to active projects SEAn_HERE and executive_reports
    print("Mirroring to target project locations...")
    ACTIVE_PROJECTS_SEAN_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Copy PDF and MD to ACTIVE_PROJECTS_SEAN_DIR
    shutil.copy2(PDF_OUT, ACTIVE_PROJECTS_SEAN_DIR / PDF_OUT.name)
    shutil.copy2(MD_OUT, ACTIVE_PROJECTS_SEAN_DIR / MD_OUT.name)

    # Copy PDF to executive_reports
    shutil.copy2(PDF_OUT, REPORTS_DIR / PDF_OUT.name)
    shutil.copy2(MD_OUT, REPORTS_DIR / MD_OUT.name)

    print("Cleaning temporary HTML...")
    if HTML_TMP.exists():
        HTML_TMP.unlink()

    print("Completed successfully!")

if __name__ == "__main__":
    main()
