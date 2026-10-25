// Made by make_review_list.py. Don't edit by hand: run that script again instead.
window.PENDING_REPORTS_STAMP = "2026-10-25T16:16:56";
window.PENDING_REPORTS = [
  {
    "name": "clean",
    "note": "Yesterday around 3pm in the corridor outside Ward B, Mr. Rao slipped on a wet floor. Small cut on his left hand. Nurse Priya saw it happen.",
    "report": {
      "date_of_report": "2026-10-25",
      "person_involved": {
        "full_name": "Mr. Rao",
        "address": null,
        "identification_type": null,
        "identification_number": null,
        "phone": null,
        "email": null
      },
      "incident": {
        "date": "Yesterday",
        "time": "around 3pm",
        "location": "the corridor outside Ward B",
        "description": "Mr. Rao slipped on a wet floor."
      },
      "injuries": {
        "anyone_injured": true,
        "description": "Small cut on his left hand."
      },
      "witnesses": {
        "were_there_witnesses": true,
        "details": "Nurse Priya"
      },
      "missing_info": [
        "person_involved.address",
        "person_involved.identification_type",
        "person_involved.identification_number",
        "person_involved.phone",
        "person_involved.email"
      ]
    }
  },
  {
    "name": "no_injury",
    "note": "Wet floor near the cafeteria this morning, patient slipped but nobody was hurt.",
    "report": {
      "date_of_report": "2026-10-25",
      "person_involved": {
        "full_name": null,
        "address": null,
        "identification_type": null,
        "identification_number": null,
        "phone": null,
        "email": null
      },
      "incident": {
        "date": null,
        "time": "this morning",
        "location": "near the cafeteria",
        "description": "A patient slipped on a wet floor near the cafeteria."
      },
      "injuries": {
        "anyone_injured": false,
        "description": null
      },
      "witnesses": {
        "were_there_witnesses": null,
        "details": null
      },
      "missing_info": [
        "person_involved.full_name",
        "person_involved.address",
        "person_involved.identification_type",
        "person_involved.identification_number",
        "person_involved.phone",
        "person_involved.email",
        "incident.date",
        "witnesses.were_there_witnesses",
        "witnesses.details"
      ]
    }
  },
  {
    "name": "witness_trap",
    "note": "Mrs. Iyer fell from her bed in room 12 at 2am. Bruise on her hip.",
    "report": {
      "date_of_report": "2026-10-25",
      "person_involved": {
        "full_name": "Mrs. Iyer",
        "address": null,
        "identification_type": null,
        "identification_number": null,
        "phone": null,
        "email": null
      },
      "incident": {
        "date": null,
        "time": "2am",
        "location": "room 12",
        "description": "Mrs. Iyer fell from her bed in room 12 at 2am."
      },
      "injuries": {
        "anyone_injured": true,
        "description": "Bruise on her hip."
      },
      "witnesses": {
        "were_there_witnesses": null,
        "details": null
      },
      "missing_info": [
        "person_involved.address",
        "person_involved.identification_type",
        "person_involved.identification_number",
        "person_involved.phone",
        "person_involved.email",
        "incident.date",
        "witnesses.were_there_witnesses",
        "witnesses.details"
      ]
    }
  },
  {
    "name": "abbrev",
    "note": "pt fell bed 7 ~2am no inj, nurse on duty saw",
    "report": {
      "date_of_report": "2026-10-25",
      "person_involved": {
        "full_name": null,
        "address": null,
        "identification_type": null,
        "identification_number": null,
        "phone": null,
        "email": null
      },
      "incident": {
        "date": null,
        "time": "~2am",
        "location": "bed 7",
        "description": "The patient fell from bed 7."
      },
      "injuries": {
        "anyone_injured": false,
        "description": null
      },
      "witnesses": {
        "were_there_witnesses": true,
        "details": "The nurse on duty saw the incident."
      },
      "missing_info": [
        "person_involved.full_name",
        "person_involved.address",
        "person_involved.identification_type",
        "person_involved.identification_number",
        "person_involved.phone",
        "person_involved.email",
        "incident.date"
      ]
    }
  },
  {
    "name": "too_short",
    "note": "Floor wet, pt slipped",
    "report": {
      "date_of_report": "2026-10-25",
      "person_involved": {
        "full_name": null,
        "address": null,
        "identification_type": null,
        "identification_number": null,
        "phone": null,
        "email": null
      },
      "incident": {
        "date": null,
        "time": null,
        "location": "Floor",
        "description": "The patient slipped on a wet floor."
      },
      "injuries": {
        "anyone_injured": null,
        "description": null
      },
      "witnesses": {
        "were_there_witnesses": null,
        "details": null
      },
      "missing_info": [
        "person_involved.full_name",
        "person_involved.address",
        "person_involved.identification_type",
        "person_involved.identification_number",
        "person_involved.phone",
        "person_involved.email",
        "incident.date",
        "incident.time",
        "injuries.anyone_injured",
        "injuries.description",
        "witnesses.were_there_witnesses",
        "witnesses.details"
      ]
    }
  },
  {
    "name": "has_phone",
    "note": "Mr. Khan, phone 555-0142, tripped on a loose cable in the lobby at 11am on Oct 20. Sprained ankle. No one saw it.",
    "report": {
      "date_of_report": "2026-10-25",
      "person_involved": {
        "full_name": "Mr. Khan",
        "address": null,
        "identification_type": null,
        "identification_number": null,
        "phone": "555-0142",
        "email": null
      },
      "incident": {
        "date": "Oct 20",
        "time": "11am",
        "location": "lobby",
        "description": "Mr. Khan tripped on a loose cable in the lobby."
      },
      "injuries": {
        "anyone_injured": true,
        "description": "Sprained ankle"
      },
      "witnesses": {
        "were_there_witnesses": false,
        "details": null
      },
      "missing_info": [
        "person_involved.address",
        "person_involved.identification_type",
        "person_involved.identification_number",
        "person_involved.email"
      ]
    }
  },
  {
    "name": "rambling",
    "note": "Ugh, long shift today, short two nurses again and the vending machine on 3 ate my money. Anyway, around 4:30pm in the Ward C hallway, an elderly patient, Mrs. Sharma, slipped near the water cooler. Bed 9 in the same ward is waiting on lab results and Mr. Gupta in bed 4 wants a different dinner. Mrs. Sharma hurt her right wrist and the duty doctor was called. Porter Anil was passing by and saw her fall.",
    "report": {
      "date_of_report": "2026-10-25",
      "person_involved": {
        "full_name": "Mrs. Sharma",
        "address": null,
        "identification_type": null,
        "identification_number": null,
        "phone": null,
        "email": null
      },
      "incident": {
        "date": null,
        "time": "around 4:30pm",
        "location": "Ward C hallway",
        "description": "Mrs. Sharma slipped near the water cooler."
      },
      "injuries": {
        "anyone_injured": true,
        "description": "right wrist"
      },
      "witnesses": {
        "were_there_witnesses": true,
        "details": "Porter Anil"
      },
      "missing_info": [
        "person_involved.address",
        "person_involved.identification_type",
        "person_involved.identification_number",
        "person_involved.phone",
        "person_involved.email",
        "incident.date"
      ]
    }
  },
  {
    "name": "two_people",
    "note": "Mr. Verma, who was visiting his mother, tripped on the stairs near the east entrance at about 6pm. His mother, Mrs. Verma, is a patient in Ward A and wasn't with him. He twisted his knee. Security guard Ravi helped him up and saw it happen.",
    "report": {
      "date_of_report": "2026-10-25",
      "person_involved": {
        "full_name": "Mr. Verma",
        "address": null,
        "identification_type": null,
        "identification_number": null,
        "phone": null,
        "email": null
      },
      "incident": {
        "date": null,
        "time": "about 6pm",
        "location": "the stairs near the east entrance",
        "description": "Mr. Verma tripped on the stairs near the east entrance."
      },
      "injuries": {
        "anyone_injured": true,
        "description": "He twisted his knee."
      },
      "witnesses": {
        "were_there_witnesses": true,
        "details": "Security guard Ravi saw it happen."
      },
      "missing_info": [
        "person_involved.address",
        "person_involved.identification_type",
        "person_involved.identification_number",
        "person_involved.phone",
        "person_involved.email",
        "incident.date"
      ]
    }
  },
  {
    "name": "odd_date",
    "note": "Last Tuesday morning, Ms. Nair fell in the physio room while getting off the treadmill. She says her ankle hurts. Physio assistant Dev was in the room. Report is being written on 23/10.",
    "report": {
      "date_of_report": "2026-10-25",
      "person_involved": {
        "full_name": "Ms. Nair",
        "address": null,
        "identification_type": null,
        "identification_number": null,
        "phone": null,
        "email": null
      },
      "incident": {
        "date": "Last Tuesday",
        "time": "morning",
        "location": "physiotherapy room",
        "description": "Ms. Nair fell in the physiotherapy room while getting off the treadmill."
      },
      "injuries": {
        "anyone_injured": true,
        "description": "The patient reports that her ankle hurts."
      },
      "witnesses": {
        "were_there_witnesses": true,
        "details": "Physiotherapy assistant Dev was in the room."
      },
      "missing_info": [
        "person_involved.address",
        "person_involved.identification_type",
        "person_involved.identification_number",
        "person_involved.phone",
        "person_involved.email"
      ]
    }
  }
];
