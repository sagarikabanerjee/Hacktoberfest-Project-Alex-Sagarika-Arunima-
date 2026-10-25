from dotenv import load_dotenv
from google import genai
import json, os, re, datetime

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = "gemma-4-26b-a4b-it"  # same model that worked in start.py

PROMPT = """You extract facts from a hospital staff note into an incident report.

Rules:
- Return ONLY valid JSON. No explanation, no markdown.
- Use exactly the schema below.
- If the note does not clearly state a field, use null. NEVER guess or invent.
- anyone_injured and were_there_witnesses must be true, false, or null.
- Always set "missing_info" to [].
- Only use information explicitly written in the note.
- If the note gives a date or time in relative terms (e.g. "yesterday", "this morning"), copy it exactly as written into the date or time field.
- If the note does not say whether anyone was injured or whether there were witnesses, use null, not false.
- If anyone_injured is false, set injuries.description to null. If were_there_witnesses is false, set witnesses.details to null.
- In "description", write 1-2 complete, formal sentences. Expand abbreviations (pt = patient) and fix grammar, but do not add any facts, causes, or details that are not in the note. Do not repeat injury or witness information in the description.
- Ignore irrelevant details such as someone complaining about a hard shift, having a long day, etc. This is an incident report: the output you provide should strictly be what you'd see on an official incident report file

Schema:
{schema}

Note:
\"\"\"{note}\"\"\"
"""

SCHEMA = """{
  "date_of_report": null,
  "person_involved": {"full_name": null, "address": null, "identification_type": null,
                      "identification_number": null, "phone": null, "email": null},
  "incident": {"date": null, "time": null, "location": null, "description": null},
  "injuries": {"anyone_injured": null, "description": null},
  "witnesses": {"were_there_witnesses": null, "details": null},
  "missing_info": []
}"""

def parse_json(text):
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        return None
    try:
        return json.loads(text[start:end + 1])
    except json.JSONDecodeError:
        return None

TEMPLATE = json.loads(SCHEMA)

def clean_value(v):
    if isinstance(v, str) and v.strip().lower() in ("", "null", "none", "n/a", "unknown", "not stated"):
        return None
    return v.strip() if isinstance(v, str) else v

def to_bool(v):
    if isinstance(v, bool):
        return v
    if isinstance(v, str) and v.strip().lower() in ("true", "yes"):
        return True
    if isinstance(v, str) and v.strip().lower() in ("false", "no"):
        return False
    return None

def normalize(data):
    """Guarantee every key exists; drop unexpected ones."""
    out = {}
    for key, default in TEMPLATE.items():
        val = data.get(key) if isinstance(data, dict) else None
        if isinstance(default, dict):
            val = val if isinstance(val, dict) else {}
            out[key] = {k: clean_value(val.get(k)) for k in default}
        elif key == "missing_info":
            out[key] = []
        else:
            out[key] = clean_value(val)

    out["injuries"]["anyone_injured"] = to_bool(out["injuries"]["anyone_injured"])
    out["witnesses"]["were_there_witnesses"] = to_bool(out["witnesses"]["were_there_witnesses"])
    out["date_of_report"] = datetime.date.today().isoformat()
    out["missing_info"] = find_missing(out)
    return out

def find_missing(report):
    missing = []
    for key, val in report.items():
        if key == "missing_info":
            continue
        if isinstance(val, dict):
            missing += [f"{key}.{k}" for k, v in val.items() if v is None]
        elif val is None:
            missing.append(key)

    if report["injuries"]["anyone_injured"] is False and "injuries.description" in missing:
        missing.remove("injuries.description")
    if report["witnesses"]["were_there_witnesses"] is False and "witnesses.details" in missing:
        missing.remove("witnesses.details")
    return missing
    

def extract_report(note_text, retries=2):
    prompt = PROMPT.format(schema=SCHEMA, note=note_text)
    for _ in range(retries + 1):
        try:
            resp = client.models.generate_content(model=MODEL, contents=prompt)
        except Exception as e:
            print("API error:", e)
            continue
        parsed = parse_json(resp.text or "")
        if parsed is not None:
            return normalize(parsed)
    return None

if __name__ == "__main__":
    note = ("Yesterday around 3pm in the corridor outside Ward B, an elderly patient, "
            "Mr. Rao, slipped on a wet floor. Small cut on his left hand. Nurse Priya saw it happen.")
    print(json.dumps(extract_report(note), indent=2))