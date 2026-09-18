#!/usr/bin/env python3
"""
Complete Video Generation & Synthesis Pipeline for 100 Beal Street
Project: 100 Beal Street Senior Affordable Housing (Hingham, MA)
Identifier: generate_presentation_video_v1.py
Constraint: Zero forbidden terms. File versioning v1.
"""

import os
import sys
import subprocess
import shutil
import json
from pathlib import Path

BASE_DIR = Path("/Volumes/BLK4TB/Housing Topics/Beal Street Senior Affordable Housing/agent_created_deliverables/video_presentation")
SLIDES_HTML_DIR = BASE_DIR / "slides_html"
SLIDE_IMAGES_DIR = BASE_DIR / "slide_images"
AUDIO_DIR = BASE_DIR / "audio_narration"
VIDEO_CLIPS_DIR = BASE_DIR / "video_clips"
ASSETS_DIR = BASE_DIR / "assets"

PDF_SLIDES = BASE_DIR / "100_Beal_Street_Presentation_Slides_v1.pdf"
FINAL_VIDEO = BASE_DIR / "100_Beal_Street_History_and_Timeline_v1.mp4"
FINAL_VTT = BASE_DIR / "100_Beal_Street_History_and_Timeline_v1.vtt"

# Slide Data Definition (16 Slides)
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
            "<strong>2026:</strong> Project fully active and permitted under long-term ground lease"
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
            "<strong>Unclouded Title:</strong> The Town never had lawful grounds to trigger re-entry during the 30-year window"
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
            "<strong>Decade-Long Oversight:</strong> Omission went unnoticed in municipal records for over ten years"
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
            "<strong>The Motion:</strong> Chair Healey moves to file litigation regarding enforcement of agreement at 100 Beal",
            "<strong>Second:</strong> Seconded by Selectman Karen Johnson",
            "<strong>Vote Tally:</strong> Passed 3–0 unanimous (Healey, Johnson, Power)",
            "<strong>Litigation Authorized:</strong> Town of Hingham authorizes formal lawsuit against Hingham Housing Authority"
        ],
        "script": "By February 2019, the situation reached a boiling point. The thirty-year calendar mark from the 1989 deed was set to expire on March 7th, 2019. Under Massachusetts law, if that date passed, any right of re-entry the Town held would vanish forever. On February 26th, exactly nine days before the deadline, the Select Board convened in Executive Session. Returning to Open Session, Selectman Karen Johnson seconded a motion by Chairman Paul Healey, and the Board voted three to zero to authorize formal litigation against their own Housing Authority to force them to deed the land back to the Town."
    },
    {
        "num": 8,
        "title": "June 2019: The Surrender Under Litigation Threat",
        "subtitle": "Housing Authority Initially Votes to Transfer 19 Acres to Town Hall",
        "points_left": [
            "<strong>Emergency Meeting:</strong> June 5, 2019 Special Meeting of HHA Board of Commissioners",
            "<strong>Severe Legal Pressure:</strong> Confronted by active 3–0 litigation vote from Board of Selectmen",
            "<strong>The Transfer Vote:</strong> HHA Board votes to approve transferring ~19 acres back to municipal control",
            "<strong>Scope of Motion:</strong> Surplus Lot 2 plateau and adjacent Town-associated parcel"
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
        "title": "September 2021: The Unanimous Rescission Vote",
        "subtitle": "Housing Authority Formally Cancels 2019 Transfer Motion",
        "points_left": [
            "<strong>Assembly:</strong> September 7, 2021 Regular Meeting at 30 Thaxter Street",
            "<strong>Legal Concurrence:</strong> Backed by formal DHCD correspondence and specialized municipal counsel",
            "<strong>The Motion:</strong> Commissioner O’Meara moves to rescind the June 5, 2019 transfer motion",
            "<strong>Second:</strong> Seconded by Commissioner Lauter"
        ],
        "points_right": [
            "<strong>Roll Call Vote:</strong> Commissioners Suchecki, O'Meara, Lauter, Buhr all vote AYE",
            "<strong>Tally:</strong> Unanimous 4–0 vote to rescind",
            "<strong>Official Minute Ruling:</strong> 'That Motion is now rescinded and the land shall remain in the ownership of the HHA'",
            "<strong>Final Conclusion:</strong> Brought an absolute, permanent end to Town Hall's recapture effort"
        ],
        "script": "Backed by state regulatory authority and legal counsel, the Hingham Housing Authority Board of Commissioners reconvened on September 7th, 2021, to settle the issue permanently. Commissioner O’Meara made a formal motion, seconded by Commissioner Lauter, to rescind the June 2019 transfer vote. The motion passed unanimously on a four to zero roll call vote. The official minutes declared unequivocally that the transfer was rescinded, and that the parcel would remain in the sole ownership of the Hingham Housing Authority to fulfill its mission of providing senior affordable housing."
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
        "title": "August 2025: Peabody Properties Awarded Project",
        "subtitle": "68 Senior Rental Apartments Under a 99-Year Ground Lease",
        "points_left": [
            "<strong>Procurement Package:</strong> 155-Page RFP issued April 16, 2025 under M.G.L. c. 30B",
            "<strong>Award Meeting:</strong> August 12, 2025 HHA meeting; passed 4–0 unanimous roll call",
            "<strong>Designated Developer:</strong> Peabody Properties / Affordable Housing Services Corp. (AHSC)",
            "<strong>Target Demographic:</strong> 68 Rental Apartments for Seniors 62 and older"
        ],
        "points_right": [
            "<strong>99-Year Ground Lease:</strong> Land fee ownership stays permanently with Hingham Housing Authority",
            "<strong>Upfront Consideration:</strong> Developer pays $500,000 upfront lease fee to Housing Authority",
            "<strong>Private/Tax-Credit Financing:</strong> 100% financed through private equity and affordable tax credits",
            "<strong>Taxpayer Obligation:</strong> Exactly $0 in municipal borrowing or Town general fund debt"
        ],
        "script": "In April 2025, the Housing Authority issued a comprehensive 155-page Request for Proposals under state procurement laws. On August 12th, 2025, following competitive evaluation, the Housing Authority Board voted unanimously, four to zero, to award the development to Peabody Properties and Affordable Housing Services Corporation. Under the agreement, Peabody will build a sixty-eight-unit rental community restricted to seniors aged sixty-two and older. The project utilizes a ninety-nine-year ground lease, meaning the town housing authority retains permanent land ownership, receives a five hundred thousand dollar upfront fee, and taxpayers bear zero debt."
    },
    {
        "num": 14,
        "title": "Architectural Vision: Modest, Sustainable & Senior-Focused",
        "subtitle": "Universal Design, Internal Courtyard, and Low-Impact Civil Engineering",
        "has_image": True,
        "image_path": "assets/weston_rendering.png",
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
        "subtitle": "The Defeated Project Was Bare Cove Park CAL; 100 Beal Street Is Fully Active",
        "is_comparison": True,
        "comparison_data": [
            ("Feature / Question", "100 Beal Street Senior Affordable Housing", "Bare Cove Park Center for Active Living (CAL)"),
            ("Project Nature", "68-Unit Residential Housing for Seniors 62+", "Daytime Municipal Senior Activities Facility"),
            ("Land Ownership", "Hingham Housing Authority (Independent State Entity)", "Inhabitants of the Town of Hingham (Municipal Park)"),
            ("Project Location", "100 Beal Street (Lot B Upland Plateau)", "Bare Cove Park Drive (Inside Bare Cove Park boundary)"),
            ("Cost to Taxpayers", "$0 Town Borrowing / $0 Municipal Debt", "$29,930,000 Municipal Debt Exclusion Borrowing"),
            ("Town Meeting Action", "Never voted down or rejected at Town Meeting", "Defeated at Town Meeting on April 27, 2026 (Art. 12)"),
            ("Vote Outcome", "Passed 2/3 Supermajority in 2006 (Art. 38)", "Failed 2/3 Debt Supermajority (510 Yes, 470 No / 52%)"),
            ("Current Status", "ACTIVE & PERMITTED (Advancing Under 99-Yr Lease)", "DEFEATED & Stalled Due to Failed Borrowing Vote")
        ],
        "script": "Now we must address the single biggest rumor in Hingham: the belief that Town Meeting voted down 100 Beal Street. This is completely false. On April 27th, 2026, Town Meeting debated Warrant Article twelve. That article proposed borrowing nearly thirty million dollars in municipal taxpayer debt to build the Center for Active Living—a daytime senior activities center inside Bare Cove Park. Under state finance law, municipal borrowing requires a strict two-thirds supermajority. The bond failed, receiving fifty-two percent. Because both projects involved seniors and both bordered Tucker's Swamp, rumors spread that the senior project died. In reality, 100 Beal Street was never on the ballot, costs taxpayers zero dollars, and is actively moving forward."
    },
    {
        "num": 16,
        "title": "The Horizon: Permitting, Groundbreaking & Legacy",
        "subtitle": "Comprehensive Permit, Financing Milestones, and Permanent Affordability",
        "points_left": [
            "<strong>August 2026:</strong> Land Disposition & Development Agreement review with Peabody",
            "<strong>Fall 2026–2027:</strong> Chapter 40B Comprehensive Permit review before Zoning Board of Appeals",
            "<strong>2027:</strong> Allocation of State/Federal Affordable Housing Tax Credits (EOHLC / MassHousing)",
            "<strong>2028:</strong> Scheduled groundbreaking on 68 units of senior affordable housing"
        ],
        "points_right": [
            "<strong>Age in Place with Dignity:</strong> Enables lifelong Hingham residents to remain in the community",
            "<strong>Local Preference:</strong> Housing preference established for eligible Hingham military veterans",
            "<strong>Permanent Public Covenants:</strong> Land remains under public housing authority title forever",
            "<strong>Fulfilling Democratic Will:</strong> Implements the vision voted by Hingham citizens twenty years ago"
        ],
        "script": "As of late 2026, 100 Beal Street is advancing through its final development phases. The Housing Authority is executing the formal Land Disposition Agreement with Peabody Properties. Permitting will proceed through a Chapter 40B Comprehensive Permit before the Zoning Board of Appeals, followed by state affordable housing tax credit financing. Construction will bring sixty-eight modern, dignified homes for Hingham's aging residents. Thirty-seven years after School Tract II was first deeded, this historic parcel will finally fulfill its democratic promise: offering Hingham seniors a permanent, affordable place to call home."
    }
]

def generate_slides_html():
    """Generate HTML/CSS for all 16 slides rendered into a multi-page presentation document."""
    SLIDES_HTML_DIR.mkdir(parents=True, exist_ok=True)
    html_file = SLIDES_HTML_DIR / "presentation_deck.html"
    
    html_parts = []
    html_parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>
@page {
    size: 1920px 1080px;
    margin: 0;
}
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
body {
    background-color: #0b1528;
    color: #1a202c;
    width: 1920px;
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
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
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
    display: block;
}
.card li:last-child {
    margin-bottom: 0;
}
.slide.title-slide .card li {
    color: #E2E8F0;
    font-size: 20px;
    line-height: 1.45;
    margin-bottom: 16px;
    padding-left: 28px;
}
.slide.title-slide .card li:last-child {
    margin-bottom: 0;
}
.card li::before {
    content: "•";
    position: absolute;
    left: 4px;
    top: -1px;
    color: #9E1B32;
    font-size: 26px;
    line-height: 1;
}
.slide.title-slide .card li::before {
    color: #FBBF24;
}
.card li strong {
    color: #0B2265;
}
.slide.title-slide .card li strong {
    color: #ffffff;
}

/* Image layout for Slide 14 */
.image-layout-grid {
    display: flex;
    gap: 36px;
    flex: 1;
}
.image-container {
    flex: 1.25;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #0B2265;
    border-radius: 16px;
    overflow: hidden;
    border: 3px solid #CBD5E1;
}
.image-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Comparison Table for Slide 15 */
.comparison-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
    background: #ffffff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0,0,0,0.06);
}
.comparison-table th {
    padding: 16px 20px;
    font-size: 20px;
    font-weight: 700;
    text-align: left;
}
.comparison-table th:nth-child(1) { width: 22%; background: #0B2265; color: #ffffff; }
.comparison-table th:nth-child(2) { width: 39%; background: #047857; color: #ffffff; text-align: center; }
.comparison-table th:nth-child(3) { width: 39%; background: #9E1B32; color: #ffffff; text-align: center; }

.comparison-table td {
    padding: 14px 20px;
    font-size: 18px;
    line-height: 1.4;
    border-bottom: 1px solid #E2E8F0;
    color: #1E293B;
}
.comparison-table td:nth-child(1) { font-weight: 600; background: #F8FAFC; color: #0B2265; }
.comparison-table td:nth-child(2) { background: #F0FDF4; font-weight: 600; text-align: center; }
.comparison-table td:nth-child(3) { background: #FEF2F2; font-weight: 600; text-align: center; }

.footer-bar {
    position: absolute;
    bottom: 25px;
    left: 80px;
    right: 80px;
    display: flex;
    justify-content: space-between;
    font-size: 14px;
    color: #64748B;
    border-top: 1px solid #E2E8F0;
    padding-top: 10px;
}
.slide.title-slide .footer-bar {
    border-top: 1px solid rgba(255,255,255,0.15);
    color: #94A3B8;
}
</style>
</head>
<body>
""")

    for data in SLIDES_DATA:
        is_title = data.get("is_title_slide", False)
        title_class = "slide title-slide" if is_title else "slide"
        
        html_parts.append(f'<div class="{title_class}">')
        html_parts.append('<div class="top-accent-bar"></div>')
        if not is_title:
            html_parts.append(f'<div class="slide-badge">SLIDE {data["num"]:02d} / 16</div>')
        
        html_parts.append('<div class="slide-header">')
        html_parts.append(f'<h1>{data["title"]}</h1>')
        html_parts.append(f'<h2>{data["subtitle"]}</h2>')
        html_parts.append('</div>')

        if data.get("is_comparison"):
            # Render Comparison Table
            html_parts.append('<table class="comparison-table">')
            for i, row in enumerate(data["comparison_data"]):
                if i == 0:
                    html_parts.append(f'<thead><tr><th>{row[0]}</th><th>{row[1]}</th><th>{row[2]}</th></tr></thead><tbody>')
                else:
                    html_parts.append(f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>')
            html_parts.append('</tbody></table>')
        elif data.get("has_image"):
            # Image + Card layout
            img_abs = (ASSETS_DIR / "weston_front.png").as_posix()
            html_parts.append('<div class="image-layout-grid">')
            html_parts.append(f'<div class="image-container"><img src="file://{img_abs}" alt="Weston & Sampson 68-Unit Senior Residence Architectural Rendering" /></div>')
            html_parts.append('<div class="card" style="flex: 1; padding: 24px 28px;">')
            html_parts.append('<h3>Senior Universal Design & Civil Engineering</h3>')
            html_parts.append('<ul>')
            for pt in data["points_left"]:
                html_parts.append(f'<li style="font-size: 18px; margin-bottom: 12px;">{pt}</li>')
            html_parts.append('</ul></div></div>')
        else:
            # Standard 2-column cards
            html_parts.append('<div class="content-grid">')
            
            # Left Card
            left_header = "Primary Historical Facts" if not is_title else "Project Overview & Scope"
            html_parts.append(f'<div class="card"><h3>{left_header}</h3><ul>')
            for pt in data["points_left"]:
                html_parts.append(f'<li>{pt}</li>')
            html_parts.append('</ul></div>')
            
            # Right Card
            right_header = "Documentary & Legal Impact" if not is_title else "Chronological Milestones"
            html_parts.append(f'<div class="card"><h3>{right_header}</h3><ul>')
            for pt in data["points_right"]:
                html_parts.append(f'<li>{pt}</li>')
            html_parts.append('</ul></div>')
            
            html_parts.append('</div>')

        # Footer
        html_parts.append('<div class="footer-bar">')
        html_parts.append('<span>100 Beal Street Senior Affordable Housing • Historical Briefing</span>')
        html_parts.append('<span>Hingham Housing Authority • 68 Senior Units • 99-Year Lease</span>')
        html_parts.append('</div>')

        html_parts.append('</div>\n')

    html_parts.append("</body></html>")

    full_html = "\n".join(html_parts)
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    print(f"[SUCCESS] Generated HTML presentation deck at: {html_file}")
    return html_file

def compile_pdf_and_images(html_file):
    """Compile HTML slides to PDF with WeasyPrint and extract 1920x1080 PNG images."""
    SLIDE_IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    
    print("\n[INFO] Compiling HTML slides to 1920x1080 PDF using WeasyPrint...")
    cmd_weasy = ["weasyprint", "-e", "utf-8", str(html_file), str(PDF_SLIDES)]
    subprocess.run(cmd_weasy, check=True)
    print(f"[SUCCESS] Compiled presentation PDF: {PDF_SLIDES}")

    print("\n[INFO] Extracting 1920x1080 PNG images for each slide using pdftoppm...")
    cmd_pdftoppm = ["pdftoppm", "-png", "-r", "96", str(PDF_SLIDES), str(SLIDE_IMAGES_DIR / "slide")]
    subprocess.run(cmd_pdftoppm, check=True)

    # Normalize image names to slide_01.png through slide_16.png
    for i in range(1, 17):
        # pdftoppm generates slide-1.png or slide-01.png
        src1 = SLIDE_IMAGES_DIR / f"slide-{i}.png"
        src2 = SLIDE_IMAGES_DIR / f"slide-{i:02d}.png"
        dst = SLIDE_IMAGES_DIR / f"slide_{i:02d}.png"
        
        if src1.exists():
            shutil.move(str(src1), str(dst))
        elif src2.exists():
            shutil.move(str(src2), str(dst))
        
        if dst.exists():
            print(f"  Slide {i:02d}/16: {dst.name}")
        else:
            raise FileNotFoundError(f"Missing slide image {dst}")

def get_existing_audio_durations():
    """Check if all 16 slide audio files exist and return their probed durations."""
    durations = {}
    for data in SLIDES_DATA:
        num = data["num"]
        out_wav = AUDIO_DIR / f"slide_{num:02d}.wav"
        if not out_wav.exists():
            return None
        dur_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(out_wav)]
        try:
            dur = float(subprocess.check_output(dur_cmd).strip())
            durations[num] = dur
        except Exception:
            return None
    return durations

def synthesize_narration_audio(voice_name="Samantha", rate=165, force=False):
    """Synthesize audio narration for all 16 slides or reuse existing/cloned audio."""
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    
    if not force:
        existing = get_existing_audio_durations()
        if existing is not None:
            print("\n[INFO] Complete set of 16 slide audio files detected in audio_narration/.")
            print("       Preserving existing/cloned narration files (pass --force-tts to re-synthesize).")
            for num, dur in existing.items():
                print(f"  Slide {num:02d}/16: {dur:5.2f} sec (existing audio preserved)")
            return existing

    print(f"\n[INFO] Synthesizing presentation audio narration via macOS speech (Voice: '{voice_name}', Rate: {rate} WPM)...")
    durations = {}
    for data in SLIDES_DATA:
        num = data["num"]
        script = data["script"]
        temp_aiff = AUDIO_DIR / f"temp_{num:02d}.aiff"
        out_wav = AUDIO_DIR / f"slide_{num:02d}.wav"
        
        # Synthesize via macOS say with high-clarity voice
        cmd_say = ["say", "-v", voice_name, "-r", str(rate), "-o", str(temp_aiff), script]
        subprocess.run(cmd_say, check=True)
        
        # Convert to standard 48kHz stereo WAV via ffmpeg
        cmd_ffmpeg = [
            "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
            "-i", str(temp_aiff),
            "-ar", "48000", "-ac", "2",
            str(out_wav)
        ]
        subprocess.run(cmd_ffmpeg, check=True)
        temp_aiff.unlink(missing_ok=True)

        # Probe exact audio duration
        dur_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(out_wav)]
        dur = float(subprocess.check_output(dur_cmd).strip())
        durations[num] = dur
        print(f"  Slide {num:02d}/16: {dur:5.2f} sec | '{script[:45]}...'")

    return durations

def render_video_clips(durations):
    """Render individual slide video clips with exact audio sync and 1.2s padding."""
    VIDEO_CLIPS_DIR.mkdir(parents=True, exist_ok=True)
    print("\n[INFO] Encoding individual 1080p slide video clips...")

    clip_paths = []
    total_presentation_time = 0.0

    for num in range(1, 17):
        img_path = SLIDE_IMAGES_DIR / f"slide_{num:02d}.png"
        audio_path = AUDIO_DIR / f"slide_{num:02d}.wav"
        clip_out = VIDEO_CLIPS_DIR / f"clip_{num:02d}.mp4"
        
        audio_dur = durations[num]
        clip_dur = audio_dur + 1.2 # 1.2s padding for clean transition
        total_presentation_time += clip_dur

        # Create video clip with padded audio and loop slide image
        cmd_clip = [
            "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
            "-loop", "1", "-framerate", "30", "-t", str(clip_dur),
            "-i", str(img_path),
            "-i", str(audio_path),
            "-filter_complex", f"[1:a]apad=whole_dur={clip_dur}[aout]",
            "-map", "0:v", "-map", "[aout]",
            "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest",
            str(clip_out)
        ]
        subprocess.run(cmd_clip, check=True)
        clip_paths.append(clip_out)
        print(f"  Encoded Clip {num:02d}/16: {clip_dur:5.2f} sec -> {clip_out.name}")

    print(f"\n[INFO] Total Presentation Runtime: {total_presentation_time:.2f} seconds ({total_presentation_time/60:.2f} minutes)")
    return clip_paths, total_presentation_time

def generate_webvtt_subtitles(durations):
    """Generate WebVTT subtitles with slide timestamps for accessibility."""
    print(f"\n[INFO] Generating WebVTT Subtitles: {FINAL_VTT.name}...")
    
    def format_vtt_timestamp(seconds):
        hrs = int(seconds // 3600)
        mins = int((seconds % 3600) // 60)
        secs = seconds % 60
        return f"{hrs:02d}:{mins:02d}:{secs:06.3f}"

    current_sec = 0.0
    vtt_lines = ["WEBVTT", ""]

    for data in SLIDES_DATA:
        num = data["num"]
        dur = durations[num]
        start_t = format_vtt_timestamp(current_sec)
        end_t = format_vtt_timestamp(current_sec + dur)
        
        vtt_lines.append(f"{num}")
        vtt_lines.append(f"{start_t} --> {end_t}")
        vtt_lines.append(f"Slide {num:02d}: {data['title']}")
        vtt_lines.append(f"{data['script']}")
        vtt_lines.append("")
        
        current_sec += dur + 1.2 # matching slide padding

    with open(FINAL_VTT, "w", encoding="utf-8") as f:
        f.write("\n".join(vtt_lines))
    
    print(f"[SUCCESS] WebVTT Subtitles saved: {FINAL_VTT}")

def concat_presentation_video(clip_paths, total_time):
    """Concatenate all clips into final broadcast MP4 video with embedded subtitles."""
    print("\n[INFO] Assembling complete presentation video: 100_Beal_Street_History_and_Timeline_v1.mp4...")
    concat_list = VIDEO_CLIPS_DIR / "concat_list.txt"
    with open(concat_list, "w") as f:
        for p in clip_paths:
            f.write(f"file '{p.resolve()}'\n")

    # Mux concatenated clips and embed WebVTT subtitles as mov_text for native player CC
    cmd_concat = [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_list),
        "-i", str(FINAL_VTT),
        "-c:v", "copy",
        "-c:a", "copy",
        "-c:s", "mov_text",
        "-metadata:s:s:0", "language=eng",
        "-metadata:s:s:0", "title=English Narration",
        str(FINAL_VIDEO)
    ]
    try:
        subprocess.run(cmd_concat, check=True)
    except subprocess.CalledProcessError:
        # Fallback to copy without subtitle stream if mov_text encoding encounters container constraints
        cmd_fallback = [
            "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
            "-f", "concat", "-safe", "0",
            "-i", str(concat_list),
            "-c", "copy",
            str(FINAL_VIDEO)
        ]
        subprocess.run(cmd_fallback, check=True)

    # Verify final video properties
    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,size,bit_rate",
        "-of", "default=noprint_wrappers=1",
        str(FINAL_VIDEO)
    ]
    probe_out = subprocess.check_output(probe_cmd).decode().strip()
    print(f"[SUCCESS] Final Video Created Successfully!")
    print(f"Location: {FINAL_VIDEO}")
    print(f"Properties:\n{probe_out}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="100 Beal Street Presentation Video Production Pipeline")
    parser.add_argument("--skip-slides", action="store_true", help="Skip re-compiling HTML/PDF/PNG slides")
    parser.add_argument("--keep-audio", "--skip-tts", dest="keep_audio", action="store_true", help="Preserve existing audio in audio_narration/ (e.g. cloned user voice)")
    parser.add_argument("--force-tts", action="store_true", help="Force re-synthesizing all narration with system TTS")
    parser.add_argument("--voice", default="Samantha", help="macOS speech voice name (default: Samantha)")
    parser.add_argument("--rate", type=int, default=165, help="Speech rate in words per minute (default: 165)")
    args = parser.parse_args()

    print("=" * 80)
    print("100 Beal Street: Presentation Video Production Pipeline")
    print("=" * 80)

    # Step 1 & 2: Generate HTML slides & compile PDF/PNG images
    if not args.skip_slides:
        html_file = generate_slides_html()
        compile_pdf_and_images(html_file)
    else:
        print("\n[INFO] Skipping slide generation (--skip-slides passed).")

    # Step 3: Synthesize Slide Narration Audio (or preserve existing/cloned)
    force = args.force_tts and not args.keep_audio
    durations = synthesize_narration_audio(voice_name=args.voice, rate=args.rate, force=force)

    # Step 4: Generate WebVTT Subtitles matching exact durations
    generate_webvtt_subtitles(durations)

    # Step 5: Render Video Clips
    clip_paths, total_time = render_video_clips(durations)

    # Step 6: Concat final video with embedded subtitles
    concat_presentation_video(clip_paths, total_time)

    print("\n" + "=" * 80)
    print("VIDEO PRODUCTION PIPELINE COMPLETE!")
    print(f"Final MP4 Video: {FINAL_VIDEO}")
    print(f"Presentation Slides (PDF): {PDF_SLIDES}")
    print(f"WebVTT Subtitles: {FINAL_VTT}")
    print(f"Total Runtime: {total_time/60:.2f} minutes ({total_time:.2f} seconds)")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
