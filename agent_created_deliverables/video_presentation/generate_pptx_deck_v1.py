#!/usr/bin/env python3
"""
Generate Native 16:9 Widescreen PowerPoint Presentation for 100 Beal Street
Project: 100 Beal Street Senior Affordable Housing (Hingham, MA)
Identifier: generate_pptx_deck_v1.py
Constraint: Zero forbidden terms. File versioning v1.
"""

# /// script
# dependencies = [
#     "python-pptx>=0.6.21",
# ]
# ///

import os
import sys
import shutil

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
        print("Run with: uv run generate_pptx_deck_v1.py  OR  uv pip install python-pptx")
        sys.exit(1)

# Color Constants
NAVY = RGBColor(11, 34, 101)       # #0B2265
CRIMSON = RGBColor(158, 27, 50)    # #9E1B32
DARK_CHARCOAL = RGBColor(26, 29, 32)
SLATE_BG = RGBColor(241, 245, 249) # #F1F5F9
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
                        "Operating Provider: Continuous license to specialized youth service providers",
                        "Zero Operational Default: At no point did youth care use cease between 1989 and 2019"
                    ]
                },
                {
                    "title": "Legal Implication of Unbroken Service",
                    "points": [
                        "Condition Precedent: Town re-entry required cessation of adolescent care",
                        "Unbroken Compliance: Continuous use prevented any default trigger",
                        "State Covenants: State Chapter 689 funding attached permanent public housing protections",
                        "Result: The Town never had lawful grounds to re-enter during the 30-year window"
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
                        "Historical Condition: Interior 13 acres held abandoned WWII naval ammunition bunkers and earthen berms",
                        "Remediation Project: Town of Hingham funded demolition and hazardous materials cleanup",
                        "Gale Associates Survey: Plan 100 of 2001 (Plymouth Plan Book 44, Page 412)",
                        "Administrative MOU: Town and Housing Authority execute cooperative site agreement"
                    ]
                },
                {
                    "title": "Division of School Tract II",
                    "points": [
                        "Lot 1 (2.000 Acres): Active adolescent group home and dedicated frontage",
                        "Lot 2 (8.020 Acres): Remediated, buildable upland plateau with frontage on Beal Street",
                        "Topography: High, dry plateau separated from rear wetland basin",
                        "Outcome: Established clean, separate building lot for future community housing"
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
                    "title": "Democratic Town Meeting Mandate",
                    "points": [
                        "Legislative Assembly: Hingham Annual Town Meeting (May 1, 2006)",
                        "Warrant Article 38: Sponsored to dedicate Lot 2 plateau for affordable senior living",
                        "Voting Threshold: Passed by declared two-thirds supermajority vote",
                        "Certified Enactment: Official certification sealed by Town Clerk Eileen A. McCracken"
                    ]
                },
                {
                    "title": "The Unrecorded Mandate",
                    "points": [
                        "Vote Directive: Authorized Selectmen to amend 1989 deed to allow residential affordable housing",
                        "The Administrative Breakdown: Town Hall never executed or recorded the amended deed release",
                        "Public Records Gap: Omission went completely unnoticed in municipal files for over a decade",
                        "Key Takeaway: Hingham voters affirmatively approved affordable housing on this site in 2006"
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
                    "title": "Discovery of the Unrecorded Release",
                    "points": [
                        "Title Review: Town Counsel Susan Murphy discovers the 2006 deed amendment was never recorded",
                        "Selectmen Jan 30, 2018: Selectman Karen Johnson details 2001 bunker demolition costs",
                        "Town Position: Selectmen argue Town paid remediation, so 8 acres should belong to Town",
                        "HHA Position: HHA Chair Bob Keys requests full legal review of title restrictions"
                    ]
                },
                {
                    "title": "The Impasse",
                    "points": [
                        "Separate Corporate Entities: Housing Authority is an independent public body under state law",
                        "HHA Board Action: Commissioners decline voluntary transfer of public housing land",
                        "Title Complexity: Land encumbered by historic Department of Interior covenants and state rules",
                        "Mounting Friction: Selectmen initiate confidential executive session review"
                    ]
                }
            ],
            "notes": "For over a decade, the unrecorded deed release remained unnoticed. But between 2016 and 2017, during due diligence for adjacent parcels on Beal Street, Town Counsel Susan Murphy discovered that the 2006 deed amendment had never been recorded. Selectman Karen Johnson briefed the Board in public sessions on January 30th and February 13th, 2018, arguing that because the Town had funded the 2001 bunker demolition, the eight acres should belong to the Town. However, the Housing Authority Board declined to surrender the parcel, noting its complex title and statutory public housing mission."
        },
        {
            "num": 7,
            "title": "February 2019: The 30-Year Deadline & Lawsuit Vote",
            "subtitle": "Select Board Votes 3–0 to Sue Housing Authority Nine Days Before Deadline",
            "cards": [
                {
                    "title": "The Looming 30-Year Clock",
                    "points": [
                        "Expiration Date: March 7, 2019 (Exactly 30 years from March 7, 1989 deed execution)",
                        "Legal Advice: Town Counsel advises that right of re-entry permanently terminates on day 30",
                        "Emergency Executive Session: February 26, 2019 at 6:45 PM (Nine days before deadline)",
                        "Public Reconvening: Board returns to open session at 7:00 PM"
                    ]
                },
                {
                    "title": "The Unanimous Litigation Vote",
                    "points": [
                        "Roster: Paul Healey (Chair), Karen Johnson (Selectman), Mary Power (Selectman)",
                        "Motion: Chair Healey moves to file litigation regarding enforcement of agreement at 100 Beal",
                        "Second: Seconded by Selectman Karen Johnson",
                        "Vote Tally: Passed 3–0 unanimous; Town formally authorizes lawsuit against HHA"
                    ]
                }
            ],
            "notes": "By February 2019, the situation reached a boiling point. The thirty-year calendar mark from the 1989 deed was set to expire on March 7th, 2019. Under Massachusetts law, if that date passed, any right of re-entry the Town held would vanish forever. On February 26th, exactly nine days before the deadline, the Select Board convened in Executive Session. Returning to Open Session, Selectman Karen Johnson seconded a motion by Chairman Paul Healey, and the Board voted three to zero to authorize formal litigation against their own Housing Authority to force them to deed the land back to the Town."
        },
        {
            "num": 8,
            "title": "June 2019: The Surrender Under Litigation Threat",
            "subtitle": "Housing Authority Initially Votes to Transfer 19 Acres to Town Hall",
            "cards": [
                {
                    "title": "Confrontation at 30 Thaxter Street",
                    "points": [
                        "Emergency Meeting: June 5, 2019 Special Meeting of HHA Board of Commissioners",
                        "Litigation Pressure: Threat of imminent Town lawsuit creating severe legal liabilities",
                        "Board Action: HHA commissioners vote to approve transferring ~19 acres back to Town",
                        "Scope: Included Lot 2 surplus acreage and adjacent Town-associated parcel"
                    ]
                },
                {
                    "title": "The Legal Fragility of the Vote",
                    "points": [
                        "Superficial Settlement: To casual observers, the land dispute appeared resolved",
                        "Statutory Reality: Housing Authorities cannot convey public housing property unilaterally",
                        "State Jurisdiction: Commonwealth Chapter 689 funding triggered mandatory state review",
                        "Pending Intervention: State oversight agencies stepped in to halt the transfer"
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
            "title": "September 2021: The Unanimous Rescission Vote",
            "subtitle": "Housing Authority Formally Cancels 2019 Transfer Motion",
            "cards": [
                {
                    "title": "The Rescission Motion",
                    "points": [
                        "Meeting: September 7, 2021 Regular Meeting at 30 Thaxter Street",
                        "Maker & Second: Moved by Commissioner O'Meara, seconded by Commissioner Lauter",
                        "Substance: Formally rescinds the June 5, 2019 motion transferring ~19 acres to Town",
                        "Legal Grounding: Backed by formal DHCD correspondence and municipal counsel opinions"
                    ]
                },
                {
                    "title": "The 4–0 Unanimous Roll Call",
                    "points": [
                        "Roll Call Vote: Commissioners Suchecki, O'Meara, Lauter, Buhr all vote in favor",
                        "Certified Minute Text: 'The Motion was passed on a 4-0 vote. That Motion is now rescinded'",
                        "Title Affirmation: Parcel declared to remain in sole ownership of HHA for affordable housing",
                        "Definitive Close: Put an end to Town Hall's attempted municipal recapture"
                    ]
                }
            ],
            "notes": "Backed by state regulatory authority and legal counsel, the Hingham Housing Authority Board of Commissioners reconvened on September 7th, 2021, to settle the issue permanently. Commissioner O’Meara made a formal motion, seconded by Commissioner Lauter, to rescind the June 2019 transfer vote. The motion passed unanimously on a four to zero roll call vote. The official minutes declared unequivocally that the transfer was rescinded, and that the parcel would remain in the sole ownership of the Hingham Housing Authority to fulfill its mission of providing senior affordable housing."
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
            "title": "August 2025: Peabody Properties Awarded Project",
            "subtitle": "68 Senior Rental Apartments Under a 99-Year Ground Lease",
            "cards": [
                {
                    "title": "Public Procurement & Selection",
                    "points": [
                        "Procurement Solicitation: 155-Page RFP issued April 16, 2025 under M.G.L. c. 30B",
                        "Selection Vote: August 12, 2025 HHA meeting; passed 4–0 unanimous (Lauter, Weiser, O'Meara, Suchecki)",
                        "Designated Developer: Peabody Properties / Affordable Housing Services Corp. (AHSC)",
                        "Development Scope: 68 One- and Two-Bedroom Rental Apartments for Seniors 62+"
                    ]
                },
                {
                    "title": "Financial & Leasehold Structure",
                    "points": [
                        "99-Year Ground Lease: Land ownership remains permanently with Hingham Housing Authority",
                        "Upfront Leasehold Consideration: Developer pays $500,000 upfront fee to Housing Authority",
                        "Construction Financing: 100% financed through private equity and state/federal tax credits",
                        "Municipal Financial Impact: Exactly $0 in Town Debt or Municipal Taxpayer Borrowing"
                    ]
                }
            ],
            "notes": "In April 2025, the Housing Authority issued a comprehensive 155-page Request for Proposals under state procurement laws. On August 12th, 2025, following competitive evaluation, the Housing Authority Board voted unanimously, four to zero, to award the development to Peabody Properties and Affordable Housing Services Corporation. Under the agreement, Peabody will build a sixty-eight-unit rental community restricted to seniors aged sixty-two and older. The project utilizes a ninety-nine-year ground lease, meaning the town housing authority retains permanent land ownership, receives a five hundred thousand dollar upfront fee, and taxpayers bear zero debt."
        },
        {
            "num": 14,
            "title": "Architectural Vision: Modest, Sustainable & Senior-Focused",
            "subtitle": "Universal Design, Internal Courtyard, and Low-Impact Civil Engineering",
            "cards": [
                {
                    "title": "Senior-Centric Architecture",
                    "points": [
                        "Design Team: Weston & Sampson architects and engineers",
                        "Building Scale: Modest 3-story wood-frame design harmonizing with residential neighborhood",
                        "Universal Accessibility: Step-free access, dual elevators, wide corridors, zero barrier showers",
                        "Resident Amenities: Multi-purpose community center, wellness exam room, walking paths, gardens"
                    ]
                },
                {
                    "title": "Civil & Environmental Engineering",
                    "points": [
                        "Stormwater Management: State-of-the-art bioretention basins and rain gardens filtering all runoff",
                        "Wetland Protection: Positioned strictly within buildable upland; zero direct wetland disturbance",
                        "Vegetative Buffers: 50-foot undisturbed natural tree buffer surrounding the entire perimeter",
                        "Sustainability: High-efficiency electric heat pumps and solar-ready structural roof engineering"
                    ]
                }
            ],
            "notes": "The architectural design, created by Weston and Sampson, reflects thoughtful community integration. Rather than an institutional complex, the development features a modest three-story wood-frame building that complements Hingham's residential character. All sixty-eight units are designed with universal accessibility, wide corridors, and step-free access for aging in place. The site plan incorporates a protected central courtyard, community gardens, walking paths, and cutting-edge bioretention stormwater basins that filter rainwater on-site, preserving fifty feet of natural vegetative tree buffers between the residence and adjacent neighborhoods."
        },
        {
            "num": 15,
            "title": "Clearing Up the Town Rumor: CAL vs. 100 Beal Street",
            "subtitle": "The Defeated Project Was Bare Cove Park CAL; 100 Beal Street Is Fully Active",
            "cards": [
                {
                    "title": "Center for Active Living (CAL) [DEFEATED]",
                    "points": [
                        "Location: Inside Bare Cove Park boundary (Bare Cove Park Drive)",
                        "Purpose: Municipal daytime senior activity and recreation facility",
                        "Cost to Taxpayers: $29,930,000 Municipal Debt Exclusion Borrowing",
                        "Town Meeting Action: April 27, 2026 Warrant Article 12",
                        "Vote Result: 510 Yes to 470 No (52% in favor; FAILED 2/3 debt supermajority requirement)"
                    ]
                },
                {
                    "title": "100 Beal Street Senior Housing [ACTIVE & PERMITTED]",
                    "points": [
                        "Location: 100 Beal Street (School Tract II Surplus Plateau, Lot B)",
                        "Purpose: 68-Unit Permanent Affordable Senior Rental Residences (62+)",
                        "Cost to Taxpayers: Exactly $0 in Town Borrowing / $0 Municipal Debt",
                        "Town Meeting Action: NEVER voted down or rejected at Town Meeting",
                        "Current Legal Status: Active, permitted development proceeding under 99-year ground lease"
                    ]
                }
            ],
            "notes": "Now we must address the single biggest rumor in Hingham: the belief that Town Meeting voted down 100 Beal Street. This is completely false. On April 27th, 2026, Town Meeting debated Warrant Article twelve. That article proposed borrowing nearly thirty million dollars in municipal taxpayer debt to build the Center for Active Living—a daytime senior activities center inside Bare Cove Park. Under state finance law, municipal borrowing requires a strict two-thirds supermajority. The bond failed, receiving fifty-two percent. Because both projects involved seniors and both bordered Tucker's Swamp, rumors spread that the senior project died. In reality, 100 Beal Street was never on the ballot, costs taxpayers zero dollars, and is actively moving forward."
        },
        {
            "num": 16,
            "title": "The Horizon: Permitting, Groundbreaking & Legacy",
            "subtitle": "Comprehensive Permit, Financing Milestones, and Permanent Affordability",
            "cards": [
                {
                    "title": "Development Permitting Milestones",
                    "points": [
                        "August 2026: Execution of Land Disposition & Development Agreement (LDDA)",
                        "Fall 2026–2027: M.G.L. c. 40B Comprehensive Permit review before Hingham Zoning Board",
                        "2027: State Affordable Housing Tax Credit Allocation (EOHLC / MassHousing / DHCD)",
                        "2028: Groundbreaking on 68 units of permanently affordable senior housing"
                    ]
                },
                {
                    "title": "A 37-Year Community Legacy",
                    "points": [
                        "Living With Dignity: Enables long-time Hingham seniors to remain in the town they built",
                        "Veterans Preference: Local housing preference for eligible Hingham military veterans",
                        "Permanent Public Ownership: Land remains with Housing Authority for generations to come",
                        "Democratic Fulfillment: Honors the supermajority vote cast by Hingham voters in 2006"
                    ]
                }
            ],
            "notes": "As of late 2026, 100 Beal Street is advancing through its final development phases. The Housing Authority is executing the formal Land Disposition Agreement with Peabody Properties. Permitting will proceed through a Chapter 40B Comprehensive Permit before the Zoning Board of Appeals, followed by state affordable housing tax credit financing. Construction will bring sixty-eight modern, dignified homes for Hingham's aging residents. Thirty-seven years after School Tract II was first deeded, this historic parcel will finally fulfill its democratic promise: offering Hingham seniors a permanent, affordable place to call home."
        }
    ]

    for data in slides_data:
        slide = prs.slides.add_slide(blank_layout)

        # Background Fill
        bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg_shape.line.fill.background()
        if data.get("is_title_slide"):
            bg_shape.fill.solid()
            bg_shape.fill.fore_color.rgb = NAVY
        else:
            bg_shape.fill.solid()
            bg_shape.fill.fore_color.rgb = WHITE

        # Top Header Accent Bar (for non-title slides)
        if not data.get("is_title_slide"):
            header_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.12))
            header_bar.fill.solid()
            header_bar.fill.fore_color.rgb = CRIMSON
            header_bar.line.fill.background()

            # Slide Number Badge
            badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(12.0), Inches(0.3), Inches(0.9), Inches(0.4))
            badge.fill.solid()
            badge.fill.fore_color.rgb = NAVY
            badge.line.fill.background()
            badge_tf = badge.text_frame
            badge_tf.word_wrap = True
            badge_p = badge_tf.paragraphs[0]
            badge_p.text = f"{data['num']:02d} / 16"
            badge_p.font.size = Pt(12)
            badge_p.font.bold = True
            badge_p.font.color.rgb = WHITE
            badge_p.alignment = PP_ALIGN.CENTER

        # Title & Subtitle Box
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.3 if not data.get("is_title_slide") else 1.0), Inches(11.5), Inches(1.3))
        tf = title_box.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = data["title"]
        p1.font.bold = True
        p1.font.name = "Arial"
        if data.get("is_title_slide"):
            p1.font.size = Pt(36)
            p1.font.color.rgb = WHITE
        else:
            p1.font.size = Pt(26)
            p1.font.color.rgb = NAVY

        p2 = tf.add_paragraph()
        p2.text = data["subtitle"]
        p2.font.name = "Arial"
        p2.font.size = Pt(16)
        if data.get("is_title_slide"):
            p2.font.color.rgb = GOLD
        else:
            p2.font.color.rgb = CRIMSON
        p2.space_before = Pt(4)

        # Content Cards
        cards = data.get("cards", [])
        num_cards = len(cards)
        if num_cards == 1:
            card_width = Inches(11.733)
            card_gap = Inches(0)
            start_left = Inches(0.8)
        else:
            card_width = Inches(5.666)
            card_gap = Inches(0.4)
            start_left = Inches(0.8)

        card_top = Inches(1.8 if not data.get("is_title_slide") else 2.6)
        card_height = Inches(4.9 if not data.get("is_title_slide") else 4.2)

        for i, card in enumerate(cards):
            left = start_left + i * (card_width + card_gap)
            c_shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, card_top, card_width, card_height)
            c_shape.fill.solid()
            if data.get("is_title_slide"):
                c_shape.fill.fore_color.rgb = RGBColor(18, 48, 128)
                c_shape.line.color.rgb = GOLD
            else:
                c_shape.fill.fore_color.rgb = SLATE_BG
                c_shape.line.color.rgb = CARD_BORDER
            c_shape.line.width = Pt(1.5)

            ctf = c_shape.text_frame
            ctf.word_wrap = True
            ctf.margin_left = Inches(0.3)
            ctf.margin_right = Inches(0.3)
            ctf.margin_top = Inches(0.3)
            ctf.margin_bottom = Inches(0.3)

            # Card Header
            cp = ctf.paragraphs[0]
            cp.text = card["title"]
            cp.font.bold = True
            cp.font.name = "Arial"
            cp.font.size = Pt(18)
            if data.get("is_title_slide"):
                cp.font.color.rgb = GOLD
            else:
                cp.font.color.rgb = NAVY
            cp.space_after = Pt(12)

            # Card Bullet Points
            for point in card["points"]:
                bp = ctf.add_paragraph()
                bp.text = f"•  {point}"
                bp.font.name = "Arial"
                bp.font.size = Pt(14)
                if data.get("is_title_slide"):
                    bp.font.color.rgb = WHITE
                else:
                    bp.font.color.rgb = DARK_CHARCOAL
                bp.space_after = Pt(8)

        # Slide Notes (Exact Spoken Narration Script)
        notes_slide = slide.notes_slide
        text_frame = notes_slide.notes_text_frame
        text_frame.text = data["notes"]

    output_path = "/Volumes/BLK4TB/Housing Topics/Beal Street Senior Affordable Housing/agent_created_deliverables/video_presentation/100_Beal_Street_Presentation_v1.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to {output_path}")

if __name__ == "__main__":
    create_presentation()
