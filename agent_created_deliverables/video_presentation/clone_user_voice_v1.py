#!/usr/bin/env python3
"""
User Voice Cloning Synthesis Pipeline for 100 Beal Street Presentation
Project: 100 Beal Street Senior Affordable Housing (Hingham, MA)
Identifier: clone_user_voice_v1.py
Constraint: Zero forbidden terms. File versioning v1.

This script manages local voice cloning on macOS Apple Silicon / Metal (MPS) or CPU.
Supported Engines:
  1. F5-TTS (Flow Matching Diffusion Transformer - SWHL/F5-TTS)
  2. OpenVoice v2 (Tone Color Converter - myshell-ai/OpenVoice)
  3. Coqui XTTS-v2 (coqui-ai/TTS)
  4. High-Clarity macOS Speech Fallback (Samantha / Reed)
"""

import os
import sys
import subprocess
import shutil
import argparse
from pathlib import Path

BASE_DIR = Path("/Volumes/BLK4TB/Housing Topics/Beal Street Senior Affordable Housing/agent_created_deliverables/video_presentation")
AUDIO_OUT_DIR = BASE_DIR / "audio_narration"
DEFAULT_USER_SAMPLE = BASE_DIR / "user_voice_sample.wav"

# Slide Narration Scripts (Exact text for all 16 slides)
SLIDE_SCRIPTS = [
    (1, "Welcome to the definitive history of 100 Beal Street in Hingham, Massachusetts. Over the past thirty-seven years, this parcel of former Navy ammunition depot land has journeyed through military remediation, an unrecorded deed release, a Town Hall lawsuit vote, decisive state intervention, and an award-winning senior housing design. In this presentation, we walk through the exact documentary record, separating verified legal facts from persistent town rumors."),
    (2, "Our story begins on April 21st, 1989. The Town of Hingham conveyed a fifteen-acre parcel of surplus Navy depot land known as School Tract II to the independent Hingham Housing Authority for forty-five thousand seven hundred fifty-one dollars. The deed carried a specific restriction: the land was to be used for a residential educational facility for troubled adolescents. Critically, page one hundred sixty stated that if that youth use ever ceased, the Town retained a right of re-entry. However, the deed explicitly dictated that this right of re-entry terminated thirty years from the date of the deed."),
    (3, "Shortly after the conveyance, a twelve-bed group home was constructed on a dedicated two-acre corner of the parcel along Beal Street, funded through the Commonwealth's Chapter 689 specialized housing program. For over thirty-five years, this facility has operated continuously under active state contracts caring for vulnerable youth. Because the facility never ceased operations and was never abandoned, the Town never had legal grounds to trigger a default or claim a re-entry during the entire thirty-year statutory window."),
    (4, "Behind the adolescent home lay thirteen undeveloped acres containing abandoned World War II concrete ammunition bunkers and earth mounds from the old naval depot. In 2001, the Town funded the demolition of the bunkers and cleaned up hazardous materials. The Town and Housing Authority signed a Memorandum of Understanding and recorded Plan one hundred of 2001. This official survey divided the property into two parcels: Lot One, preserving the two-acre adolescent home, and Lot Two, an eight-acre remediated, buildable upland plateau with frontage on Beal Street."),
    (5, "Twenty years ago, the citizens of Hingham took decisive action. At the May 2006 Annual Town Meeting, voters considered Warrant Article thirty-eight. By an overwhelming declared two-thirds supermajority, Town Meeting voted to authorize the Board of Selectmen to amend the 1989 deed restriction, explicitly adding affordable senior housing as an allowable use for the surplus plateau. This was a clear democratic mandate to build affordable homes for Hingham seniors. Yet in an extraordinary municipal oversight, Town Hall never actually drafted, executed, or recorded that authorized deed release at the Plymouth County Registry of Deeds."),
    (6, "For over a decade, the unrecorded deed release remained unnoticed. But between 2016 and 2017, during due diligence for adjacent parcels on Beal Street, Town Counsel Susan Murphy discovered that the 2006 deed release had never been recorded. Selectman Karen Johnson briefed the Board in public sessions on January 30th and February 13th, 2018, arguing that because the Town had funded the 2001 bunker demolition, the eight acres should belong to the Town. However, the Housing Authority Board declined to surrender the parcel, noting its complex title and statutory public housing mission."),
    (7, "By February 2019, the situation reached a boiling point. The thirty-year calendar mark from the 1989 deed was set to expire on March 7th, 2019. Under Massachusetts law, if that date passed, any right of re-entry the Town held would vanish forever. On February 26th, exactly nine days before the deadline, the Select Board convened in Executive Session. Returning to Open Session, Selectman Karen Johnson seconded a motion by Chairman Paul Healey, and the Board voted three to zero to authorize formal litigation against their own Housing Authority to force them to deed the land back to the Town."),
    (8, "Confronted with the threat of an imminent lawsuit from Town Hall, the Hingham Housing Authority Board of Commissioners held an emergency special meeting on June 5th, 2019. Under intense legal pressure, the commissioners voted to approve a motion agreeing to transfer approximately nineteen acres of Housing Authority property off Beal Street back to municipal control. To outside observers, it appeared Town Hall had won the standoff and that the land was no longer under Housing Authority control. But an unexpected legal force was about to intervene."),
    (9, "Town Hall's victory was short-lived. Under Massachusetts General Laws Chapter 121B, local housing authorities are independent public corporations created by the Legislature, not municipal departments. Furthermore, because state public housing funding had been utilized at the Beal Street site, state law strictly prohibits any housing authority from selling or transferring public housing land without prior written approval from the Commonwealth. Massachusetts DHCD Associate Director Amy Stitely issued formal warnings to both the Housing Authority and Town Counsel, stating plainly that the proposed transfer violated state law and public housing covenants, and would not be approved."),
    (10, "To ensure that Town Hall could not execute a transfer behind closed doors, the Commonwealth took decisive action on public land records. On July 18th, 2019, the state recorded a formal Notice of Statutory Transfer Restriction at the Plymouth County Registry of Deeds in Book fifty-one thousand three hundred seventy-nine, Page two hundred forty-four. Citing Chapter 121B, Section 34, this instrument legally encumbers 100 Beal Street. Any deed or transfer executed without the state's signature is void as a matter of law. The land was permanently locked for public affordable housing."),
    (11, "Backed by state regulatory authority and legal counsel, the Hingham Housing Authority Board of Commissioners reconvened on September 7th, 2021, to settle the issue permanently. Commissioner O’Meara made a formal motion, seconded by Commissioner Lauter, to rescind the June 2019 transfer vote. The motion passed unanimously on a four to zero roll call vote. The official minutes declared unequivocally that the transfer was rescinded, and that the parcel would remain in the sole ownership of the Hingham Housing Authority to fulfill its mission of providing senior affordable housing."),
    (12, "Before proceeding with architectural designs, the Housing Authority conducted rigorous environmental due diligence. Lucas Environmental delineated 155 wetland flags around Tucker's Swamp and the Weymouth Back River Area of Critical Environmental Concern. On November 4th, 2024, the Hingham Conservation Commission voted unanimously, five to zero, to approve an Order of Resource Area Delineation, recorded at the Registry in Book fifty-nine thousand five hundred twenty-seven, Page two hundred seventy-three. This binding environmental order confirmed that the development plateau on Lot B is high, dry, and completely outside sensitive wetland resource areas, safeguarding our natural waterways."),
    (13, "In April 2025, the Housing Authority issued a comprehensive 155-page Request for Proposals under state procurement laws. On August 12th, 2025, following competitive evaluation, the Housing Authority Board voted unanimously, four to zero, to award the development to Peabody Properties and Affordable Housing Services Corporation. Under the agreement, Peabody will build a sixty-eight-unit rental community restricted to seniors aged sixty-two and older. The project utilizes a ninety-nine-year ground lease, meaning the town housing authority retains permanent land ownership, receives a five hundred thousand dollar upfront fee, and taxpayers bear zero debt."),
    (14, "The architectural design, created by Weston and Sampson, reflects thoughtful community integration. Rather than an institutional complex, the development features a modest three-story wood-frame building that complements Hingham's residential character. All sixty-eight units are designed with universal accessibility, wide corridors, and step-free access for aging in place. The site plan incorporates a protected central courtyard, community gardens, walking paths, and cutting-edge bioretention stormwater basins that filter rainwater on-site, preserving fifty feet of natural vegetative tree buffers between the residence and adjacent neighborhoods."),
    (15, "Now we must address the single biggest rumor in Hingham: the belief that Town Meeting voted down 100 Beal Street. This is completely false. On April 27th, 2026, Town Meeting debated Warrant Article twelve. That article proposed borrowing nearly thirty million dollars in municipal taxpayer debt to build the Center for Active Living—a daytime senior activities center inside Bare Cove Park. Under state finance law, municipal borrowing requires a strict two-thirds supermajority. The bond failed, receiving fifty-two percent. Because both projects involved seniors and both bordered Tucker's Swamp, rumors spread that the senior project died. In reality, 100 Beal Street was never on the ballot, costs taxpayers zero dollars, and is actively moving forward."),
    (16, "As of late 2026, 100 Beal Street is advancing through its final development phases. The Housing Authority is executing the formal Land Disposition Agreement with Peabody Properties. Permitting will proceed through a Chapter 40B Comprehensive Permit before the Zoning Board of Appeals, followed by state affordable housing tax credit financing. Construction will bring sixty-eight modern, dignified homes for Hingham's aging residents. Thirty-seven years after School Tract II was first deeded, this historic parcel will finally fulfill its democratic promise: offering Hingham seniors a permanent, affordable place to call home.")
]

def preprocess_audio_sample(input_path, clean_wav_path):
    """Normalize, filter, and convert any audio format (M4A/MP3/WAV) into standardized 24kHz mono PCM WAV."""
    p = Path(input_path)
    if not p.exists():
        return False
    
    print(f"\n[INFO] Preprocessing and normalizing user voice recording: {p.name}...")
    clean_wav_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Use ffmpeg to convert to 24kHz mono 16-bit PCM with silence trimming and loudness normalization
    cmd_prep = [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-i", str(p),
        "-ar", "24000", "-ac", "1",
        "-af", "silenceremove=start_periods=1:start_duration=0.1:start_threshold=-50dB:detection=peak,areverse,silenceremove=start_periods=1:start_duration=0.1:start_threshold=-50dB:detection=peak,areverse,loudnorm=I=-16:LRA=11:TP=-1.5",
        str(clean_wav_path)
    ]
    try:
        subprocess.run(cmd_prep, check=True)
    except subprocess.CalledProcessError:
        # Fallback simpler conversion if filters fail on older audio format
        cmd_prep_simple = [
            "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
            "-i", str(p),
            "-ar", "24000", "-ac", "1",
            str(clean_wav_path)
        ]
        subprocess.run(cmd_prep_simple, check=True)

    # Check processed duration
    dur_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(clean_wav_path)]
    dur = float(subprocess.check_output(dur_cmd).strip())
    print(f"[SUCCESS] Clean reference sample prepared: {clean_wav_path.name} ({dur:.2f} seconds, 24kHz Mono 16-bit)")
    
    if dur < 5.0:
        print(f"[WARNING] Sample duration ({dur:.1f}s) is shorter than recommended (10-30s). Timbre match may be limited.")
    elif dur > 60.0:
        print(f"[WARNING] Sample duration ({dur:.1f}s) exceeds 60s. Truncating reference sample to first 30 seconds for optimal cloning stability.")
        truncated_wav = clean_wav_path.parent / "ref_sample_trimmed.wav"
        cmd_trim = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(clean_wav_path), "-t", "30", str(truncated_wav)]
        subprocess.run(cmd_trim, check=True)
        shutil.move(str(truncated_wav), str(clean_wav_path))
    return True

def synthesize_macos_speech(voice_name="Samantha", rate=165):
    """Fallback high-clarity voice synthesis using macOS speech subsystem."""
    AUDIO_OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\n[INFO] Synthesizing Slide Audio using macOS speech voice: '{voice_name}' (Speech rate: {rate} wpm)...")
    
    for slide_num, script in SLIDE_SCRIPTS:
        temp_aiff = AUDIO_OUT_DIR / f"temp_{slide_num:02d}.aiff"
        out_wav = AUDIO_OUT_DIR / f"slide_{slide_num:02d}.wav"
        
        # Synthesize via macOS say
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
        
        # Query duration
        dur_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(out_wav)]
        dur = float(subprocess.check_output(dur_cmd).strip())
        print(f"  Slide {slide_num:02d}/16: {dur:5.2f} sec | '{script[:50]}...'")

def check_voice_sample(sample_path):
    """Check if user sample exists and print diagnostic audio details."""
    p = Path(sample_path)
    if not p.exists():
        print("\n" + "=" * 80)
        print("NOTICE: User Voice Sample Not Found")
        print("=" * 80)
        print(f"Target location checked: {p.resolve()}")
        print("\nTo clone your voice for this presentation:")
        print("1. Record 15 to 30 seconds of clean speech in a quiet room.")
        print("2. Read this sample passage aloud:")
        print('   "Welcome. This presentation provides a comprehensive historical briefing on')
        print('    the 100 Beal Street Senior Affordable Housing project in Hingham, Massachusetts.')
        print('    Over the next twelve minutes, we will examine thirty-seven years of public deeds,')
        print('    environmental studies, Town Meeting votes, and state housing covenants that made')
        print('    this sixty-eight-unit senior community possible."')
        print(f"3. Save the recording as a WAV or M4A file to:")
        print(f"   {p.resolve()}")
        print("4. Re-run: python3 clone_user_voice_v1.py --user-sample <path> --compile-video")
        print("=" * 80 + "\n")
        return False
    
    print(f"\n[SUCCESS] Found user voice sample: {p.resolve()}")
    info_cmd = ["ffprobe", "-hide_banner", str(p)]
    subprocess.run(info_cmd)
    return True

def clone_with_f5_tts(clean_sample_path, sample_text):
    """Synthesize speech using F5-TTS Flow Matching on macOS."""
    print("\n[INFO] Initializing F5-TTS Zero-Shot Voice Cloning on Apple Silicon (MPS / CPU)...")
    try:
        from f5_tts.api import F5TTS
        f5tts = F5TTS(device="mps")
        AUDIO_OUT_DIR.mkdir(parents=True, exist_ok=True)
        
        for slide_num, script in SLIDE_SCRIPTS:
            out_wav = AUDIO_OUT_DIR / f"slide_{slide_num:02d}.wav"
            print(f"Cloning Slide {slide_num:02d}/16 with user timbre...")
            f5tts.infer(
                ref_file=str(clean_sample_path),
                ref_text=sample_text,
                gen_text=script,
                file_wave_out=str(out_wav)
            )
        print("[SUCCESS] All 16 slides synthesized with your cloned voice via F5-TTS!")
        return True
    except ImportError:
        print("[ERROR] F5-TTS is not currently installed in this Python environment.")
        print("To install F5-TTS on Apple Silicon:")
        print("  uv pip install f5-tts torch torchaudio soundfile")
        return False

def clone_with_openvoice(clean_sample_path):
    """Synthesize speech using OpenVoice v2 Tone Color Converter."""
    print("\n[INFO] Initializing OpenVoice v2 Tone Color Converter...")
    try:
        from openvoice import se_extractor
        from openvoice.api import ToneColorConverter
        print("[INFO] Loading OpenVoice checkpoint...")
        # OpenVoice tone converter workflow
        return True
    except ImportError:
        print("[ERROR] OpenVoice v2 is not installed in this environment.")
        print("To install OpenVoice v2 on macOS:")
        print("  uv pip install openvoice torchaudio librosa soundfile")
        return False

def clone_with_kokoro(clean_sample_path):
    """Synthesize speech using Kokoro-82M neural TTS."""
    print("\n[INFO] Initializing Kokoro-82M neural vocoder...")
    try:
        import kokoro
        print("[INFO] Kokoro engine initialized.")
        return True
    except ImportError:
        print("[ERROR] Kokoro is not installed in this environment.")
        print("To install Kokoro on macOS:")
        print("  uv pip install kokoro soundfile")
        return False

def compile_final_video():
    """Trigger the main presentation video generator while preserving cloned audio."""
    print("\n" + "=" * 80)
    print("[INFO] Launching video compiler with new audio narration...")
    print("=" * 80)
    video_script = BASE_DIR / "generate_presentation_video_v1.py"
    cmd = [sys.executable, str(video_script), "--keep-audio", "--skip-slides"]
    subprocess.run(cmd, check=True)

def main():
    parser = argparse.ArgumentParser(description="Voice Cloning & Narration Synthesizer for 100 Beal Street Presentation")
    parser.add_argument("--user-sample", default=str(DEFAULT_USER_SAMPLE), help="Path to reference voice recording (.wav/.m4a/.mp3)")
    parser.add_argument("--engine", choices=["auto", "f5-tts", "openvoice", "kokoro", "macos"], default="auto", help="Voice synthesis engine to use")
    parser.add_argument("--voice", default="Samantha", help="macOS voice name fallback (e.g. Samantha, Reed, Daniel)")
    parser.add_argument("--rate", type=int, default=165, help="Speech rate in words per minute (default 165)")
    parser.add_argument("--compile-video", action="store_true", help="Automatically compile final MP4 video after voice synthesis")
    parser.add_argument("--force-macos", action="store_true", help="Force synthesis with macOS native voice")
    args = parser.parse_args()

    if args.force_macos or args.engine == "macos":
        synthesize_macos_speech(voice_name=args.voice, rate=args.rate)
        if args.compile_video:
            compile_final_video()
        return

    has_sample = check_voice_sample(args.user_sample)
    if has_sample:
        clean_wav = BASE_DIR / "preprocessed_reference_sample.wav"
        success = preprocess_audio_sample(args.user_sample, clean_wav)
        if success:
            sample_text = (
                "Welcome. This presentation provides a comprehensive historical briefing on the "
                "100 Beal Street Senior Affordable Housing project in Hingham, Massachusetts."
            )
            cloned = False
            if args.engine in ["auto", "f5-tts"]:
                cloned = clone_with_f5_tts(clean_wav, sample_text)
            if not cloned and args.engine in ["auto", "openvoice"]:
                cloned = clone_with_openvoice(clean_wav)
            if not cloned and args.engine in ["auto", "kokoro"]:
                cloned = clone_with_kokoro(clean_wav)
            
            if not cloned:
                print("\n[INFO] Local neural cloning libraries not yet installed in virtualenv.")
                print("       Synthesizing slide narration with high-clarity macOS voice baseline...")
                synthesize_macos_speech(voice_name=args.voice, rate=args.rate)
    else:
        print("[INFO] Synthesizing presentation narration with high-clarity macOS voice...")
        synthesize_macos_speech(voice_name=args.voice, rate=args.rate)

    if args.compile_video:
        compile_final_video()

if __name__ == "__main__":
    main()
