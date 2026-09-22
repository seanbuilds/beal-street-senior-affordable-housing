#!/usr/bin/env python3
"""
Compile 100 Beal Street Primary Records Verification Guide & Actionable Audit Checklist into a Publication-Grade PDF.
Project: 100 Beal Street Senior Affordable Housing (Hingham, MA)
Identifier: compile_verification_checklist_pdf_v1.py
Constraint: Zero forbidden terms. File versioning v1.
"""

import sys
import subprocess
import shutil
from pathlib import Path

BASE_DIR = Path("/Volumes/BLK4TB/Housing Topics/Beal Street Senior Affordable Housing")
REPORTS_DIR = BASE_DIR / "agent_created_deliverables" / "executive_reports"
ACTIVE_PROJECTS_DIR = Path("/Volumes/BLK4TB/10_ACTIVE_PROJECTS/100_Beal_Street")
DESKTOP_DIR = Path("/Users/dad/Desktop")
DESKTOP_PROJECT_DIR = Path("/Users/dad/Desktop/100 Beal Street Project")

MD_SRC = REPORTS_DIR / "100_Beal_Street_Records_Verification_Checklist_and_Audit_v1.md"
PDF_OUT = REPORTS_DIR / "100_Beal_Street_Records_Verification_Checklist_and_Audit_v1.pdf"
HTML_TMP = REPORTS_DIR / "temp_checklist_render_v1.html"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>100 Beal Street: Primary Records Verification Guide & Actionable Audit Checklist</title>
<style>
    @page {
        size: letter;
        margin: 0.5in 0.5in 0.55in 0.5in;
        @top-left {
            content: "100 Beal Street Senior Affordable Housing • Primary Records Verification Guide";
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 7pt;
            color: #718096;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        @top-right {
            content: "Official Document v1 • September 2026";
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 7pt;
            font-weight: 600;
            color: #4A5568;
        }
        @bottom-left {
            content: "Town of Hingham Municipal Housing Archive • Evidentiary Ledger & Audit Checklist";
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 7pt;
            color: #718096;
        }
        @bottom-right {
            content: "Page " counter(page) " of " counter(pages);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 7.5pt;
            font-weight: 700;
            color: #1A365D;
        }
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #2D3748;
        line-height: 1.35;
        font-size: 8.8pt;
        margin: 0;
        padding: 0;
    }

    h1, h2, h3, h4 {
        color: #1A365D;
        margin-top: 0;
        font-weight: 700;
    }

    .header-box {
        background: linear-gradient(135deg, #1A365D 0%, #2B6CB0 100%);
        color: #FFFFFF;
        padding: 14px 18px;
        border-radius: 5px;
        margin-bottom: 10px;
    }

    .header-box h1 {
        color: #FFFFFF;
        font-size: 16pt;
        margin-bottom: 4px;
        letter-spacing: -0.01em;
    }

    .header-box .subtitle {
        font-size: 9pt;
        color: #E2E8F0;
        font-weight: 400;
        margin-bottom: 8px;
        line-height: 1.3;
    }

    .meta-grid {
        display: table;
        width: 100%;
        margin-top: 6px;
        padding-top: 8px;
        border-top: 1px solid rgba(255, 255, 255, 0.25);
        font-size: 7.5pt;
    }

    .meta-col {
        display: table-cell;
        width: 25%;
        color: #CBD5E0;
    }

    .meta-col strong {
        color: #FFFFFF;
        display: block;
        font-size: 8pt;
    }

    .badge {
        display: inline-block;
        padding: 2px 6px;
        border-radius: 3px;
        font-size: 6.8pt;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    .badge-verified {
        background-color: #276749;
        color: #FFFFFF;
    }

    .badge-action {
        background-color: #C53030;
        color: #FFFFFF;
    }

    .badge-pending {
        background-color: #D69E2E;
        color: #FFFFFF;
    }

    .section-title {
        font-size: 11pt;
        border-bottom: 2px solid #2B6CB0;
        padding-bottom: 3px;
        margin-top: 12px;
        margin-bottom: 6px;
        color: #1A365D;
    }

    .section-desc {
        font-size: 8pt;
        color: #4A5568;
        margin-bottom: 8px;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        font-size: 7.6pt;
        margin-bottom: 10px;
    }

    th {
        background-color: #1A365D;
        color: #FFFFFF;
        font-weight: 600;
        text-align: left;
        padding: 5px 6px;
        border: 1px solid #1A365D;
    }

    td {
        padding: 4px 6px;
        border: 1px solid #E2E8F0;
        vertical-align: top;
    }

    tr:nth-child(even) td {
        background-color: #F8FAFC;
    }

    .item-card {
        border: 1px solid #CBD5E0;
        border-radius: 4px;
        margin-bottom: 10px;
        background-color: #FFFFFF;
        page-break-inside: avoid;
    }

    .item-card-header {
        background-color: #EDF2F7;
        padding: 6px 10px;
        border-bottom: 1px solid #CBD5E0;
        display: table;
        width: 100%;
        box-sizing: border-box;
    }

    .item-card-title {
        display: table-cell;
        font-size: 9pt;
        font-weight: 700;
        color: #1A365D;
    }

    .item-card-custodian {
        display: table-cell;
        text-align: right;
        font-size: 7.5pt;
        color: #4A5568;
        font-weight: 600;
    }

    .item-card-body {
        padding: 7px 10px;
        font-size: 8pt;
        line-height: 1.35;
    }

    .item-prop {
        margin-bottom: 3px;
    }

    .item-prop-label {
        font-weight: 700;
        color: #2B6CB0;
        display: inline-block;
        width: 95px;
    }

    .checklist-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 8pt;
        margin-top: 6px;
        margin-bottom: 12px;
    }

    .checklist-table th {
        background-color: #2B6CB0;
        color: #FFFFFF;
        padding: 6px 8px;
    }

    .checklist-table td {
        padding: 6px 8px;
        border: 1px solid #CBD5E0;
    }

    .checkbox-box {
        display: inline-block;
        width: 13px;
        height: 13px;
        border: 1.5px solid #2B6CB0;
        border-radius: 2px;
        vertical-align: middle;
        margin-right: 4px;
        background-color: #FFFFFF;
    }

    .template-box {
        background-color: #F8FAFC;
        border: 1px solid #CBD5E0;
        border-left: 3.5px solid #2B6CB0;
        border-radius: 4px;
        padding: 8px 12px;
        font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
        font-size: 7.2pt;
        line-height: 1.35;
        color: #2D3748;
        margin-bottom: 10px;
        white-space: pre-wrap;
        page-break-inside: avoid;
    }

    .template-title {
        font-size: 8.5pt;
        font-weight: 700;
        color: #1A365D;
        margin-top: 8px;
        margin-bottom: 3px;
    }

    .page-break {
        page-break-before: always;
    }

    .notice-box {
        background-color: #EBF8FF;
        border: 1px solid #BEE3F8;
        border-left: 3.5px solid #3182CE;
        padding: 6px 10px;
        border-radius: 4px;
        font-size: 7.8pt;
        color: #2B6CB0;
        margin-bottom: 8px;
        line-height: 1.3;
    }
</style>
</head>
<body>

<!-- PAGE 1: VERIFIED IN-HAND RECORDS LEDGER -->
<div class="header-box">
    <h1>100 Beal Street: Primary Records Verification Guide</h1>
    <div class="subtitle">An Evidentiary Ledger of In-Hand Primary Sources, Open Documentary Questions, and Actionable Public Audit Protocols</div>
    <div class="meta-grid">
        <div class="meta-col">
            <strong>Subject Property:</strong>
            100 Beal Street, Hingham (School Tract II)
        </div>
        <div class="meta-col">
            <strong>Record Fee Owner:</strong>
            Hingham Housing Authority (M.G.L. c. 121B)
        </div>
        <div class="meta-col">
            <strong>Proposed Development:</strong>
            68-Unit Senior Affordable Housing (Peabody)
        </div>
        <div class="meta-col">
            <strong>Document Identifier:</strong>
            v1 • Publication Date: Sep 2026
        </div>
    </div>
</div>

<div class="notice-box">
    <strong>Auditor's Evidentiary Standard:</strong> This document distinguishes between records <em>possessed, inspected, and verified</em> in the repository versus records that are <em>cited or referenced</em> but require independent inspection, docket searches, or public records requests.
</div>

<h2 class="section-title">1. Verified In-Hand Primary Records Ledger</h2>
<div class="section-desc">The following eleven primary records are fully possessed, transcribed, and verified within the project archive:</div>

<table>
    <thead>
        <tr>
            <th style="width: 4%; text-align: center;">#</th>
            <th style="width: 22%;">Record & Citation</th>
            <th style="width: 9%;">Date</th>
            <th style="width: 20%;">Public Custodian / Grantor</th>
            <th style="width: 9%; text-align: center;">Status</th>
            <th style="width: 36%;">Documented Legal Action</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center; font-weight: bold;">01</td>
            <td><strong>1989 Fee Deed</strong><br>Plymouth Bk 09097, Pg 158</td>
            <td>04/21/1989</td>
            <td>Town of Hingham &rarr; HHA</td>
            <td style="text-align: center;"><span class="badge badge-verified">VERIFIED</span></td>
            <td>Town conveyed 15.014-acre School Tract II for $45,751. Page 160 restricts use to adolescent facility with 30-year right of re-entry citing M.G.L. c. 184A, § 3.</td>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: bold;">02</td>
            <td><strong>1989 ZBA 40B Permit</strong><br>Plymouth Bk 09097, Pgs 162–170</td>
            <td>04/21/1989</td>
            <td>Hingham Zoning Board of Appeals</td>
            <td style="text-align: center;"><span class="badge badge-verified">VERIFIED</span></td>
            <td>Comprehensive Permit for 12-bed youth home; Condition 7 bars other structures on School Tract II without further ZBA relief.</td>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: bold;">03</td>
            <td><strong>Plan 100 of 2001 (Division)</strong><br>Plan Bk 44, Pg 412</td>
            <td>06/12/2001</td>
            <td>Gale Associates; Selectmen & HHA</td>
            <td style="text-align: center;"><span class="badge badge-verified">VERIFIED</span></td>
            <td>Survey divides land into 2.0-ac Lot 1 (youth home) and 8.02-ac Lot 2 (plateau) following Town-funded munitions bunker demolition.</td>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: bold;">04</td>
            <td><strong>2006 ATM Warrant Art. 38</strong><br>Certified Vote by Town Clerk</td>
            <td>05/01/2006</td>
            <td>Hingham Annual Town Meeting</td>
            <td style="text-align: center;"><span class="badge badge-verified">VERIFIED</span></td>
            <td>Town Meeting voted by declared 2/3 majority to authorize Selectmen to amend restriction to permit affordable senior housing.</td>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: bold;">05</td>
            <td><strong>Select Board Minutes</strong><br>Executive & Open Session</td>
            <td>02/26/2019</td>
            <td>Hingham Board of Selectmen</td>
            <td style="text-align: center;"><span class="badge badge-verified">VERIFIED</span></td>
            <td>Select Board voted 3–0 to authorize litigation against HHA to enforce 2001 agreement (voted 9 days prior to 30-yr deed anniversary).</td>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: bold;">06</td>
            <td><strong>Transfer Restriction Notice</strong><br>Plymouth Bk 51379, Pg 244</td>
            <td>07/18/2019</td>
            <td>Mass. DHCD / EOHLC & HHA</td>
            <td style="text-align: center;"><span class="badge badge-verified">VERIFIED</span></td>
            <td>Notice recorded under M.G.L. c. 121B, § 34 prohibiting transfer of School Tract II without state housing director approval.</td>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: bold;">07</td>
            <td><strong>HHA Rescission Vote</strong><br>Official Minutes, Pgs 3–4</td>
            <td>09/07/2021</td>
            <td>Hingham Housing Authority</td>
            <td style="text-align: center;"><span class="badge badge-verified">VERIFIED</span></td>
            <td>Board voted 4–0 to formally rescind the June 5, 2019 transfer motion, confirming permanent HHA fee ownership of 100 Beal Street.</td>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: bold;">08</td>
            <td><strong>MassDEP Recorded ORAD</strong><br>Plymouth Bk 59527, Pg 273</td>
            <td>12/10/2024</td>
            <td>MassDEP / Conservation Comm.</td>
            <td style="text-align: center;"><span class="badge badge-verified">VERIFIED</span></td>
            <td>Order of Resource Area Delineation confirms 155+ wetland flags and classifies Wetland D as non-jurisdictional depression.</td>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: bold;">09</td>
            <td><strong>Official Developer RFP</strong><br>155-Page Solicitation Package</td>
            <td>04/16/2025</td>
            <td>Hingham Housing Authority</td>
            <td style="text-align: center;"><span class="badge badge-verified">VERIFIED</span></td>
            <td>Procurement under M.G.L. c. 30B, § 16 for 99-year ground lease of 8.6-acre Lot B; includes Bohler civil study and CPA survey.</td>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: bold;">10</td>
            <td><strong>2024 ALTA Survey Note 3</strong><br>Control Point Associates, Sheet 1</td>
            <td>05/01/2024</td>
            <td>Title Examiner Kellem & Kellem</td>
            <td style="text-align: center;"><span class="badge badge-verified">VERIFIED</span></td>
            <td>Schedule B, Part II, Note 3 flags unreleased 1989 restriction: <em>"THEREFORE NEED RELEASE OR CHANGE OF THIS RESTRICTION FROM THE TOWN OF HINGHAM."</em></td>
        </tr>
        <tr>
            <td style="text-align: center; font-weight: bold;">11</td>
            <td><strong>HHA Developer Award Vote</strong><br>Official Minutes, Pg 2</td>
            <td>08/12/2025</td>
            <td>Hingham Housing Authority</td>
            <td style="text-align: center;"><span class="badge badge-verified">VERIFIED</span></td>
            <td>Board voted 4–0 to award 100 Beal Street development to Peabody Properties / AHSC and authorize Executive Director to enter LDDA.</td>
        </tr>
    </tbody>
</table>

<!-- PAGE 2: OPEN RECORDS ITEMS 1-4 -->
<div class="page-break"></div>

<h2 class="section-title">2. The 7 Critical Open Records Requiring Verification (Part 1: Items 1 to 4)</h2>
<div class="section-desc">Detailed investigation profiles for unobtained records, pending dockets, and municipal agreements:</div>

<div class="item-card">
    <div class="item-card-header">
        <div class="item-card-title">1. Complete Grantor/Grantee Deed Release Census (2006–Present)</div>
        <div class="item-card-custodian">Plymouth County Registry of Deeds</div>
    </div>
    <div class="item-card-body">
        <div class="item-prop"><span class="item-prop-label">Core Question:</span> Did the Selectmen ever record an instrument releasing or amending the 1989 restriction after the 2006 2/3 vote?</div>
        <div class="item-prop"><span class="item-prop-label">Why It Matters:</span> The 2024 ALTA Survey Note 3 indicates it was never recorded, leaving title encumbered. An exhaustive grantor/grantee title search eliminates any chance of a mis-indexed filing.</div>
        <div class="item-prop"><span class="item-prop-label">Verification:</span> Visit <code>plymouthdeeds.org</code>. Run Grantor search: <code>Town of Hingham</code> &rarr; Grantee: <code>Hingham Housing Authority</code> (2006–present). Filter codes: <code>REL</code>, <code>AMD</code>, <code>MOD</code>, <code>AGR</code>, <code>DEED</code>. Reverse search: Grantor: <code>HHA</code> &rarr; Grantee: <code>Town of Hingham</code>.</div>
        <div class="item-prop"><span class="item-prop-label">Target Finding:</span> Absence of recorded release confirms restriction remains active on title, requiring municipal release or 40B override.</div>
    </div>
</div>

<div class="item-card">
    <div class="item-card-header">
        <div class="item-card-title">2. The Executed 2001 Memorandum of Understanding (MOU)</div>
        <div class="item-card-custodian">Hingham Town Clerk / Select Board Office</div>
    </div>
    <div class="item-card-body">
        <div class="item-prop"><span class="item-prop-label">Core Question:</span> What are the exact terms, covenants, expiration dates, and municipal remedies in the signed June 12, 2001 agreement?</div>
        <div class="item-prop"><span class="item-prop-label">Why It Matters:</span> Plan 100 of 2001 cites an agreement of June 12, 2001. In 2019, the Select Board cited funds spent under this MOU to justify litigation. Without the text, the validity of Town contractual claims is unverified.</div>
        <div class="item-prop"><span class="item-prop-label">Verification:</span> File Public Records Request (M.G.L. c. 66, § 10) with Town Clerk / Select Board for the executed agreement referenced on Plan 100 of 2001.</div>
        <div class="item-prop"><span class="item-prop-label">Target Finding:</span> Review clauses to determine if MOU contained an expiration date, re-conveyance covenant, or administrative cost-sharing.</div>
    </div>
</div>

<div class="item-card">
    <div class="item-card-header">
        <div class="item-card-title">3. MassCourts Litigation Docket Search (2019 Lawsuit Check)</div>
        <div class="item-card-custodian">Massachusetts Trial Court (Plymouth Superior & Land Court)</div>
    </div>
    <div class="item-card-body">
        <div class="item-prop"><span class="item-prop-label">Core Question:</span> Did Town Counsel actually file a formal civil lawsuit after the Select Board voted 3–0 on February 26, 2019?</div>
        <div class="item-prop"><span class="item-prop-label">Why It Matters:</span> Proves whether the dispute was an active court case or resolved administratively before filing.</div>
        <div class="item-prop"><span class="item-prop-label">Verification:</span> Visit <code>masscourts.org</code>. Search Plymouth County Superior Court and Land Court. Parties: <code>Town of Hingham</code> vs. <code>Hingham Housing Authority</code> (Years: 2018–2022).</div>
        <div class="item-prop"><span class="item-prop-label">Target Finding:</span> If docket exists, obtain complaint to inspect formal claims; if none exists, confirms dispute was pre-litigation.</div>
    </div>
</div>

<div class="item-card">
    <div class="item-card-header">
        <div class="item-card-title">4. State DHCD Supervisory Warning Letters (April 19 & June 26, 2019)</div>
        <div class="item-card-custodian">Executive Office of Housing and Livable Communities (EOHLC)</div>
    </div>
    <div class="item-card-body">
        <div class="item-prop"><span class="item-prop-label">Core Question:</span> What statutory analysis did Associate Director Amy Stitely provide regarding state-assisted housing land?</div>
        <div class="item-prop"><span class="item-prop-label">Why It Matters:</span> These letters represent the state's legal basis under M.G.L. c. 121B, § 34 for blocking the municipal land recapture.</div>
        <div class="item-prop"><span class="item-prop-label">Verification:</span> Submit Public Records Request to EOHLC Public Records Officer for Amy Stitely letters to HHA/Town between April and July 2019.</div>
        <div class="item-prop"><span class="item-prop-label">Target Finding:</span> Verifies the Commonwealth's statutory interpretation asserting sole supervisory authority over Chapter 689 public land.</div>
    </div>
</div>

<!-- PAGE 3: OPEN RECORDS ITEMS 5-7 -->
<div class="page-break"></div>

<h2 class="section-title">2. The 7 Critical Open Records Requiring Verification (Part 2: Items 5 to 7)</h2>
<div class="section-desc">Detailed investigation profiles for pending board minutes, executed development agreements, and state permits:</div>

<div class="item-card">
    <div class="item-card-header">
        <div class="item-card-title">5. Certified HHA Board Minutes & Votes (June 5, 2019 & August 25, 2026)</div>
        <div class="item-card-custodian">Hingham Housing Authority Administrative Office</div>
    </div>
    <div class="item-card-body">
        <div class="item-prop"><span class="item-prop-label">Core Question:</span> What was the verbatim vote on June 5, 2019, and did the Board approve Item 9 on August 25, 2026?</div>
        <div class="item-prop"><span class="item-prop-label">Why It Matters:</span> An agenda proves scheduling; only approved, certified minutes legally prove official board action, vote tallies, and approvals.</div>
        <div class="item-prop"><span class="item-prop-label">Verification:</span> Contact HHA Executive Office (30 Thaxter Park) to inspect or request certified approved minutes for both dates.</div>
        <div class="item-prop"><span class="item-prop-label">Target Finding:</span> Confirms legal passage of Item 9 authorizing execution of the Land Disposition Agreement with Peabody Properties.</div>
    </div>
</div>

<div class="item-card">
    <div class="item-card-header">
        <div class="item-card-title">6. Executed Land Disposition Agreement (LDA) & Ground Lease</div>
        <div class="item-card-custodian">HHA Administration & Peabody Properties / AHSC</div>
    </div>
    <div class="item-card-body">
        <div class="item-prop"><span class="item-prop-label">Core Question:</span> Has the final LDA been executed, and what specific closing conditions and milestones are established?</div>
        <div class="item-prop"><span class="item-prop-label">Why It Matters:</span> The RFP contained draft templates. The executed contract establishes binding obligations, financing milestones, and contingencies.</div>
        <div class="item-prop"><span class="item-prop-label">Verification:</span> Request executed agreement from HHA; monitor Registry of Deeds for subsequent recording of Notice of Lease.</div>
        <div class="item-prop"><span class="item-prop-label">Target Finding:</span> Confirms whether municipal deed release is an explicit condition precedent before closing.</div>
    </div>
</div>

<div class="item-card">
    <div class="item-card-header">
        <div class="item-card-title">7. MassHousing Project Eligibility Letter (PEL) & Chapter 40B Filing</div>
        <div class="item-card-custodian">MassHousing & Hingham Zoning Board of Appeals</div>
    </div>
    <div class="item-card-body">
        <div class="item-prop"><span class="item-prop-label">Core Question:</span> Has MassHousing issued a formal PEL, and has the Comprehensive Permit application been filed with the ZBA?</div>
        <div class="item-prop"><span class="item-prop-label">Why It Matters:</span> The PEL is mandatory before the ZBA can open hearings under Chapter 40B, which provides the mechanism to override local deed restrictions.</div>
        <div class="item-prop"><span class="item-prop-label">Verification:</span> Monitor MassHousing 40B application portal and Hingham ZBA active hearing docket.</div>
        <div class="item-prop"><span class="item-prop-label">Target Finding:</span> Establishes the commencement of the statutory 180-day local Comprehensive Permit public hearing window.</div>
    </div>
</div>

<!-- PAGE 4: ACTIONABLE CHECKLIST -->
<div class="page-break"></div>

<h2 class="section-title">3. Actionable Records Verification Checklist</h2>
<div class="section-desc">Interactive and printable tracking matrix for document retrieval, inspection dates, and findings:</div>

<table class="checklist-table">
    <thead>
        <tr>
            <th style="width: 5%; text-align: center;">Done</th>
            <th style="width: 25%;">Record Item & Description</th>
            <th style="width: 24%;">Official Custodian</th>
            <th style="width: 23%;">Inspection Method</th>
            <th style="width: 23%;">Status / Notes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;"><div class="checkbox-box"></div></td>
            <td><strong>Deed Release Census</strong><br>1989 Restriction Run (2006–Pres.)</td>
            <td>Plymouth County Registry of Deeds (Brockton, MA)</td>
            <td>Online search at <code>plymouthdeeds.org</code> (Grantor: Hingham)</td>
            <td>Date: _____________ Score: ☐ Found ☐ None</td>
        </tr>
        <tr>
            <td style="text-align: center;"><div class="checkbox-box"></div></td>
            <td><strong>Executed 2001 MOU</strong><br>Naval Bunker Remediation Agr.</td>
            <td>Hingham Town Clerk / Select Board Office</td>
            <td>Public Records Request (M.G.L. c. 66, § 10)</td>
            <td>Date: _____________ Status: ☐ Pending ☐ Inspected</td>
        </tr>
        <tr>
            <td style="text-align: center;"><div class="checkbox-box"></div></td>
            <td><strong>Litigation Docket Search</strong><br>Town vs. HHA Court Filing Check</td>
            <td>Plymouth Superior Court / Massachusetts Land Court</td>
            <td>Electronic case search at <code>masscourts.org</code></td>
            <td>Date: _____________ Docket #: _____________</td>
        </tr>
        <tr>
            <td style="text-align: center;"><div class="checkbox-box"></div></td>
            <td><strong>DHCD Warning Letters</strong><br>Amy Stitely (Apr 19 & Jun 26, 2019)</td>
            <td>Executive Office of Housing & Livable Communities (EOHLC)</td>
            <td>Public Records Request to EOHLC Custodian</td>
            <td>Date: _____________ Status: ☐ Received ☐ Reviewed</td>
        </tr>
        <tr>
            <td style="text-align: center;"><div class="checkbox-box"></div></td>
            <td><strong>HHA Certified Minutes</strong><br>Votes: 06/05/2019 & 08/25/2026</td>
            <td>Hingham Housing Authority (30 Thaxter Park)</td>
            <td>In-person inspection / Board Secretary request</td>
            <td>Date: _____________ Aug 25 Tally: _________</td>
        </tr>
        <tr>
            <td style="text-align: center;"><div class="checkbox-box"></div></td>
            <td><strong>Executed Peabody LDA</strong><br>Land Disposition Agreement</td>
            <td>HHA Administration / Peabody Properties</td>
            <td>Contract inspection / Public Records Request</td>
            <td>Date: _____________ Closing Date: _________</td>
        </tr>
        <tr>
            <td style="text-align: center;"><div class="checkbox-box"></div></td>
            <td><strong>MassHousing PEL & 40B</strong><br>Comprehensive Permit Filing</td>
            <td>MassHousing / Hingham Zoning Board of Appeals</td>
            <td>Agency 40B portal / Town ZBA public hearing docket</td>
            <td>Date: _____________ ZBA Case #: __________</td>
        </tr>
    </tbody>
</table>

<!-- PAGE 5: PUBLIC RECORDS REQUEST TEMPLATES -->
<div class="page-break"></div>

<h2 class="section-title">4. Public Records Request Templates (M.G.L. c. 66, § 10)</h2>
<div class="section-desc">Pre-drafted formal public records requests ready for immediate submission:</div>

<div class="template-title">Template A: To Hingham Town Clerk & Select Board (For 2001 MOU)</div>
<div class="template-box">VIA EMAIL: townclerk@hingham-ma.gov / selectboard@hingham-ma.gov
To: Records Access Officer, Town of Hingham, 210 Central St, Hingham, MA 02043
RE: PUBLIC RECORDS REQUEST PURSUANT TO M.G.L. c. 66, § 10 — 2001 Beal Street MOU

Dear Records Access Officer:
Pursuant to M.G.L. c. 66, § 10, I hereby request digital copies of the following public record:
1. The fully executed Memorandum of Understanding (MOU), agreement, or contract entered into on or about June 12, 2001 between the Town of Hingham (acting through its Board of Selectmen) and the Hingham Housing Authority concerning School Tract II, 100 Beal Street, and/or the naval munitions bunker demolition and remediation, as referenced on recorded Plan 100 of 2001 (Plymouth Registry Plan Book 44, Page 412).
Please provide this record in electronic PDF format. If fees exceed $25.00, please notify me in advance.</div>

<div class="template-title">Template B: To State EOHLC (For 2019 Amy Stitely Supervisory Letters)</div>
<div class="template-box">VIA EMAIL: eohlcpublicrecords@mass.gov
To: Records Access Officer, Executive Office of Housing and Livable Communities, 100 Cambridge St, Suite 300, Boston, MA 02114
RE: PUBLIC RECORDS REQUEST PURSUANT TO M.G.L. c. 66, § 10 — 100 Beal Street (Project 689-01)

Dear Records Access Officer:
Pursuant to M.G.L. c. 66, § 10, I hereby request digital copies of the following public records in EOHLC custody:
1. Formal letters or written correspondence from Amy Stitely, Associate Director of Public Housing, to the Hingham Housing Authority and/or Town of Hingham officials dated on or about April 19, 2019 and June 26, 2019 regarding proposed transfers, statutory transfer restrictions, or property dispositions at 100 Beal Street (Project 689-01).
2. Any written approvals or conditional determination letters issued by EOHLC pursuant to M.G.L. c. 121B, § 34 regarding the long-term ground lease of 100 Beal Street (Lot B) from January 1, 2024 to present.</div>

<div class="template-title">Template C: To Hingham Housing Authority (For Certified Minutes & LDA)</div>
<div class="template-box">VIA EMAIL / IN-PERSON: Hingham Housing Authority, 30 Thaxter Park, Hingham, MA 02043
RE: PUBLIC RECORDS REQUEST PURSUANT TO M.G.L. c. 66, § 10 — Board Minutes & Land Disposition Agreement

Dear Records Access Officer:
Pursuant to M.G.L. c. 66, § 10, I hereby request digital copies of the following public records:
1. Approved meeting minutes and voting records for the HHA Special Meeting held on June 5, 2019.
2. Approved meeting minutes and voting records for the HHA Special Meeting held on August 25, 2026 (specifically Item 9 regarding approval of the Land Disposition Agreement with AHSC Peabody Developers LLC).
3. A copy of the executed Land Disposition and Development Agreement (LDDA) or Land Disposition Agreement between HHA and AHSC Peabody Developers LLC / Peabody Properties for 100 Beal Street (Lot B).</div>

<!-- PAGE 6: PUBLIC AGENCY DIRECTORY -->
<div class="page-break"></div>

<h2 class="section-title">5. Public Agency Directory & Official Portals</h2>
<div class="section-desc">Key public contact information, physical addresses, and online search repositories:</div>

<table>
    <thead>
        <tr>
            <th style="width: 25%;">Agency / Public Body</th>
            <th style="width: 25%;">Address & Office</th>
            <th style="width: 18%;">Telephone / Contact</th>
            <th style="width: 32%;">Official Search Portal / Website</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Plymouth County Registry of Deeds</strong></td>
            <td>50 Obery Street<br>Plymouth, MA 02360</td>
            <td>(508) 830-9200</td>
            <td><code>plymouthdeeds.org</code><br>(Search recorded deeds, plans, encumbrances)</td>
        </tr>
        <tr>
            <td><strong>Hingham Town Clerk</strong></td>
            <td>Town Hall, 210 Central St<br>Hingham, MA 02043</td>
            <td>(781) 741-1410</td>
            <td><code>hingham-ma.gov/town-clerk</code><br>(Certified Town Meeting votes & bylaws)</td>
        </tr>
        <tr>
            <td><strong>Hingham Select Board</strong></td>
            <td>Town Hall, 210 Central St<br>Hingham, MA 02043</td>
            <td>(781) 741-1451</td>
            <td><code>hingham-ma.gov/select-board</code><br>(Executive session minutes & municipal files)</td>
        </tr>
        <tr>
            <td><strong>Hingham Housing Authority</strong></td>
            <td>30 Thaxter Park<br>Hingham, MA 02043</td>
            <td>(781) 741-1417</td>
            <td><code>hinghamhousing.org</code><br>(Board minutes, developer RFP & LDA)</td>
        </tr>
        <tr>
            <td><strong>Executive Office of HLC (EOHLC)</strong></td>
            <td>100 Cambridge St, Suite 300<br>Boston, MA 02114</td>
            <td>(617) 573-1100</td>
            <td><code>mass.gov/orgs/eohlc</code><br>(c. 121B, § 34 state public housing approvals)</td>
        </tr>
        <tr>
            <td><strong>Massachusetts Trial Court</strong></td>
            <td>MassCourts Electronic Portal</td>
            <td>N/A</td>
            <td><code>masscourts.org</code><br>(Plymouth Superior & Land Court dockets)</td>
        </tr>
        <tr>
            <td><strong>MassHousing (40B Agency)</strong></td>
            <td>1 Beacon Street<br>Boston, MA 02108</td>
            <td>(617) 854-1000</td>
            <td><code>masshousing.com</code><br>(Project Eligibility Letters & 40B applications)</td>
        </tr>
        <tr>
            <td><strong>Hingham Zoning Board of Appeals</strong></td>
            <td>Town Hall, 210 Central St<br>Hingham, MA 02043</td>
            <td>(781) 741-1415</td>
            <td><code>hingham-ma.gov/zba</code><br>(Comprehensive Permit active hearings)</td>
        </tr>
    </tbody>
</table>

<div style="margin-top: 35px; padding-top: 14px; border-top: 1px solid #CBD5E0; font-size: 8pt; color: #718096; text-align: center; line-height: 1.4;">
    <strong>100 Beal Street Senior Affordable Housing • Official Records Verification Guide & Actionable Audit Checklist v1</strong><br>
    Town of Hingham Municipal Housing Archive • For Public Records Review & Informational Purposes Only • Not a Formal Title Opinion
</div>

</body>
</html>
"""

def generate_pdf():
    print(f"[...] Writing temporary HTML render to: {HTML_TMP}")
    with open(HTML_TMP, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE)

    print(f"[...] Compiling PDF via WeasyPrint to: {PDF_OUT}")
    cmd = ["/opt/homebrew/bin/weasyprint", str(HTML_TMP), str(PDF_OUT)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[ERROR] WeasyPrint compilation failed: {result.stderr}")
        sys.exit(result.returncode)

    if HTML_TMP.exists():
        HTML_TMP.unlink()

    print(f"[OK] Successfully compiled PDF: {PDF_OUT} ({PDF_OUT.stat().st_size:,} bytes)")

    # Mirror to active project folder and desktop
    ACTIVE_PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    dest_active = ACTIVE_PROJECTS_DIR / PDF_OUT.name
    shutil.copy2(PDF_OUT, dest_active)
    print(f"[OK] Mirrored PDF to: {dest_active}")

    # Mirror markdown as well
    shutil.copy2(MD_SRC, ACTIVE_PROJECTS_DIR / MD_SRC.name)
    print(f"[OK] Mirrored Markdown to: {ACTIVE_PROJECTS_DIR / MD_SRC.name}")

    if DESKTOP_DIR.exists():
        shutil.copy2(PDF_OUT, DESKTOP_DIR / PDF_OUT.name)
        print(f"[OK] Mirrored PDF to Desktop: {DESKTOP_DIR / PDF_OUT.name}")

    if DESKTOP_PROJECT_DIR.exists():
        shutil.copy2(PDF_OUT, DESKTOP_PROJECT_DIR / PDF_OUT.name)
        print(f"[OK] Mirrored PDF to Desktop Project folder: {DESKTOP_PROJECT_DIR / PDF_OUT.name}")

if __name__ == "__main__":
    generate_pdf()
