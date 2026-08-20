\# Skill 1: Product Requirements Analyzer



\## Purpose

Takes a rough, possibly incomplete product idea from the user and determines whether enough detail exists to generate a spec, or whether clarification is needed first.



\## Inputs

\- Raw text describing a product idea or requirement (free-form, unstructured)



\## Outputs

\- If input is sufficient: a structured breakdown (goals, target user, key features)

\- If input is ambiguous or incomplete: a list of clarifying questions to ask the user



\## Failure Cases

\- Input is too vague to analyze at all (e.g. one word, no context)

\- Gemini API call times out or errors

\- Input contains multiple unrelated ideas mixed together (needs splitting, not analyzing as one)

