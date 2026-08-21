import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.5-flash")

ANALYSIS_PROMPT = """You are a product requirements analyst. Given a rough, possibly incomplete
description of a product idea or feature request, analyze it and respond with ONLY a JSON object
(no markdown, no explanation) in exactly this shape:

{{
  "status": "ready" or "needs_clarification",
  "problem": "the core problem being solved, or null if unclear",
  "target_users": "who this is for, or null if unclear",
  "goals": ["list", "of", "goals"],
  "requirements": ["list", "of", "concrete", "requirements"],
  "open_questions": ["list of ambiguities or missing info, if any"]
}}

If the input is too vague to identify a problem, users, or goals, set "status" to
"needs_clarification" and put your questions in "open_questions", leaving other fields as null
or empty lists as appropriate.

User's input:
{requirement_text}
"""

def analyze_requirement(requirement_text: str) -> dict:
    prompt = ANALYSIS_PROMPT.format(requirement_text=requirement_text)

    try:
        response = model.generate_content(prompt)
        raw_text = response.text.strip()

        # Gemini sometimes wraps output in ```json ... ``` even when told not to — strip if present
        if raw_text.startswith("```"):
            raw_text = raw_text.strip("`")
            raw_text = raw_text.replace("json", "", 1).strip()

        return json.loads(raw_text)

    except json.JSONDecodeError:
        return {
            "status": "error",
            "error": "Could not parse AI response as JSON",
            "raw_response": raw_text,
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
        }