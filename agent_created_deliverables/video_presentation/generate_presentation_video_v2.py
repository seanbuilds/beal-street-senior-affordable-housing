#!/usr/bin/env python3
"""
Complete Video Generation & Synthesis Pipeline for 100 Beal Street (Version 2)
Project: 100 Beal Street Senior Affordable Housing (Hingham, MA)
Identifier: generate_presentation_video_v2.py
Constraint: Zero forbidden terms. File versioning v2.
Integrates exact legal reality: 1989 deed adolescent restriction across all 15 acres,
unrecorded 2006 Town Meeting release, 2024 ALTA survey note, and contingent Peabody lease.
"""

import os
import sys
import subprocess
import shutil
import json
import argparse
from pathlib import Path

BASE_DIR = Path("/Volumes/BLK4TB/Housing Topics/Beal Street Senior Affordable Housing/agent_created_deliverables/video_presentation")
SLIDES_HTML_DIR = BASE_DIR / "slides_html_v2"
SLIDE_IMAGES_DIR = BASE_DIR / "slide_images_v2"
AUDIO_DIR = BASE_DIR / "audio_narration_v2"
VIDEO_CLIPS_DIR = BASE_DIR / "video_clips_v2"
ASSETS_DIR = BASE_DIR / "assets"

PDF_SLIDES = BASE_DIR / "100_Beal_Street_Presentation_Slides_v2.pdf"
FINAL_VIDEO = BASE_DIR / "100_Beal_Street_History_and_Timeline_v2.mp4"
FINAL_VTT = BASE_DIR / "100_Beal_Street_History_and_Timeline_v2.vtt"

# Slide Data Definition (16 Slides) - Version 2
SLIDES_DATA = [
    {
        "num": 1,
        "title": "100 Beal Street: The 37-Year Journey",
        "subtitle": "From Naval Munitions Bunkers to State-Protected Senior Affordable Housing (1989–2026)",
        "is_title_slide": True,
        "points_left": [
            "<strong>Location:</strong> 100 Beal Street, Hingham, MA (School Tract II)",
            "<strong>Record Property Owner:</strong> Hingham Housing Authority (Independent State Entity)",
            "<strong>Proposed Development:</strong> 68-Unit Senior Affordable Rental Residence (Ages 62+)",
            "<strong>Selected Developer:</strong> Peabody Properties / AHSC (99-Year Ground Lease)",
            "<strong>Municipal Taxpayer Cost:</strong> Exactly $0 in Town Borrowing or Taxpayer Debt"
        ],
        "points_right": [
            "<strong>1989:</strong> Town deeds 15 acres with 30-year adolescent care reverter",
            "<strong>2001:</strong> WWII naval munitions bunkers demolished; 8-acre Lot 2 created",
            "<strong>2006:</strong> Town Meeting 2/3 vote mandates senior affordable housing",
            "<strong>2019:</strong> Select Board 3–0 litigation vote; State DHCD statutory transfer block",
            "<strong>2021:</strong> Housing Authority votes 4–0 to permanently retain land for housing",
            "<strong>2026:</strong> Project actively advancing toward permitting and title resolution"
        ],
        "script": "Welcome to the definitive history of 100 Beal Street in Hingham, Massachusetts. Over the past thirty-seven years, this parcel of former Navy ammunition depot land has journeyed through military remediation, an unrecorded deed release, a Town Hall lawsuit vote, decisive state intervention, and an award-winning senior housing design. In this presentation, we walk through the exact documentary record, separating verified legal facts from persistent town rumors."
    },
    {
        "num": 2,
        "title": "April 1989: The Deed & The 30-Year Reverter",
        "subtitle": "Town Conveys 15.014 Acres of Surplus Military Land to HHA",
        "points_left": [
            "<strong>Execution Date:</strong> March 7, 1989 | <strong>Recording Date:</strong> April 21, 1989",
            "<strong>Registry Citation:</strong> Plymouth County Registry of Deeds, Book 09097, Page 158 (Doc #29758)",
            "<strong>Grantor:</strong> Inhabitants of the Town of Hingham",
            "<strong>Grantee:</strong> Hingham Housing Authority",
            "<strong>Stated Consideration:</strong> $45,751 for 15.014-Acre School Tract II"
        ],
        "points_right": [
            "<strong>Specific Use Restriction:</strong> Dedicated solely for adolescent residential facility",
            "<strong>Full Property Scope:</strong> Restriction applied to ALL 15.014 acres of School Tract II",
            "<strong>Right of Re-Entry:</strong> Town retained right to enter if youth use ceased",
            "<strong>The 30-Year Limitation Clause (Page 160):</strong> Deed expressly dictates re-entry terminates after thirty years pursuant to M.G.L. c. 184A, § 3",
            "<strong>Expiration Deadline:</strong> March 7, 2019 (Exactly 30 calendar years)"
        ],
        "script": "Our story begins on April 21st, 1989. The Town of Hingham conveyed a fifteen-acre parcel of surplus Navy depot land known as School Tract II to the independent Hingham Housing Authority for forty-five thousand seven hundred fifty-one dollars. The deed carried a specific restriction: the land was to be used for a residential educational facility for troubled adolescents. Critically, page one hundred sixty stated that if that youth use ever ceased, the Town retained a right of re-entry. However, the deed explicitly dictated that this right of re-entry terminated thirty years from the date of the deed."
    },
    {
        "num": 3,
        "title": "1990 to Present: Continuous Public Service",
        "subtitle": "The 12-Bed Adolescent Facility Operates Without Interruption",
        "points_left": [
            "<strong>Facility Footprint:</strong> 12-bed group home constructed on dedicated 2.0-acre parcel fronting Beal Street",
            "<strong>Funding Program:</strong> Commonwealth Chapter 689 specialized public housing funds",
            "<strong>Operational Oversight:</strong> State youth services contract and licensed child care provider",
            "<strong>Continuous Public Service:</strong> Over 35 consecutive years of continuous operation"
        ],
        "points_right": [
            "<strong>Legal Standard:</strong> Re-entry required cessation of adolescent residential use",
            "<strong>Zero Default:</strong> Facility never ceased operations or abandoned its mission",
            "<strong>State Encumbrance:</strong> Chapter 689 funding attached permanent state public housing covenants",
            "<strong>Unclouded Title on Lot 1:</strong> Active youth home remains undisturbed on its 2-acre lot"
        ],
        "script": "Shortly after the conveyance, a twelve-bed group home was constructed on a dedicated two-acre corner of the parcel along Beal Street, funded through the Commonwealth's Chapter 689 specialized housing program. For over thirty-five years, this facility has operated continuously under active state contracts caring for vulnerable youth. Because the facility never ceased operations and was never abandoned, the Town never had legal grounds to trigger a default or claim a re-entry during the entire thirty-year statutory window."
    },
    {
        "num": 4,
        "title": "June 2001: Demolition, Remediation & Division",
        "subtitle": "WWII Munitions Bunkers Cleared; 8-Acre Surplus Plateau Created",
        "points_left": [
            "<strong>Naval History:</strong> Interior 13 acres held abandoned WWII ammunition bunkers and berms",
            "<strong>Environmental Cleanup:</strong> Town funded demolition of structures and asbestos/soil remediation",
            "<strong>Cooperative Agreement:</strong> Town and HHA execute administrative Memorandum of Understanding",
            "<strong>Boundary Survey:</strong> Gale Associates prepares formal division survey"
        ],
        "points_right": [
            "<strong>Recorded Instrument:</strong> Plan 100 of 2001 (Plymouth Plan Book 44, Page 412)",
            "<strong>Lot 1 (2.000 Acres):</strong> Active adolescent group home with dedicated Beal Street frontage",
            "<strong>Lot 2 (8.020 Acres):</strong> Remediated, buildable upland plateau with direct Beal Street access",
            "<strong>Milestone Result:</strong> Created clean, separate building lot for future public housing needs"
        ],
        "script": "Behind the adolescent home lay thirteen undeveloped acres containing abandoned World War II concrete ammunition bunkers and earth mounds from the old naval depot. In 2001, the Town funded the demolition of the bunkers and cleaned up hazardous materials. The Town and Housing Authority signed a Memorandum of Understanding and recorded Plan one hundred of 2001. This official survey divided the property into two parcels: Lot One, preserving the two-acre adolescent home, and Lot Two, an eight-acre remediated, buildable upland plateau with frontage on Beal Street."
    },
    {
        "num": 5,
        "title": "May 2006: Town Meeting Mandates Senior Housing",
        "subtitle": "Declared 2/3 Supermajority Authorizes Deed Release for Affordable Housing",
        "points_left": [
            "<strong>Legislative Assembly:</strong> Hingham Annual Town Meeting (May 1, 2006)",
            "<strong>Warrant Article 38:</strong> Sponsored to unlock Lot 2 surplus plateau for senior housing",
            "<strong>Voting Result:</strong> Declared two-thirds supermajority vote in favor by Hingham voters",
            "<strong>Certified Seal:</strong> Attested by Town Clerk Eileen A. McCracken"
        ],
        "points_right": [
            "<strong>Enacted Text:</strong> Authorized Selectmen to amend 1989 deed restriction to permit affordable housing",
            "<strong>Democratic Will:</strong> Clear democratic mandate dedicating parcel to senior community living",
            "<strong>The Administrative Breakdown:</strong> Town Hall never executed or recorded the amended deed release",
            "<strong>Decade-Long Oversight:</strong> Omission left 1989 deed restriction technically unreleased on record"
        ],
        "script": "Twenty years ago, the citizens of Hingham took decisive action. At the May 2006 Annual Town Meeting, voters considered Warrant Article thirty-eight. By an overwhelming declared two-thirds supermajority, Town Meeting voted to authorize the Board of Selectmen to amend the 1989 deed restriction, explicitly adding affordable senior housing as an allowable use for the surplus plateau. This was a clear democratic mandate to build affordable homes for Hingham seniors. Yet in an extraordinary municipal oversight, Town Hall never actually drafted, executed, or recorded that authorized deed release at the Plymouth County Registry of Deeds."
    },
    {
        "num": 6,
        "title": "2017–2018: The Unexecuted Deed Resurfaces",
        "subtitle": "Beal Street Due Diligence Reveals the Unrecorded Release",
        "points_left": [
            "<strong>Title Rediscovery:</strong> Town Counsel Susan Murphy discovers 2006 deed release was never recorded",
            "<strong>Selectmen Meeting Jan 30, 2018:</strong> Selectman Karen Johnson details 2001 bunker remediation history",
            "<strong>Selectmen Meeting Feb 13, 2018:</strong> HHA Chair Bob Keys requests review of restrictions and covenants",
            "<strong>Town Position:</strong> Board of Selectmen argues 8 acres should belong to Town due to remediation funding"
        ],
        "points_right": [
            "<strong>Corporate Independence:</strong> Housing Authority is an independent public body under state law",
            "<strong>Statutory Mission:</strong> HHA holds property for affordable housing, not general municipal real estate",
            "<strong>Board Resistance:</strong> HHA commissioners vote against voluntary conveyance back to municipal hall",
            "<strong>Escalating Impasse:</strong> Board of Selectmen prepares legal strategy in executive session"
        ],
        "script": "For over a decade, the unrecorded deed release remained unnoticed. But between 2016 and 2017, during due diligence for adjacent parcels on Beal Street, Town Counsel Susan Murphy discovered that the 2006 deed release had never been recorded. Selectman Karen Johnson briefed the Board in public sessions on January 30th and February 13th, 2018, arguing that because the Town had funded the 2001 bunker demolition, the eight acres should belong to the Town. However, the Housing Authority Board declined to surrender the parcel, noting its complex title and statutory public housing mission."
    },
    {
        "num": 7,
        "title": "February 2019: The 30-Year Deadline & Lawsuit Vote",
        "subtitle": "Select Board Votes 3–0 to Sue Housing Authority Nine Days Before Deadline",
        "points_left": [
            "<strong>30-Year Expiration:</strong> March 7, 2019 (Exactly 30 years from March 7, 1989 execution)",
            "<strong>Legal Expiration Risk:</strong> Town Counsel advises right of re-entry extinguishes forever on Day 30",
            "<strong>Executive Session:</strong> February 26, 2019 at 6:45 PM (Nine days before statutory expiration)",
            "<strong>Public Reconvening:</strong> Board returns to open session at 7:00 PM (Chairman Paul Healey presiding)"
        ],
        "points_right": [
            "<strong>Formal Litigation Vote:</strong> Moved by Healey, seconded by Johnson, voted 3–0 unanimous",
            "<strong>Documented Mandate:</strong> 'To file litigation regarding enforcement of agreement as to 100 Beal Street'",
            "<strong>Core Objective:</strong> Force HHA to deed 100 Beal Street back to Town Hall before reverter lapsed",
            "<strong>Municipal Standoff:</strong> Town Hall prepares formal litigation against its own Housing Authority"
        ],
        "script": "Town Counsel warned the Selectmen that under Massachusetts property law, if the thirty-year window closed without legal action, the Town's right of re-entry would expire forever. On February 26th, 2019—exactly nine days before the deadline—the Select Board met in Executive Session. Returning to Open Session at 7:00 PM, Chairman Paul Healey moved to file litigation against the Hingham Housing Authority to enforce the agreement on 100 Beal Street. Selectman Karen Johnson seconded, and the Board voted three to zero to authorize the lawsuit. Town Hall was prepared to take its own independent Housing Authority to court."
    },
    {
        "num": 8,
        "title": "June 2019: The Emergency Transfer Vote Under Duress",
        "subtitle": "Facing Litigation, Housing Authority Boards Vote to Surrender 19 Acres",
        "points_left": [
            "<strong>Meeting Date:</strong> June 5, 2019 (Special Meeting of HHA Board of Commissioners)",
            "<strong>Litigation Threat:</strong> Board confronted with pending Select Board court action",
            "<strong>The Motion:</strong> Board votes to approve transfer of ~19 acres off Beal Street to the Town",
            "<strong>Scope of Surrender:</strong> Contemplated relinquishing Lot 2 and associated Housing land"
        ],
        "points_right": [
            "<strong>The Illusion of Finality:</strong> Town Hall believed the property dispute had been settled",
            "<strong>Statutory Constraints:</strong> Local housing authorities cannot convey public housing property unilaterally",
            "<strong>State Financial Interest:</strong> Chapter 689 funding triggered mandatory Commonwealth supervision",
            "<strong>Imminent State Reaction:</strong> State regulatory authorities intervene to safeguard the asset"
        ],
        "script": "Confronted with the threat of an imminent lawsuit from Town Hall, the Hingham Housing Authority Board of Commissioners held an emergency special meeting on June 5th, 2019. Under intense legal pressure, the commissioners voted to approve a motion agreeing to transfer approximately nineteen acres of Housing Authority property off Beal Street back to municipal control. To outside observers, it appeared Town Hall had won the standoff and that the land was no longer under Housing Authority control. But an unexpected legal force was about to intervene."
    },
    {
        "num": 9,
        "title": "Summer 2019: The State Steps In",
        "subtitle": "Massachusetts DHCD Enforces Statutory Protections on Public Housing Land",
        "points_left": [
            "<strong>Governing Authority:</strong> Massachusetts General Laws Chapter 121B (Housing & Urban Renewal)",
            "<strong>Legal Status:</strong> Housing authorities are independent public bodies corporate, not Town departments",
            "<strong>Jurisdiction:</strong> Board of Selectmen has zero statutory authority to seize or command housing assets",
            "<strong>Public Purpose:</strong> Land dedicated to low-income housing cannot be alienated for general municipal use"
        ],
        "points_right": [
            "<strong>Supervisory Regulator:</strong> Massachusetts DHCD (Associate Director Amy Stitely)",
            "<strong>Statutory Bar (M.G.L. c. 121B, § 34):</strong> Public housing land cannot be transferred without written state approval",
            "<strong>Regulatory Letters:</strong> Issued April 19 & June 26, 2019 to HHA and Town Counsel",
            "<strong>State Decision:</strong> DHCD formally refuses to consent to municipal recapture"
        ],
        "script": "Town Hall's victory was short-lived. Under Massachusetts General Laws Chapter 121B, local housing authorities are independent public corporations created by the Legislature, not municipal departments. Furthermore, because state public housing funding had been utilized at the Beal Street site, state law strictly prohibits any housing authority from selling or transferring public housing land without prior written approval from the Commonwealth. Massachusetts DHCD Associate Director Amy Stitely issued formal warnings to both the Housing Authority and Town Counsel, stating plainly that the proposed transfer violated state law and public housing covenants, and would not be approved."
    },
    {
        "num": 10,
        "title": "July 2019: The Legal Lock on Title",
        "subtitle": "Commonwealth Records Notice of Statutory Transfer Restriction",
        "points_left": [
            "<strong>Recording Timestamp:</strong> July 18, 2019 at 1:44 PM",
            "<strong>Registry Citation:</strong> Plymouth County Registry of Deeds, Book 51379, Page 244 (Doc #55967)",
            "<strong>Grantor/Regulator:</strong> Commonwealth of Massachusetts DHCD",
            "<strong>Encumbered Real Estate:</strong> Assessor Map 58, Block 0, Lot 23 (100 Beal Street)"
        ],
        "points_right": [
            "<strong>Public Notice:</strong> Formally notifies title examiners and municipal attorneys of Chapter 121B, § 34 restriction",
            "<strong>Legal Nullity:</strong> Any deed executed without DHCD written approval is void as a matter of state law",
            "<strong>ALTA Survey:</strong> Explicitly recognized as Schedule B, Item 5 encumbrance on 2024 boundary survey",
            "<strong>Permanent Protection:</strong> Land permanently protected for public housing purposes"
        ],
        "script": "To ensure that Town Hall could not execute a transfer behind closed doors, the Commonwealth took decisive action on public land records. On July 18th, 2019, the state recorded a formal Notice of Statutory Transfer Restriction at the Plymouth County Registry of Deeds in Book fifty-one thousand three hundred seventy-nine, Page two hundred forty-four. Citing Chapter 121B, Section 34, this instrument legally encumbers 100 Beal Street. Any deed or transfer executed without the state's signature is void as a matter of law. The land was permanently locked for public affordable housing."
    },
    {
        "num": 11,
        "title": "September 2021: HHA Rescission & The Unresolved Title Cloud",
        "subtitle": "Ownership Reaffirmed, But 1989 Adolescent Restriction Remains on Record",
        "points_left": [
            "<strong>Assembly:</strong> September 7, 2021 Regular Meeting at 30 Thaxter Street",
            "<strong>Legal Concurrence:</strong> Backed by formal DHCD correspondence and specialized municipal counsel",
            "<strong>The Motion:</strong> Commissioner O’Meara moves to rescind the June 5, 2019 transfer motion",
            "<strong>Roll Call:</strong> Commissioners Suchecki, O'Meara, Lauter, Buhr vote 4–0 unanimous"
        ],
        "points_right": [
            "<strong>Ownership Retained:</strong> Fee title remained with HHA under state statutory protection",
            "<strong>The Continuing Cloud:</strong> The 2021 vote did NOT erase the 1989 deed restriction from Registry",
            "<strong>Missing Release:</strong> Town Hall never recorded the 2006 deed release on the public records",
            "<strong>2024 ALTA Survey Note 3:</strong> Kellem & Kellem / Control Point explicitly states: <em>'Need release or change of this restriction from the Town of Hingham'</em>"
        ],
        "script": "Backed by state regulatory authority and legal counsel, the Hingham Housing Authority Board reconvened on September 7th, 2021, voting four to zero to officially rescind its 2019 transfer motion. This confirmed that fee ownership of the land remained with the Housing Authority under state statutory protection. However, keeping ownership did not erase the 1989 deed restriction from public land records. The original restriction requiring the land to be used for adolescent care still technically encumbered the parcel because Town Hall never recorded the 2006 deed release. In fact, the official 2024 ALTA Title Survey specifically noted that the project still needs a formal release or change of this restriction from the Town of Hingham."
    },
    {
        "num": 12,
        "title": "December 2024: Verified Environmental Stewardship",
        "subtitle": "Conservation Commission Records MassDEP ORAD Protecting Tucker's Swamp",
        "points_left": [
            "<strong>MassDEP Docket:</strong> MassDEP File No. 034-1509",
            "<strong>Hearing:</strong> November 4, 2024 before Hingham Conservation Commission",
            "<strong>Roll Call:</strong> Passed 5–0 unanimous (Nielsen, Mosher, Roby, Villanova, Freeman)",
            "<strong>Recorded Instrument:</strong> Plymouth Registry Book 59527, Page 273 (Doc #78968, Dec 10, 2024)"
        ],
        "points_right": [
            "<strong>155+ Delineated Flags:</strong> Certified boundary survey by Lucas Environmental, LLC",
            "<strong>Protected Resources:</strong> 3 Bordering Vegetated Wetlands, 2 Isolated Wetlands, vernal pool",
            "<strong>ACEC Buffer Protection:</strong> Safeguards Tucker's Swamp and Weymouth Back River watershed",
            "<strong>Verified Plateau:</strong> Confirms Lot B contains expansive, high-and-dry buildable upland"
        ],
        "script": "Before proceeding with architectural designs, the Housing Authority conducted rigorous environmental due diligence. Lucas Environmental delineated 155 wetland flags around Tucker's Swamp and the Weymouth Back River Area of Critical Environmental Concern. On November 4th, 2024, the Hingham Conservation Commission voted unanimously, five to zero, to approve an Order of Resource Area Delineation, recorded at the Registry in Book fifty-nine thousand five hundred twenty-seven, Page two hundred seventy-three. This binding environmental order confirmed that the development plateau on Lot B is high, dry, and completely outside sensitive wetland resource areas, safeguarding our natural waterways."
    },
    {
        "num": 13,
        "title": "August 2025: Peabody Award (Conditional Ground Lease)",
        "subtitle": "68 Senior Units Under a 99-Year Ground Lease Contingent on Title Resolution",
        "points_left": [
            "<strong>Procurement Package:</strong> 155-Page RFP issued April 16, 2025 under M.G.L. c. 30B / c. 121B",
            "<strong>Award Meeting:</strong> August 12, 2025 HHA meeting; passed 4–0 unanimous roll call",
            "<strong>Designated Developer:</strong> Peabody Properties / Affordable Housing Services Corp. (AHSC)",
            "<strong>Target Demographic:</strong> 68 Rental Apartments for Seniors 62 and older"
        ],
        "points_right": [
            "<strong>99-Year Ground Lease:</strong> Land fee ownership stays permanently with Hingham Housing Authority",
            "<strong>Upfront Consideration:</strong> Developer pays $500,000 upfront lease fee to Housing Authority",
            "<strong>Contingent Agreement:</strong> Ground lease execution depends on state approvals and title resolution",
            "<strong>Taxpayer Obligation:</strong> Exactly $0 in municipal borrowing or Town general fund debt"
        ],
        "script": "In April 2025, the Housing Authority issued a comprehensive 155-page Request for Proposals under state procurement laws. On August 12th, 2025, the Housing Authority Board voted unanimously, four to zero, to award the development to Peabody Properties and Affordable Housing Services Corporation to build sixty-eight affordable apartments for seniors aged sixty-two and older under a ninety-nine-year ground lease. Under this arrangement, the Housing Authority retains permanent land ownership, receives a five hundred thousand dollar upfront fee, and taxpayers bear zero debt. However, final execution of the ground lease remains contingent upon obtaining state regulatory approvals and formally clearing the outstanding deed restriction through municipal agreement or the Chapter 40B permitting process."
    },
    {
        "num": 14,
        "title": "Architectural Vision: Modest, Sustainable & Senior-Focused",
        "subtitle": "Universal Design, Internal Courtyard, and Low-Impact Civil Engineering",
        "has_image": True,
        "image_path": "assets/weston_front.png",
        "points_left": [
            "<strong>Architectural Scale:</strong> Modest 3-story wood-frame design complementing Hingham neighborhoods",
            "<strong>Universal Accessibility:</strong> 100% single-floor barrier-free living, wide corridors, dual elevators",
            "<strong>Community Amenities:</strong> Multi-purpose hall, wellness exam room, outdoor walking paths, gardens",
            "<strong>Environmental Buffers:</strong> 50-foot undisturbed natural vegetative tree buffer to all abutters",
            "<strong>Stormwater Innovation:</strong> Advanced bioretention swales filtering 100% of rainwater on-site"
        ],
        "points_right": [],
        "script": "The architectural design, created by Weston and Sampson, reflects thoughtful community integration. Rather than an institutional complex, the development features a modest three-story wood-frame building that complements Hingham's residential character. All sixty-eight units are designed with universal accessibility, wide corridors, and step-free access for aging in place. The site plan incorporates a protected central courtyard, community gardens, walking paths, and cutting-edge bioretention stormwater basins that filter rainwater on-site, preserving fifty feet of natural vegetative tree buffers between the residence and adjacent neighborhoods."
    },
    {
        "num": 15,
        "title": "Clearing Up the Town Rumor: CAL vs. 100 Beal Street",
        "subtitle": "The Defeated Project Was Bare Cove Park CAL; 100 Beal Street Was Never on the Ballot",
        "is_comparison": True,
        "comparison_data": [
            ("Feature / Question", "100 Beal Street Senior Affordable Housing", "Bare Cove Park Center for Active Living (CAL)"),
            ("Project Nature", "68-Unit Residential Housing for Seniors 62+", "Daytime Municipal Senior Activities Facility"),
            ("Land Ownership", "Hingham Housing Authority (Independent State Entity)", "Inhabitants of the Town of Hingham (Municipal Park)"),
            ("Project Location", "100 Beal Street (Lot B Upland Plateau)", "Bare Cove Park Drive (Inside Bare Cove Park boundary)"),
            ("Cost to Taxpayers", "$0 Town Borrowing / $0 Municipal Debt", "$29,930,000 Municipal Debt Exclusion Borrowing"),
            ("Town Meeting Action", "Never voted down or rejected at Town Meeting", "Defeated at Town Meeting on April 27, 2026 (Art. 12)"),
            ("Current Status", "ACTIVE: Advancing toward 40B permitting & title agreement", "DEFEATED: Stalled due to failed 2/3 debt borrowing vote")
        ],
        "script": "This brings us to the single biggest misconception in town: why do so many residents believe Town Meeting killed the senior housing project? The project defeated on April 27th, 2026, was NOT 100 Beal Street. It was the Center for Active Living, or CAL—a separate twenty-nine-point-nine million dollar municipal daytime senior center that the Select Board proposed building inside Bare Cove Park. That project required Town Meeting to approve thirty million dollars in taxpayer borrowing, which failed to achieve the necessary two-thirds debt supermajority. Because both projects involved seniors and both bordered Tucker's Swamp, the community blurred them together. 100 Beal Street requires zero Town debt and was never voted down."
    },
    {
        "num": 16,
        "title": "Conclusion & The Path Forward: Resolving the Final Hurdle",
        "subtitle": "37 Years of History Moving Toward Permitting and Municipal Resolution",
        "points_left": [
            "<strong>37-Year Evolution:</strong> Naval Depot → Adolescent Care → Bunker Cleanup → Senior Housing",
            "<strong>Secure Ownership:</strong> Land remains with Housing Authority under state statutory protection",
            "<strong>Environmental Approval:</strong> 155+ wetland flags stamped and protected under recorded MassDEP ORAD"
        ],
        "points_right": [
            "<strong>The Final Hurdle:</strong> Formally clearing the historic 1989 deed restriction on title",
            "<strong>Dual Pathways:</strong> Select Board execution of 2006 authorized release OR Chapter 40B override",
            "<strong>Community Result:</strong> 68 permanently affordable homes for seniors with $0 in municipal debt"
        ],
        "script": "The thirty-seven-year history of 100 Beal Street is a story of community evolution—from a World War II ammunition depot to an adolescent care home, through hazardous bunker cleanup, and toward urgently needed senior affordable housing. Today, the Housing Authority holds fee title under state statutory protection, and environmental regulators have confirmed the buildable plateau protects Tucker's Swamp. The final chapter involves resolving the historic deed restriction with the Town—either by executing the release Town Meeting authorized in 2006 or through the Comprehensive Permit process. As this sixty-eight-unit senior residence advances, it represents a path to fulfill a twenty-year community promise without costing Hingham taxpayers a single dollar in municipal debt."
    }
]

def generate_slides_html():
    """Generate individual HTML slide files with pixel-perfect 16:9 1080p styling."""
    SLIDES_HTML_DIR.mkdir(parents=True, exist_ok=True)
    
    css_content = """
@page {
    size: 1920px 1080px;
    margin: 0;
}
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background: #ffffff;
    -webkit-font-smoothing: antialiased;
}
.slide {
    width: 1920px;
    height: 1080px;
    page-break-after: always;
    position: relative;
    overflow: hidden;
    background: #ffffff;
    display: flex;
    flex-direction: column;
    padding: 60px 80px 50px 80px;
}
.slide.title-slide {
    background: linear-gradient(135deg, #0B2265 0%, #06153d 100%);
    color: #ffffff;
    justify-content: center;
    padding: 80px 100px;
}
.top-accent-bar {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 12px;
    background: linear-gradient(90deg, #9E1B32 0%, #D97706 100%);
}
.slide-badge {
    position: absolute;
    top: 40px;
    right: 80px;
    background: #0B2265;
    color: #ffffff;
    font-size: 18px;
    font-weight: 700;
    padding: 8px 20px;
    border-radius: 20px;
    letter-spacing: 1px;
}
.slide-header {
    margin-bottom: 35px;
}
.slide-header h1 {
    font-size: 40px;
    font-weight: 800;
    color: #0B2265;
    line-height: 1.2;
}
.slide.title-slide .slide-header h1 {
    font-size: 56px;
    color: #ffffff;
    margin-bottom: 12px;
}
.slide-header h2 {
    font-size: 24px;
    font-weight: 600;
    color: #9E1B32;
    margin-top: 8px;
}
.slide.title-slide .slide-header h2 {
    font-size: 28px;
    color: #FBBF24;
}
.content-grid {
    display: flex;
    gap: 40px;
    flex: 1;
}
.card {
    flex: 1;
    background: #F8FAFC;
    border: 2px solid #E2E8F0;
    border-radius: 16px;
    padding: 28px 32px;
    display: block;
}
.slide.title-slide .card {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(251, 191, 36, 0.4);
    color: #ffffff;
}
.card h3 {
    font-size: 24px;
    font-weight: 700;
    color: #0B2265;
    margin-bottom: 18px;
    padding-bottom: 10px;
    border-bottom: 2px solid #CBD5E1;
}
.slide.title-slide .card h3 {
    color: #FBBF24;
    border-bottom: 1px solid rgba(251, 191, 36, 0.4);
}
.card ul {
    list-style: none;
    display: block;
    margin: 0;
    padding: 0;
}
.card li {
    font-size: 19px;
    line-height: 1.45;
    color: #334155;
    position: relative;
    padding-left: 28px;
    margin-bottom: 14px;
}
.card li:last-child {
    margin-bottom: 0;
}
.slide.title-slide .card li {
    color: #E2E8F0;
}
.card li::before {
    content: "■";
    position: absolute;
    left: 0;
    color: #9E1B32;
    font-size: 16px;
    top: -1px;
}
.slide.title-slide .card li::before {
    color: #FBBF24;
}
.card strong {
    color: #0F172A;
}
.slide.title-slide .card strong {
    color: #ffffff;
}
.comparison-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
    background: #ffffff;
    border-radius: 12px;
    overflow: hidden;
}
.comparison-table th, .comparison-table td {
    padding: 16px 20px;
    text-align: left;
    border-bottom: 1px solid #E2E8F0;
    font-size: 18px;
}
.comparison-table th {
    background: #0B2265;
    color: #ffffff;
    font-size: 20px;
    font-weight: 700;
}
.comparison-table th:first-child {
    width: 25%;
}
.comparison-table tr:nth-child(even) td {
    background: #F8FAFC;
}
.comparison-table td:nth-child(2) {
    color: #065F46;
    font-weight: 600;
    background: #ECFDF5;
}
.comparison-table td:nth-child(3) {
    color: #991B1B;
    font-weight: 600;
    background: #FEF2F2;
}
.image-layout {
    display: flex;
    gap: 40px;
    flex: 1;
}
.image-col {
    flex: 1.2;
    border-radius: 16px;
    overflow: hidden;
    border: 2px solid #CBD5E1;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #F1F5F9;
}
.image-col img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.slide-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 25px;
    padding-top: 15px;
    border-top: 1px solid #E2E8F0;
    font-size: 15px;
    color: #64748B;
    font-weight: 500;
}
.slide.title-slide .slide-footer {
    border-top: 1px solid rgba(255, 255, 255, 0.2);
    color: #94A3B8;
}
"""
    
    master_html_slides = []
    
    for slide in SLIDES_DATA:
        num = slide["num"]
        title = slide["title"]
        subtitle = slide["subtitle"]
        is_title = slide.get("is_title_slide", False)
        
        slide_class = "slide title-slide" if is_title else "slide"
        badge_html = "" if is_title else f'<div class="slide-badge">SLIDE {num:02d} OF 16</div>'
        
        if slide.get("is_comparison"):
            # Table slide
            rows_html = ""
            for idx, (feat, beal, cal) in enumerate(slide["comparison_data"]):
                if idx == 0:
                    rows_html += f"<tr><th>{feat}</th><th>{beal}</th><th>{cal}</th></tr>"
                else:
                    rows_html += f"<tr><td><strong>{feat}</strong></td><td>{beal}</td><td>{cal}</td></tr>"
            content_html = f"""
            <table class="comparison-table">
                {rows_html}
            </table>
            """
        elif slide.get("has_image"):
            # Image + single card layout
            img_rel = slide["image_path"]
            img_abs = str((BASE_DIR / img_rel).resolve())
            left_li = "".join([f"<li>{p}</li>" for p in slide["points_left"]])
            content_html = f"""
            <div class="image-layout">
                <div class="image-col">
                    <img src="file://{img_abs}" alt="Presentation Graphic">
                </div>
                <div class="card" style="flex: 1;">
                    <h3>Project Specifications & Universal Living</h3>
                    <ul>
                        {left_li}
                    </ul>
                </div>
            </div>
            """
        else:
            # 2-Column cards layout
            left_li = "".join([f"<li>{p}</li>" for p in slide["points_left"]])
            right_li = "".join([f"<li>{p}</li>" for p in slide["points_right"]])
            
            left_title = "Historical Context & Authority" if not is_title else "Executive Summary"
            right_title = "Documented Legal Findings" if not is_title else "Milestone Chronology"
            
            content_html = f"""
            <div class="content-grid">
                <div class="card">
                    <h3>{left_title}</h3>
                    <ul>
                        {left_li}
                    </ul>
                </div>
                <div class="card">
                    <h3>{right_title}</h3>
                    <ul>
                        {right_li}
                    </ul>
                </div>
            </div>
            """
            
        footer_html = f"""
        <div class="slide-footer">
            <span>100 Beal Street Senior Affordable Housing • Historical Presentation & Legal Analysis</span>
            <span>Town of Hingham, Massachusetts • Plymouth County</span>
            <span>Slide {num} of 16</span>
        </div>
        """
        
        slide_html = f"""
        <div class="{slide_class}">
            <div class="top-accent-bar"></div>
            {badge_html}
            <div class="slide-header">
                <h1>{title}</h1>
                <h2>{subtitle}</h2>
            </div>
            {content_html}
            {footer_html}
        </div>
        """
        master_html_slides.append(slide_html)
        
        # Save individual slide HTML for debug
        indiv_file = SLIDES_HTML_DIR / f"slide_{num:02d}.html"
        with open(indiv_file, "w", encoding="utf-8") as f:
            f.write(f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{css_content}</style></head><body>{slide_html}</body></html>")

    # Combine all into master HTML for WeasyPrint PDF compilation
    master_html_file = BASE_DIR / "master_slides_v2.html"
    with open(master_html_file, "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>100 Beal Street Senior Affordable Housing - Presentation Deck v2</title>
    <style>
        {css_content}
    </style>
</head>
<body>
    {''.join(master_html_slides)}
</body>
</html>
""")
    print(f"[OK] Master slides HTML generated at: {master_html_file}")
    return master_html_file

def compile_slides_pdf(master_html_path):
    """Compile master HTML slides into a 16-page 1080p PDF using WeasyPrint."""
    print(f"[...] Compiling PDF slides via WeasyPrint to: {PDF_SLIDES}")
    cmd = ["/opt/homebrew/bin/weasyprint", str(master_html_path), str(PDF_SLIDES)]
    subprocess.run(cmd, check=True)
    print(f"[OK] PDF slides successfully compiled: {PDF_SLIDES} ({PDF_SLIDES.stat().st_size:,} bytes)")

def extract_slide_images():
    """Extract each PDF page as an ultra-crisp 1920x1080 PNG image using pdftoppm."""
    SLIDE_IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[...] Extracting 1080p slide PNGs to: {SLIDE_IMAGES_DIR}")
    
    # pdftoppm extracts all pages
    prefix = str(SLIDE_IMAGES_DIR / "page")
    cmd = ["pdftoppm", "-png", "-r", "150", str(PDF_SLIDES), prefix]
    subprocess.run(cmd, check=True)
    
    # Rename generated page-01.png etc to slide_01.png
    extracted_files = sorted(SLIDE_IMAGES_DIR.glob("page-*.png"))
    for idx, f in enumerate(extracted_files, start=1):
        target = SLIDE_IMAGES_DIR / f"slide_{idx:02d}.png"
        shutil.move(str(f), str(target))
        
    print(f"[OK] Extracted {len(extracted_files)} slide PNG images.")

def get_existing_audio_durations():
    """Check if all 16 slide audio files already exist and return their durations."""
    durations = {}
    for slide in SLIDES_DATA:
        num = slide["num"]
        audio_file = AUDIO_DIR / f"slide_{num:02d}.wav"
        if not audio_file.exists():
            return None
        dur = get_audio_duration(audio_file)
        if dur <= 0:
            return None
        durations[num] = dur
    return durations

def synthesize_narration_audio(voice="Samantha", rate=165, force_tts=False):
    """Synthesize high-clarity voice narration for each slide using macOS say."""
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    
    if not force_tts:
        existing = get_existing_audio_durations()
        if existing:
            print(f"[INFO] Complete set of 16 slide audio files detected in {AUDIO_DIR}.")
            print("[INFO] Preserving existing/cloned narration files. (Use --force-tts to overwrite).")
            return existing

    print(f"[...] Synthesizing narration audio files using macOS speech ({voice} at {rate} WPM)...")
    durations = {}
    
    for slide in SLIDES_DATA:
        num = slide["num"]
        script = slide["script"]
        aiff_file = AUDIO_DIR / f"slide_{num:02d}.aiff"
        wav_file = AUDIO_DIR / f"slide_{num:02d}.wav"
        
        # Synthesize via say
        say_cmd = ["say", "-v", voice, "-r", str(rate), "-o", str(aiff_file), script]
        subprocess.run(say_cmd, check=True)
        
        # Convert AIFF to standard 48kHz stereo WAV with subtle 0.25s silence padding
        ffmpeg_cmd = [
            "ffmpeg", "-y", "-i", str(aiff_file),
            "-af", "apad=pad_dur=0.35,volume=1.05",
            "-ar", "48000", "-ac", "2",
            str(wav_file)
        ]
        subprocess.run(ffmpeg_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        aiff_file.unlink(missing_ok=True)
        
        duration = get_audio_duration(wav_file)
        durations[num] = duration
        print(f"  - Slide {num:02d} Audio: {duration:.2f}s | {wav_file.name}")
        
    print(f"[OK] Synthesized all {len(durations)} audio narration tracks.")
    return durations

def get_audio_duration(audio_path):
    """Get precise duration of an audio file in seconds via ffprobe."""
    cmd = [
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=noprint_wrappers=1:nokey=1",
        str(audio_path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return float(res.stdout.strip())

def generate_video_clips(durations):
    """Generate 1080p MP4 video clip for each slide matching exact audio duration."""
    VIDEO_CLIPS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[...] Rendering individual 1080p video clips to: {VIDEO_CLIPS_DIR}")
    
    clip_paths = []
    for slide in SLIDES_DATA:
        num = slide["num"]
        duration = durations[num]
        slide_img = SLIDE_IMAGES_DIR / f"slide_{num:02d}.png"
        slide_audio = AUDIO_DIR / f"slide_{num:02d}.wav"
        clip_mp4 = VIDEO_CLIPS_DIR / f"clip_{num:02d}.mp4"
        
        # Create MP4 clip looping image over exact audio duration
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-i", str(slide_img),
            "-i", str(slide_audio),
            "-c:v", "libx264", "-tune", "stillimage",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k",
            "-t", str(duration),
            "-shortest",
            str(clip_mp4)
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        clip_paths.append(clip_mp4)
        print(f"  - Rendered Clip {num:02d}: {duration:.2f}s | {clip_mp4.name}")
        
    print(f"[OK] Rendered {len(clip_paths)} video clips.")
    return clip_paths

def concatenate_video_clips(clip_paths):
    """Concatenate all slide video clips into the final master presentation MP4."""
    print(f"[...] Concatenating {len(clip_paths)} clips into master video...")
    concat_list_file = BASE_DIR / "concat_list_v2.txt"
    
    with open(concat_list_file, "w", encoding="utf-8") as f:
        for p in clip_paths:
            f.write(f"file '{p.resolve()}'\n")
            
    vtt_path = generate_vtt()
    
    # Concatenate clips and mux WebVTT subtitle track
    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_list_file),
        "-i", str(vtt_path),
        "-c:v", "copy",
        "-c:a", "copy",
        "-c:s", "mov_text",
        "-metadata:s:s:0", "language=eng",
        "-metadata:s:s:0", "title=English Narration",
        str(FINAL_VIDEO)
    ]
    subprocess.run(concat_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    concat_list_file.unlink(missing_ok=True)
    
    final_size = FINAL_VIDEO.stat().st_size
    final_duration = get_audio_duration(FINAL_VIDEO)
    print(f"[OK] Master Video Successfully Generated!")
    print(f"  - Video File: {FINAL_VIDEO}")
    print(f"  - File Size: {final_size:,} bytes ({final_size / (1024*1024):.1f} MB)")
    print(f"  - Duration: {final_duration:.2f} seconds ({final_duration / 60:.2f} minutes)")

def format_timestamp_vtt(seconds):
    """Format seconds into HH:MM:SS.mmm for WebVTT."""
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    mils = int((seconds - int(seconds)) * 1000)
    return f"{hrs:02d}:{mins:02d}:{secs:02d}.{mils:03d}"

def generate_vtt():
    """Generate timed WebVTT closed captions for the presentation video."""
    print(f"[...] Generating WebVTT subtitle track: {FINAL_VTT}")
    
    current_time = 0.0
    vtt_lines = ["WEBVTT", ""]
    
    for slide in SLIDES_DATA:
        num = slide["num"]
        wav_file = AUDIO_DIR / f"slide_{num:02d}.wav"
        duration = get_audio_duration(wav_file)
        start_time = current_time
        end_time = current_time + duration
        current_time = end_time
        
        start_str = format_timestamp_vtt(start_time)
        end_str = format_timestamp_vtt(end_time)
        
        vtt_lines.append(f"{num}")
        vtt_lines.append(f"{start_str} --> {end_str}")
        vtt_lines.append(f"[Slide {num}: {slide['title']}]")
        vtt_lines.append(slide["script"])
        vtt_lines.append("")
        
    with open(FINAL_VTT, "w", encoding="utf-8") as f:
        f.write("\n".join(vtt_lines))
        
    print(f"[OK] WebVTT subtitles generated: {FINAL_VTT}")
    return FINAL_VTT

def main():
    parser = argparse.ArgumentParser(description="Generate 100 Beal Street Video Presentation v2")
    parser.add_argument("--voice", default="Samantha", help="macOS speech voice name")
    parser.add_argument("--rate", type=int, default=165, help="Speech rate in words per minute")
    parser.add_argument("--keep-audio", action="store_true", help="Preserve existing/cloned narration files in audio_narration_v2/")
    parser.add_argument("--force-tts", action="store_true", help="Force re-synthesis of narration audio using macOS speech")
    parser.add_argument("--skip-slides", action="store_true", help="Skip regenerating slides HTML/PDF/PNG if they already exist")
    args = parser.parse_args()

    print("================================================================================")
    print("100 BEAL STREET PRESENTATION VIDEO PIPELINE (VERSION 2)")
    print("================================================================================")
    
    # Step 1: Slides Generation
    if not args.skip_slides or not PDF_SLIDES.exists():
        master_html = generate_slides_html()
        compile_slides_pdf(master_html)
        extract_slide_images()
    else:
        print(f"[INFO] Skipping slide regeneration (--skip-slides); using existing slides.")
        
    # Step 2: Audio Synthesis / Detection
    durations = synthesize_narration_audio(
        voice=args.voice,
        rate=args.rate,
        force_tts=args.force_tts
    )
    
    # Step 3: Render Clips & Concatenate
    clip_paths = generate_video_clips(durations)
    concatenate_video_clips(clip_paths)
    
    print("\n[SUCCESS] Pipeline completed successfully!")
    print(f"- Final Video: {FINAL_VIDEO}")
    print(f"- PDF Slides: {PDF_SLIDES}")
    print(f"- Subtitles:  {FINAL_VTT}")

if __name__ == "__main__":
    main()
