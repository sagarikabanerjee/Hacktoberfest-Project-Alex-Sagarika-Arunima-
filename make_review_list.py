"""
make_review_list.py (Person 2)

Runs the test notes through Gemma (Person 1's extract_report) and saves the
results to pending_reports.js. review_form.html loads that file, so every
note shows up in its "Awaiting approval" list.

Run it from the project folder:   python make_review_list.py
Then open (or refresh) review_form.html in your browser.
"""

import json
from datetime import datetime
from pathlib import Path

from script import extract_report

# The same fictional notes as Person 1's test file. Add or change notes here.
NOTES = {
    "clean": "Yesterday around 3pm in the corridor outside Ward B, Mr. Rao slipped on a wet floor. Small cut on his left hand. Nurse Priya saw it happen.",
    "no_injury": "Wet floor near the cafeteria this morning, patient slipped but nobody was hurt.",
    "witness_trap": "Mrs. Iyer fell from her bed in room 12 at 2am. Bruise on her hip.",
    "abbrev": "pt fell bed 7 ~2am no inj, nurse on duty saw",
    "too_short": "Floor wet, pt slipped",
    "has_phone": "Mr. Khan, phone 555-0142, tripped on a loose cable in the lobby at 11am on Oct 20. Sprained ankle. No one saw it.",
    "rambling": "Ugh, long shift today, short two nurses again and the vending machine on 3 ate my money. Anyway, around 4:30pm in the Ward C hallway, an elderly patient, Mrs. Sharma, slipped near the water cooler. Bed 9 in the same ward is waiting on lab results and Mr. Gupta in bed 4 wants a different dinner. Mrs. Sharma hurt her right wrist and the duty doctor was called. Porter Anil was passing by and saw her fall.",
    "two_people": "Mr. Verma, who was visiting his mother, tripped on the stairs near the east entrance at about 6pm. His mother, Mrs. Verma, is a patient in Ward A and wasn't with him. He twisted his knee. Security guard Ravi helped him up and saw it happen.",
    "odd_date": "Last Tuesday morning, Ms. Nair fell in the physio room while getting off the treadmill. She says her ankle hurts. Physio assistant Dev was in the room. Report is being written on 23/10.",
}

results = []
for i, (name, note) in enumerate(NOTES.items(), start=1):
    print(f"[{i}/{len(NOTES)}] Gemma is reading '{name}'...")
    try:
        report = extract_report(note)
        if isinstance(report, str):  # in case extract_report returns JSON text
            report = json.loads(report)
        if not isinstance(report, dict):
            raise ValueError(f"expected a JSON object, got {type(report).__name__}")
        results.append({"name": name, "note": note, "report": report})
        print("      done")
    except Exception as e:  # one bad note shouldn't stop the rest
        print(f"      SKIPPED: {e}")

out = Path(__file__).resolve().parent / "pending_reports.js"
stamp = datetime.now().isoformat(timespec="seconds")
out.write_text(
    "// Made by make_review_list.py. Don't edit by hand: run that script again instead.\n"
    f"window.PENDING_REPORTS_STAMP = {json.dumps(stamp)};\n"
    f"window.PENDING_REPORTS = {json.dumps(results, indent=2, ensure_ascii=False)};\n",
    encoding="utf-8",
)
print(f"\nSaved {len(results)} of {len(NOTES)} reports to {out.name}.")
print("Now open (or refresh) review_form.html in your browser.")
