Hingham Selectmen / Select Board Whisper transcripts
=====================================================

Method
------
Audio was transcribed with faster-whisper model "small.en"
(device=cpu, compute_type=int8).

For the three longer meetings, each source MP3 was split into 3 chunks
(with a ~2 second overlap at the start of part2 and part3) using
split_to_thirds.py. Each chunk was transcribed separately, then stitched
into one file with absolute timestamps:

  part1 absolute = local timestamp
  part2 absolute = (dur/3 - 2) + local
  part3 absolute = (2*dur/3 - 2) + local

Overlap duplicate lines at chunk boundaries were dropped when stitching.

Files
-----
Already complete (full-file pass, do not redo):
  t4P0ZzzO0oY_whisper_transcript.txt   Feb 13, 2018 Selectmen

Stitched from 3 chunks:
  KfiJSICX-mo_whisper_transcript.txt   Jan 30, 2018 Selectmen
  COFl6DmOWAo_whisper_transcript.txt   Oct 29, 2019 Selectmen
  LLJSH5V2ngg_whisper_transcript.txt   Aug 25, 2026 Select Board

Per-chunk intermediates (local timestamps from 00:00 of that chunk):
  {id}_part{1,2,3}of3_whisper.txt

Status sidecars:
  {id}_whisper_status.txt

Related (Gemini)
----------------
A Gemini full transcript exists for a different meeting:
  /workspace/beal-transcripts/gemini-out/iSOkQlHX-5s_GeminiPro_transcript.txt
Gemini struggled / failed on some long audio; Whisper was used for these.

Notes
-----
- No speaker diarization in this pass (no Speaker 1/2/3 labels).
- Tiny adjacent segments within a chunk are merged (gap <1s); a new
  timestamp is emitted at least every ~20–30s or when pause >~1.5s.
- t4P0ZzzO0oY was completed earlier as a full-file (internally chunked)
  Whisper pass and was not re-run with the 3-chunk method.
