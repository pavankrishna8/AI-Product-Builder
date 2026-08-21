\# Skill: Product Requirements Analyzer



\## Purpose

Takes a rough, possibly incomplete product idea or requirement from a user and determines whether enough detail exists to generate a structured spec, or whether clarification is needed first.



\## When to use this skill

Trigger this skill whenever a user submits free-form text describing a product idea, feature request, or requirement — before attempting to generate a formal spec.



\## Inputs

\- `requirement\_text` (string): raw, unstructured text describing the idea



\## Outputs

One of two shapes:



\*\*If input is sufficient:\*\*

```json

{

&#x20; "status": "ready",

&#x20; "breakdown": {

&#x20;   "goal": "...",

&#x20;   "target\_user": "...",

&#x20;   "key\_features": \["...", "..."]

&#x20; }

}

```



\*\*If input is ambiguous or incomplete:\*\*

```json

{

&#x20; "status": "needs\_clarification",

&#x20; "questions": \["...", "..."]

}

```



\## Failure Cases

\- Input is too vague to analyze at all (e.g. a single word, no context)

\- The underlying AI call times out or errors

\- Input contains multiple unrelated ideas mixed together (should be flagged for splitting, not analyzed as a single requirement)

