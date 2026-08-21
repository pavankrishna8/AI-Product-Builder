# Skill: Product Requirements Analyzer (v1)

## Purpose
Takes a rough, possibly incomplete product idea or requirement from a user and determines whether enough detail exists to identify the problem, users, and goals — producing a structured breakdown if so, or clarifying questions if not.

## When to use this skill
Trigger this skill whenever a user submits free-form text describing a product idea, feature request, or requirement — before attempting to generate a formal spec.

## Implementation
`backend/ai_analyzer.py` — calls Gemini (`gemini-3.6-flash`) with a structured prompt, validated on the way out via a Pydantic model (`AnalysisResult` in `backend/main.py`).

## Inputs
- `requirement_text` (string): raw, unstructured text describing the idea

## Outputs

**If input is sufficient (`status: "ready"`):**
```json
{
  "status": "ready",
  "problem": "the core problem being solved",
  "target_users": "who this is for",
  "goals": ["goal 1", "goal 2"],
  "requirements": ["concrete requirement 1", "concrete requirement 2"],
  "open_questions": ["any smart follow-up questions worth considering"]
}
```

**If input is ambiguous (`status: "needs_clarification"`):**
```json
{
  "status": "needs_clarification",
  "problem": null,
  "target_users": null,
  "goals": [],
  "requirements": [],
  "open_questions": ["clarifying question 1", "clarifying question 2"]
}
```

**If something goes wrong (`status: "error"`):**
```json
{
  "status": "error",
  "error": "description of what failed"
}
```

## Failure Cases (verified in testing)
- Input too vague to identify a problem, users, or goals → correctly returns `needs_clarification`
- AI response doesn't match expected schema → caught by Pydantic validation, returns `error`
- AI response isn't valid JSON at all → caught in `ai_analyzer.py`, returns `error`
- Gemini API call fails (bad key, network, deprecated model) → caught, returns `error`
- Input contains multiple unrelated ideas mixed together — **not yet handled explicitly**, currently gets analyzed as one requirement rather than flagged for splitting (known gap, candidate for v2)

## Version Notes
- v1 (Day 3): real Gemini integration, both `ready` and `needs_clarification` paths verified working, Pydantic schema validation added on the output.
- Notably, `open_questions` in the `ready` case can surface non-obvious follow-ups (e.g. rate limiting, session invalidation) even when the input itself was clear — this is a genuine strength worth preserving in future prompt tweaks, not just a fallback for ambiguity.