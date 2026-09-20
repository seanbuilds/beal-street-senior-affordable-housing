#!/usr/bin/env python3
"""
Generate Native 16:9 Widescreen PowerPoint Presentation for 100 Beal Street (Version 2)
Project: 100 Beal Street Senior Affordable Housing (Hingham, MA)
Identifier: generate_pptx_deck_v2.py
Constraint: Zero forbidden terms. File versioning v2.
Integrates exact legal reality: 1989 deed adolescent restriction across all 15 acres,
unrecorded 2006 Town Meeting release, 2024 ALTA survey note, and contingent Peabody lease.
"""

# /// script
# dependencies = [
#     "python-pptx>=0.6.21",
# ]
# ///

import os
import sys
import shutil
from pathlib import Path

try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN
    from pptx.enum.shapes import MSO_SHAPE
except ModuleNotFoundError:
    uv_bin = shutil.which("uv")
    if uv_bin and "_PPTX_REEXEC" not in os.environ:
        os.environ["_PPTX_REEXEC"] = "1"
        os.execvp(uv_bin, [uv_bin, "run", __file__] + sys.argv[1:])
    else:
        print("[ERROR] 'python-pptx' is required to generate the PowerPoint presentation.")
        print("Run with: uv run generate_pptx_deck_v2.py  OR  uv pip install python-pptx")
        sys.exit(1)

BASE_DIR = Path("/Volumes/BLK4TB/Housing Topics/Beal Street Senior Affordable Housing/agent_created_deliverables/video_presentation")
OUTPUT_PPTX = BASE_DIR / "100_Beal_Street_Presentation_v2.pptx"

# Color Constants (Hingham Municipal Palette)
NAVY = RGBColor(11, 34, 101)        # #0B2265
CRIMSON = RGBColor(158, 27, 50)     # #9E1B32
DARK_CHARCOAL = RGBColor(26, 29, 32)
SLATE_BG = RGBColor(241, 245, 249)  # #F1F5F9
CARD_BORDER = RGBColor(203, 213, 225)
GOLD = RGBColor(217, 119, 6)
WHITE = RGBColor(255, 255, 255)
MUTED_TEXT = RGBColor(100, 116, 139)

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # Blank slide

    slides_data = [
        {
            "num": 1,
            "title": "100 Beal Street: The 37-Year Journey",
            "subtitle": "From Naval Munitions Bunkers to State-Protected Senior Affordable Housing (1989–2026)",
            "is_title_slide": True,
            "cards": [
                {
                    "title": "Project Foundation",
                    "points": [
                        "Subject Property: 100 Beal Street, Hingham, MA (School Tract II)",
                        "Record Property Owner: Hingham Housing Authority (Independent State Public Entity)",
                        "Development Scope: 68-Unit Age-Restricted Senior Affordable Rental Community (62+)",
                        "Developer: Peabody Properties / Affordable Housing Services Corp. (99-Year Ground Lease)",
                        "Municipal Financial Impact: Exactly $0 in Town Borrowing or Taxpayer Debt"
                    ]
                }
            ],
            "notes": "Welcome to the definitive history of 100 Beal Street in Hingham, Massachusetts. Over the past thirty-seven years, this parcel of former Navy ammunition depot land has journeyed through military remediation, an unrecorded deed release, a Town Hall lawsuit vote, decisive state intervention, and an award-winning senior housing design. In this presentation, we walk through the exact documentary record, separating verified legal facts from persistent town rumors."
        },
        {
            "num": 2,
            "title": "April 1989: The Deed & The 30-Year Reverter",
            "subtitle": "Town Conveys 15.014 Acres of Surplus Military Land to HHA",
            "cards": [
                {
                    "title": "Recorded Fee Deed Facts",
                    "points": [
                        "Document Date: March 7, 1989 | Recording Date: April 21, 1989",
                        "Registry Citation: Plymouth County Registry of Deeds, Book 09097, Page 158 (Doc #29758)",
                        "Grantor: Inhabitants of the Town of Hingham | Grantee: Hingham Housing Authority",
                        "Stated Consideration: $45,751 for entire 15.014-acre parcel (School Tract II)"
                    ]
                },
                {
                    "title": "The 30-Year Reverter Clause (Page 160)",
                    "points": [
                        "Use Restriction: Solely for adolescent residential education / group care facility",
                        "Full Parcel Scope: Restriction legally applied to ALL 15.014 acres of School Tract II",
                        "Right of Re-Entry: Town retained right to enter if adolescent care ceased",
                        "Statutory Expiration: Deed expressly dictates re-entry terminates after thirty years under M.G.L. c. 184A, § 3",
                        "Expiration Date: March 7, 2019 (Exactly 30 years from deed execution)"
                    ]
                }
            ],
            "notes": "Our story begins on April 21st, 1989. The Town of Hingham conveyed a fifteen-acre parcel of surplus Navy depot land known as School Tract II to the independent Hingham Housing Authority for forty-five thousand seven hundred fifty-one dollars. The deed carried a specific restriction: the land was to be used for a residential educational facility for troubled adolescents. Critically, page one hundred sixty stated that if that youth use ever ceased, the Town retained a right of re-entry. However, the deed explicitly dictated that this right of re-entry terminated thirty years from the date of the deed."
        },
        {
            "num": 3,
            "title": "1990 to Present: Continuous Public Service",
            "subtitle": "The 12-Bed Adolescent Facility Operates Without Interruption",
            "cards": [
                {
                    "title": "Continuous Operational Compliance",
                    "points": [
                        "Facility Footprint: 12-bed group home constructed on dedicated 2.0-acre parcel fronting Beal Street",
                        "Funding Program: Commonwealth Chapter 689 specialized public housing funds",
                        "Operating Provider: Continuous license to specialized youth service providers under DCF",
                        "Zero Operational Default: At no point did youth care use cease between 1989 and 2026"
                    ]
                },
                {
                    "title": "Legal Implication of Unbroken Service",
                    "points": [
                        "Condition Precedent: Town re-entry required cessation of adolescent care",
                        "Unbroken Compliance: Continuous youth home use prevented any total default trigger",
                        "State Covenants: State Chapter 689 funding attached permanent public housing protections",
                        "Active Facility Today: Youth home continues operating on Lot 1, undisturbed by senior housing"
                    ]
                }
            ],
            "notes": "Shortly after the conveyance, a twelve-bed group home was constructed on a dedicated two-acre corner of the parcel along Beal Street, funded through the Commonwealth's Chapter 689 specialized housing program. For over thirty-five years, this facility has operated continuously under active state contracts caring for vulnerable youth. Because the facility never ceased operations and was never abandoned, the Town never had legal grounds to trigger a default or claim a re-entry during the entire thirty-year statutory window."
        },
        {
            "num": 4,
            "title": "June 2001: Demolition, Remediation & Division",
            "subtitle": "WWII Munitions Bunkers Cleared; 8-Acre Surplus Plateau Created",
            "cards": [
                {
                    "title": "Naval Depot Remediation",
                    "points": [
                        "Naval Ammunition Legacy: Interior 13 acres held abandoned concrete bunkers and earthen berms",
                        "Remediation Funding: Town funded demolition of structures and environmental soil cleanup",
                        "Administrative MOU: Town and HHA executed Memorandum of Understanding to coordinate future use",
                        "Site Clearance: Transformed overgrown military ruins into clean upland acreage"
                    ]
                },
                {
                    "title": "Plan 100 of 2001 Subdivision",
                    "points": [
                        "Recorded Survey: Gale Associates plan recorded in Plymouth Plan Book 44, Page 412",
                        "Lot 1 (2.000 Acres): Active adolescent group home with dedicated Beal Street access",
                        "Lot 2 (8.020 Acres): Remediated, buildable upland plateau fronting Beal Street",
                        "Milestone Result: Established clean legal boundaries for future municipal/housing needs"
                    ]
                }
            ],
            "notes": "Behind the adolescent home lay thirteen undeveloped acres containing abandoned World War II concrete ammunition bunkers and earth mounds from the old naval depot. In 2001, the Town funded the demolition of the bunkers and cleaned up hazardous materials. The Town and Housing Authority signed a Memorandum of Understanding and recorded Plan one hundred of 2001. This official survey divided the property into two parcels: Lot One, preserving the two-acre adolescent home, and Lot Two, an eight-acre remediated, buildable upland plateau with frontage on Beal Street."
        },
        {
            "num": 5,
            "title": "May 2006: Town Meeting Mandates Senior Housing",
            "subtitle": "Declared 2/3 Supermajority Authorizes Deed Release for Affordable Housing",
            "cards": [
                {
                    "title": "Warrant Article 38 Legislative Action",
                    "points": [
                        "Legislative Assembly: Hingham Annual Town Meeting (May 1, 2006)",
                        "Voting Threshold: Declared two-thirds supermajority vote in favor by Hingham voters",
                        "Mandate Text: Authorized Selectmen to amend 1989 deed restriction on School Tract II",
                        "Designated Purpose: Adding affordable senior housing as an express allowable use"
                    ]
                },
                {
                    "title": "The Administrative Breakdown",
                    "points": [
                        "Democratic Mandate: Clear Town Meeting directive dedicating land to senior housing",
                        "Town Hall Omission: Board of Selectmen never drafted, signed, or recorded deed release",
                        "Registry Reality: 1989 deed restriction remained technically unreleased on public records",
                        "Latent Vulnerability: The unrecorded release created a title defect that surfaced years later"
                    ]
                }
            ],
            "notes": "Twenty years ago, the citizens of Hingham took decisive action. At the May 2006 Annual Town Meeting, voters considered Warrant Article thirty-eight. By an overwhelming declared two-thirds supermajority, Town Meeting voted to authorize the Board of Selectmen to amend the 1989 deed restriction, explicitly adding affordable senior housing as an allowable use for the surplus plateau. This was a clear democratic mandate to build affordable homes for Hingham seniors. Yet in an extraordinary municipal oversight, Town Hall never actually drafted, executed, or recorded that authorized deed release at the Plymouth County Registry of Deeds."
        },
        {
            "num": 6,
            "title": "2017–2018: The Unexecuted Deed Resurfaces",
            "subtitle": "Beal Street Due Diligence Reveals the Unrecorded Release",
            "cards": [
                {
                    "title": "Title Due Diligence & Discovery",
                    "points": [
                        "Discovery Date: 2016–2017 title examination by Town Counsel Susan Murphy",
                        "The Finding: 2006 Town Meeting deed release was never executed or recorded at Registry",
                        "Selectmen Hearing Jan 30, 2018: Selectman Karen Johnson details 2001 remediation history",
                        "Selectmen Hearing Feb 13, 2018: HHA Chair Bob Keys requests review of covenants"
                    ]
                },
                {
                    "title": "Town Hall vs. Housing Authority",
                    "points": [
                        "Select Board Argument: Because back 13 acres were never used for youth, Town should recapture land",
                        "HHA Response: Board votes against voluntary conveyance; land is dedicated to public housing",
                        "Impasse: Town Hall prepares litigation strategy in executive session",
                        "Statutory Clock: 30-year deed reverter deadline of March 7, 2019 rapidly approaching"
                    ]
                }
            ],
            "notes": "For over a decade, the unrecorded deed release remained unnoticed. But between 2016 and 2017, during due diligence for adjacent parcels on Beal Street, Town Counsel Susan Murphy discovered that the 2006 deed release had never been recorded. Selectman Karen Johnson briefed the Board in public sessions on January 30th and February 13th, 2018, arguing that because the Town had funded the 2001 bunker demolition, the eight acres should belong to the Town. However, the Housing Authority Board declined to surrender the parcel, noting its complex title and statutory public housing mission."
        },
        {
            "num": 7,
            "title": "February 2019: The 30-Year Deadline & Lawsuit Vote",
            "subtitle": "Select Board Votes 3–0 to Sue Housing Authority Nine Days Before Deadline",
            "cards": [
                {
                    "title": "The Statutory Countdown",
                    "points": [
                        "Statutory Deadline: March 7, 2019 (Exactly 30 years from March 7, 1989 deed execution)",
                        "Legal Advice: Town Counsel advises right of re-entry terminates forever under c. 184A, § 3",
                        "Executive Session: February 26, 2019 at 6:45 PM (Nine days before deadline)",
                        "Open Session Action: Board reconvenes at 7:00 PM (Chairman Paul Healey presiding)"
                    ]
                },
                {
                    "title": "The 3–0 Lawsuit Vote",
                    "points": [
                        "Mover & Second: Motion by Healey, seconded by Johnson; passed 3–0 unanimous",
                        "Formal Mandate: 'To file litigation regarding enforcement of agreement as to 100 Beal Street'",
                        "Objective: Force Housing Authority to deed 100 Beal Street back to Town Hall",
                        "Significance: Town of Hingham prepares formal lawsuit against its own Housing Authority"
                    ]
                }
            ],
            "notes": "Town Counsel warned the Selectmen that under Massachusetts property law, if the thirty-year window closed without legal action, the Town's right of re-entry would expire forever. On February 26th, 2019—exactly nine days before the deadline—the Select Board met in Executive Session. Returning to Open Session at 7:00 PM, Chairman Paul Healey moved to file litigation against the Hingham Housing Authority to enforce the agreement on 100 Beal Street. Selectman Karen Johnson seconded, and the Board voted three to zero to authorize the lawsuit. Town Hall was prepared to take its own independent Housing Authority to court."
        },
        {
            "num": 8,
            "title": "June 2019: The Emergency Transfer Vote Under Duress",
            "subtitle": "Facing Litigation, Housing Authority Boards Vote to Surrender 19 Acres",
            "cards": [
                {
                    "title": "The Special Meeting Under Duress",
                    "points": [
                        "Meeting Date: June 5, 2019 (Special Meeting of HHA Board of Commissioners)",
                        "Litigation Pressure: Board confronted with imminent court filing by Town of Hingham",
                        "The Motion: Board votes to approve transfer of ~19 acres off Beal Street to the Town",
                        "Contemplated Surrender: Agreement to relinquish Lot 2 and associated Housing Authority parcels"
                    ]
                },
                {
                    "title": "The Legal Reality",
                    "points": [
                        "Illusion of Finality: Town Hall believed the property dispute had been settled",
                        "Statutory Barrier: Local housing authorities cannot convey public housing land unilaterally",
                        "State Financial Interest: Chapter 689 funding triggered mandatory Commonwealth supervision",
                        "Imminent State Reaction: State regulatory authorities intervene to safeguard the asset"
                    ]
                }
            ],
            "notes": "Confronted with the threat of an imminent lawsuit from Town Hall, the Hingham Housing Authority Board of Commissioners held an emergency special meeting on June 5th, 2019. Under intense legal pressure, the commissioners voted to approve a motion agreeing to transfer approximately nineteen acres of Housing Authority property off Beal Street back to municipal control. To outside observers, it appeared Town Hall had won the standoff and that the land was no longer under Housing Authority control. But an unexpected legal force was about to intervene."
        },
        {
            "num": 9,
            "title": "Summer 2019: The State Steps In",
            "subtitle": "Massachusetts DHCD Enforces Statutory Protections on Public Housing Land",
            "cards": [
                {
                    "title": "Independent Statutory Entity",
                    "points": [
                        "Governing Law: Massachusetts General Laws Chapter 121B (Housing and Urban Renewal)",
                        "Corporate Independence: Housing Authorities are independent public corporations, not Town departments",
                        "Municipal Separation: Board of Selectmen has zero statutory authority to direct HHA real estate",
                        "Public Purpose: Real estate must remain dedicated to low-income housing needs"
                    ]
                },
                {
                    "title": "Statutory Prohibition: M.G.L. c. 121B, § 34",
                    "points": [
                        "State Regulator: Massachusetts DHCD (Associate Director Amy Stitely)",
                        "Supervisory Letters: Issued April 19 and June 26, 2019 to HHA and Town Counsel",
                        "Statutory Bar: Real estate assisted with state funds cannot be sold or transferred without written state approval",
                        "Determination: DHCD formally refuses to consent to municipal conveyance"
                    ]
                }
            ],
            "notes": "Town Hall's victory was short-lived. Under Massachusetts General Laws Chapter 121B, local housing authorities are independent public corporations created by the Legislature, not municipal departments. Furthermore, because state public housing funding had been utilized at the Beal Street site, state law strictly prohibits any housing authority from selling or transferring public housing land without prior written approval from the Commonwealth. Massachusetts DHCD Associate Director Amy Stitely issued formal warnings to both the Housing Authority and Town Counsel, stating plainly that the proposed transfer violated state law and public housing covenants, and would not be approved."
        },
        {
            "num": 10,
            "title": "July 2019: The Legal Lock on Title",
            "subtitle": "Commonwealth Records Notice of Statutory Transfer Restriction",
            "cards": [
                {
                    "title": "Recorded Title Encumbrance",
                    "points": [
                        "Recording Date: July 18, 2019 at 1:44 PM",
                        "Citation: Plymouth County Registry of Deeds, Book 51379, Page 244 (Document No. 55967)",
                        "Regulator: Commonwealth of Massachusetts Department of Housing & Community Development",
                        "Subject Property: Assessor Map 58, Block 0, Lot 23 (100 Beal Street)"
                    ]
                },
                {
                    "title": "Operational Effect on Title",
                    "points": [
                        "Statutory Weapon: Cites M.G.L. c. 121B, § 34 directly on the public land title",
                        "Conveyance Void: Any deed executed without DHCD written approval is void as a matter of law",
                        "ALTA Survey Note: Formally identified as Schedule B, Item 5 encumbrance on 2024 boundary survey",
                        "Permanent Lock: Ensured parcel could never be repurposed away from public housing"
                    ]
                }
            ],
            "notes": "To ensure that Town Hall could not execute a transfer behind closed doors, the Commonwealth took decisive action on public land records. On July 18th, 2019, the state recorded a formal Notice of Statutory Transfer Restriction at the Plymouth County Registry of Deeds in Book fifty-one thousand three hundred seventy-nine, Page two hundred forty-four. Citing Chapter 121B, Section 34, this instrument legally encumbers 100 Beal Street. Any deed or transfer executed without the state's signature is void as a matter of law. The land was permanently locked for public affordable housing."
        },
        {
            "num": 11,
            "title": "September 2021: HHA Rescission & The Unresolved Title Cloud",
            "subtitle": "Ownership Reaffirmed, But 1989 Adolescent Restriction Remains on Record",
            "cards": [
                {
                    "title": "The Rescission Motion (Sept 7, 2021)",
                    "points": [
                        "Meeting: September 7, 2021 Regular Meeting at 30 Thaxter Street",
                        "Maker & Second: Moved by Commissioner O'Meara, seconded by Commissioner Lauter",
                        "Roll Call: Commissioners Suchecki, O'Meara, Lauter, Buhr vote 4–0 unanimous",
                        "Ownership Reaffirmed: Fee ownership remained with HHA under state statutory protection"
                    ]
                },
                {
                    "title": "The Continuing Title Cloud & Survey Finding",
                    "points": [
                        "The Unresolved Cloud: The 2021 vote did NOT erase the 1989 deed restriction from Registry",
                        "Missing Release: Town Hall never recorded the 2006 deed release on public land records",
                        "2024 ALTA Survey Note 3: Kellem & Kellem / Control Point survey explicitly states:",
                        "'THEREFORE NEED RELEASE OR CHANGE OF THIS RESTRICTION FROM THE TOWN OF HINGHAM'",
                        "Active Reality: Standoff between Town deed conditions and state housing policy remains open"
                    ]
                }
            ],
            "notes": "Backed by state regulatory authority and legal counsel, the Hingham Housing Authority Board reconvened on September 7th, 2021, voting four to zero to officially rescind its 2019 transfer motion. This confirmed that fee ownership of the land remained with the Housing Authority under state statutory protection. However, keeping ownership did not erase the 1989 deed restriction from public land records. The original restriction requiring the land to be used for adolescent care still technically encumbered the parcel because Town Hall never recorded the 2006 deed release. In fact, the official 2024 ALTA Title Survey specifically noted that the project still needs a formal release or change of this restriction from the Town of Hingham."
        },
        {
            "num": 12,
            "title": "December 2024: Verified Environmental Stewardship",
            "subtitle": "Conservation Commission Records MassDEP ORAD Protecting Tucker's Swamp",
            "cards": [
                {
                    "title": "MassDEP File No. 034-1509",
                    "points": [
                        "Application: Abbreviated Notice of Resource Area Delineation (ANRAD) for 100 Beal Street",
                        "Hearing Date: November 4, 2024 before Hingham Conservation Commission",
                        "Vote Result: Passed 5–0 unanimous (Nielsen, Mosher, Roby, Villanova, Freeman)",
                        "Recorded Instrument: Plymouth Registry Book 59527, Page 273 (Doc #78968, Dec 10, 2024)"
                    ]
                },
                {
                    "title": "155+ Verified Wetland Flags & Buffer Protection",
                    "points": [
                        "Delineation Expert: Christopher Lucas, PWS/PSS (Lucas Environmental, LLC)",
                        "Protected Resources: 3 Bordering Vegetated Wetlands, 2 Isolated Wetlands, confirmed vernal pool",
                        "Watershed Shield: Establishes permanent protective buffers for Tucker's Swamp and Back River ACEC",
                        "Upland Verification: Proves Lot B contains high, dry, fully buildable plateau outside buffer zones"
                    ]
                }
            ],
            "notes": "Before proceeding with architectural designs, the Housing Authority conducted rigorous environmental due diligence. Lucas Environmental delineated 155 wetland flags around Tucker's Swamp and the Weymouth Back River Area of Critical Environmental Concern. On November 4th, 2024, the Hingham Conservation Commission voted unanimously, five to zero, to approve an Order of Resource Area Delineation, recorded at the Registry in Book fifty-nine thousand five hundred twenty-seven, Page two hundred seventy-three. This binding environmental order confirmed that the development plateau on Lot B is high, dry, and completely outside sensitive wetland resource areas, safeguarding our natural waterways."
        },
        {
            "num": 13,
            "title": "August 2025: Peabody Award (Conditional Ground Lease)",
            "subtitle": "68 Senior Units Under a 99-Year Ground Lease Contingent on Title Resolution",
            "cards": [
                {
                    "title": "Public Procurement & Selection",
                    "points": [
                        "Procurement Solicitation: 155-Page RFP issued April 16, 2025 under M.G.L. c. 30B / c. 121B",
                        "Selection Vote: August 12, 2025 HHA meeting; passed 4–0 unanimous (Lauter, Weiser, O'Meara, Suchecki)",
                        "Designated Developer: Peabody Properties / Affordable Housing Services Corp. (AHSC)",
                        "Development Scope: 68 One- and Two-Bedroom Rental Apartments for Seniors 62+"
                    ]
                },
                {
                    "title": "99-Year Lease & Contingencies",
                    "points": [
                        "99-Year Ground Lease: Land ownership remains permanently with Hingham Housing Authority",
                        "Upfront Leasehold Fee: Developer pays $500,000 upfront fee to Housing Authority",
                        "Contingent Execution: Lease closing requires state approvals and formal resolution of deed restriction",
                        "Municipal Financial Impact: Exactly $0 in Town Debt or Municipal Taxpayer Borrowing"
                    ]
                }
            ],
            "notes": "In April 2025, the Housing Authority issued a comprehensive 155-page Request for Proposals under state procurement laws. On August 12th, 2025, the Housing Authority Board voted unanimously, four to zero, to award the development to Peabody Properties and Affordable Housing Services Corporation to build sixty-eight affordable apartments for seniors aged sixty-two and older under a ninety-nine-year ground lease. Under this arrangement, the Housing Authority retains permanent land ownership, receives a five hundred thousand dollar upfront fee, and taxpayers bear zero debt. However, final execution of the ground lease remains contingent upon obtaining state regulatory approvals and formally clearing the outstanding deed restriction through municipal agreement or the Chapter 40B permitting process."
        },
        {
            "num": 14,
            "title": "Architectural Vision: Modest, Sustainable & Senior-Focused",
            "subtitle": "Universal Design, Internal Courtyard, and Low-Impact Civil Engineering",
            "has_image": True,
            "image_path": "assets/weston_front.png",
            "cards": [
                {
                    "title": "Senior-Focused Design Specifications",
                    "points": [
                        "Modest Architectural Scale: 3-story wood-frame residential building complementing Hingham",
                        "100% Universal Accessibility: Single-floor barrier-free living, wide corridors, dual elevators",
                        "Community Amenities: Multi-purpose gathering hall, wellness clinic, garden courtyard",
                        "Natural Environmental Buffers: 50-foot undisturbed natural vegetative tree buffer to abutters",
                        "Advanced Stormwater Engineering: Bioretention swales filtering 100% of rainwater on-site"
                    ]
                }
            ],
            "notes": "The architectural design, created by Weston and Sampson, reflects thoughtful community integration. Rather than an institutional complex, the development features a modest three-story wood-frame building that complements Hingham's residential character. All sixty-eight units are designed with universal accessibility, wide corridors, and step-free access for aging in place. The site plan incorporates a protected central courtyard, community gardens, walking paths, and cutting-edge bioretention stormwater basins that filter rainwater on-site, preserving fifty feet of natural vegetative tree buffers between the residence and adjacent neighborhoods."
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
            "notes": "This brings us to the single biggest misconception in town: why do so many residents believe Town Meeting killed the senior housing project? The project defeated on April 27th, 2026, was NOT 100 Beal Street. It was the Center for Active Living, or CAL—a separate twenty-nine-point-nine million dollar municipal daytime senior center that the Select Board proposed building inside Bare Cove Park. That project required Town Meeting to approve thirty million dollars in taxpayer borrowing, which failed to achieve the necessary two-thirds debt supermajority. Because both projects involved seniors and both bordered Tucker's Swamp, the community blurred them together. 100 Beal Street requires zero Town debt and was never voted down."
        },
        {
            "num": 16,
            "title": "Conclusion & The Path Forward: Resolving the Final Hurdle",
            "subtitle": "37 Years of History Moving Toward Permitting and Municipal Resolution",
            "cards": [
                {
                    "title": "Core Achievements & Security",
                    "points": [
                        "37-Year Evolution: Naval Depot → Adolescent Care → Bunker Cleanup → Senior Housing",
                        "Secure Ownership: Land remains in Housing Authority ownership under state statutory protection",
                        "Environmental Clearance: 155+ wetland flags stamped under recorded MassDEP ORAD",
                        "Democratic Legitimacy: 2006 Town Meeting 2/3 supermajority authorized senior housing use"
                    ]
                },
                {
                    "title": "The Final Hurdle & Next Steps",
                    "points": [
                        "The Unresolved Hurdle: Formally clearing the historic 1989 deed restriction on title",
                        "Dual Pathways: Select Board execution of 2006 authorized release OR Chapter 40B override",
                        "Community Benefit: 68 permanently affordable homes for seniors with $0 municipal debt",
                        "Path Forward: Comprehensive Permit application, state regulatory reviews, and civic dialogue"
                    ]
                }
            ],
            "notes": "The thirty-seven-year history of 100 Beal Street is a story of community evolution—from a World War II ammunition depot to an adolescent care home, through hazardous bunker cleanup, and toward urgently needed senior affordable housing. Today, the Housing Authority holds fee title under state statutory protection, and environmental regulators have confirmed the buildable plateau protects Tucker's Swamp. The final chapter involves resolving the historic deed restriction with the Town—either by executing the release Town Meeting authorized in 2006 or through the Comprehensive Permit process. As this sixty-eight-unit senior residence advances, it represents a path to fulfill a twenty-year community promise without costing Hingham taxpayers a single dollar in municipal debt."
        }
    ]

    for slide_info in slides_data:
        num = slide_info["num"]
        slide = prs.slides.add_slide(blank_layout)
        is_title = slide_info.get("is_title_slide", False)

        # Background
        bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg_shape.line.color.rgb = NAVY if is_title else WHITE
        bg_shape.fill.solid()
        bg_shape.fill.fore_color.rgb = NAVY if is_title else WHITE

        # Top Accent Line
        accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.15))
        accent.line.fill.background()
        accent.fill.solid()
        accent.fill.fore_color.rgb = GOLD if is_title else CRIMSON

        # Header Box
        header_top = Inches(0.8) if not is_title else Inches(1.5)
        header_box = slide.shapes.add_textbox(Inches(0.8), header_top, Inches(11.7), Inches(1.2))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = slide_info["title"]
        p1.font.name = "Arial"
        p1.font.size = Pt(36) if not is_title else Pt(44)
        p1.font.bold = True
        p1.font.color.rgb = WHITE if is_title else NAVY

        p2 = tf.add_paragraph()
        p2.text = slide_info["subtitle"]
        p2.font.name = "Arial"
        p2.font.size = Pt(20) if not is_title else Pt(24)
        p2.font.bold = True
        p2.font.color.rgb = GOLD if is_title else CRIMSON
        p2.space_before = Pt(8)

        # Content Handling
        if slide_info.get("is_comparison"):
            rows = len(slide_info["comparison_data"])
            cols = 3
            left = Inches(0.8)
            top = Inches(2.2)
            width = Inches(11.733)
            height = Inches(4.5)
            table_shape = slide.shapes.add_table(rows, cols, left, top, width, height)
            table = table_shape.table
            table.columns[0].width = Inches(2.8)
            table.columns[1].width = Inches(4.466)
            table.columns[2].width = Inches(4.466)

            for r_idx, row in enumerate(slide_info["comparison_data"]):
                for c_idx, val in enumerate(row):
                    cell = table.cell(r_idx, c_idx)
                    cell.text = val
                    for paragraph in cell.text_frame.paragraphs:
                        paragraph.font.name = "Arial"
                        if r_idx == 0:
                            paragraph.font.size = Pt(14)
                            paragraph.font.bold = True
                            paragraph.font.color.rgb = WHITE
                            cell.fill.solid()
                            cell.fill.fore_color.rgb = NAVY
                        else:
                            paragraph.font.size = Pt(13)
                            if c_idx == 0:
                                paragraph.font.bold = True
                                paragraph.font.color.rgb = DARK_CHARCOAL
                            elif c_idx == 1:
                                paragraph.font.color.rgb = RGBColor(6, 95, 70)
                            else:
                                paragraph.font.color.rgb = RGBColor(153, 27, 27)

        elif slide_info.get("has_image"):
            img_rel = slide_info["image_path"]
            img_abs = str((BASE_DIR / img_rel).resolve())
            if os.path.exists(img_abs):
                slide.shapes.add_picture(img_abs, Inches(0.8), Inches(2.2), Inches(6.0), Inches(4.5))
            card = slide_info["cards"][0]
            c_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(2.2), Inches(5.4), Inches(4.5))
            c_box.line.color.rgb = CARD_BORDER
            c_box.fill.solid()
            c_box.fill.fore_color.rgb = SLATE_BG
            ctf = c_box.text_frame
            ctf.word_wrap = True
            ctf.margin_left = ctf.margin_right = ctf.margin_top = ctf.margin_bottom = Inches(0.3)
            cp = ctf.paragraphs[0]
            cp.text = card["title"]
            cp.font.name = "Arial"
            cp.font.size = Pt(18)
            cp.font.bold = True
            cp.font.color.rgb = NAVY
            cp.space_after = Pt(12)
            for pt_text in card["points"]:
                pt_p = ctf.add_paragraph()
                pt_p.text = f"■  {pt_text}"
                pt_p.font.name = "Arial"
                pt_p.font.size = Pt(13)
                pt_p.font.color.rgb = DARK_CHARCOAL
                pt_p.space_after = Pt(10)

        elif is_title:
            card = slide_info["cards"][0]
            c_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(3.2), Inches(10.333), Inches(3.2))
            c_box.line.color.rgb = GOLD
            c_box.fill.solid()
            c_box.fill.fore_color.rgb = RGBColor(16, 42, 115)
            ctf = c_box.text_frame
            ctf.word_wrap = True
            ctf.margin_left = ctf.margin_right = ctf.margin_top = ctf.margin_bottom = Inches(0.4)
            cp = ctf.paragraphs[0]
            cp.text = card["title"]
            cp.font.name = "Arial"
            cp.font.size = Pt(20)
            cp.font.bold = True
            cp.font.color.rgb = GOLD
            cp.space_after = Pt(12)
            for pt_text in card["points"]:
                pt_p = ctf.add_paragraph()
                pt_p.text = f"■  {pt_text}"
                pt_p.font.name = "Arial"
                pt_p.font.size = Pt(14)
                pt_p.font.color.rgb = WHITE
                pt_p.space_after = Pt(8)

        else:
            cards = slide_info["cards"]
            left_pos = [Inches(0.8), Inches(6.8)]
            card_width = Inches(5.7)
            card_height = Inches(4.5)
            for c_idx, card in enumerate(cards):
                c_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos[c_idx], Inches(2.2), card_width, card_height)
                c_box.line.color.rgb = CARD_BORDER
                c_box.fill.solid()
                c_box.fill.fore_color.rgb = SLATE_BG
                ctf = c_box.text_frame
                ctf.word_wrap = True
                ctf.margin_left = ctf.margin_right = ctf.margin_top = ctf.margin_bottom = Inches(0.35)
                cp = ctf.paragraphs[0]
                cp.text = card["title"]
                cp.font.name = "Arial"
                cp.font.size = Pt(18)
                cp.font.bold = True
                cp.font.color.rgb = NAVY
                cp.space_after = Pt(14)
                for pt_text in card["points"]:
                    pt_p = ctf.add_paragraph()
                    pt_p.text = f"■  {pt_text}"
                    pt_p.font.name = "Arial"
                    pt_p.font.size = Pt(13)
                    pt_p.font.color.rgb = DARK_CHARCOAL
                    pt_p.space_after = Pt(10)

        # Footer
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.9), Inches(11.7), Inches(0.4))
        ftf = footer_box.text_frame
        ftf.margin_left = ftf.margin_top = ftf.margin_right = ftf.margin_bottom = 0
        fp = ftf.paragraphs[0]
        fp.text = f"100 Beal Street Senior Affordable Housing • Slide {num} of 16"
        fp.font.name = "Arial"
        fp.font.size = Pt(11)
        fp.font.color.rgb = WHITE if is_title else MUTED_TEXT

        # Speaker Notes
        if "notes" in slide_info:
            notes_slide = slide.notes_slide
            notes_tf = notes_slide.notes_text_frame
            notes_tf.text = slide_info["notes"]

    prs.save(str(OUTPUT_PPTX))
    print(f"[OK] PowerPoint Presentation v2 successfully created: {OUTPUT_PPTX}")
    print(f"     Total Slides: {len(slides_data)} (16:9 Widescreen)")

if __name__ == "__main__":
    create_presentation()
