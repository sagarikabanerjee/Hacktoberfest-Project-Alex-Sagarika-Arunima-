from script import extract_report
import json

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

for name, note in NOTES.items():
    print("=" * 40, name, "=" * 40)
    print(json.dumps(extract_report(note), indent=2))