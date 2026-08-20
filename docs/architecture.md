\# ProductPilot — Architecture



\## Overview

ProductPilot takes a rough product idea or requirement from a user, uses AI to analyze it, asks clarifying questions where the input is ambiguous or incomplete, and produces a structured product spec the user can act on.



\## Tech Stack



\- \*\*Frontend:\*\* React + Vite + TypeScript

Chosen for fast local dev (Vite's hot reload), type safety on API responses, and a component model that fits a form-heavy, step-based UI (input → clarify → review spec).



\- \*\*Backend:\*\* FastAPI (Python)

Chosen for speed of building REST endpoints, built-in request validation via Pydantic, automatic OpenAPI docs, and being Python-native — same language as the AI/prompt logic.



\- \*\*Database:\*\* PostgreSQL

Relational data (users, submitted requirements, generated specs, skill definitions) benefits from proper schema/constraints rather than a schemaless store. Well-supported, easy to run locally or hosted (e.g. Neon/Supabase) for free during development.



\- \*\*AI:\*\* Google Gemini API

Used for analyzing user input, generating clarifying questions, and producing the final structured spec output.



\## High-Level Flow



1\. \*\*User submits a requirement\*\* (rough, possibly incomplete) via the frontend form.

2\. \*\*Backend receives it\*\* at a REST endpoint, validates the payload with Pydantic.

3\. \*\*Backend calls Gemini\*\* with the requirement, asking it to identify gaps or ambiguities.

4\. \*\*If clarification is needed:\*\* backend returns clarifying questions to the frontend; user answers; answers are sent back and merged into context.

5\. \*\*Once sufficient detail exists:\*\* backend calls Gemini again to generate a structured product spec (e.g. goals, user stories, constraints, open questions).

6\. \*\*Spec is stored in PostgreSQL\*\* and returned to the frontend for the user to review, edit, or export.





User Input → FastAPI (validate) → Gemini (analyze) → \[clarify loop] → Gemini (generate spec) → PostgreSQL (store) → Frontend (display)







\## Why this shape



\- Keeping the clarification step separate from spec generation avoids the AI guessing on incomplete input — better to ask than to hallucinate details into an authoritative-looking spec.

\- FastAPI + Pydantic gives request/response validation almost for free, which matters since

&#x20; the frontend and AI output both need to be trusted at the boundary.

\- Postgres over a NoSQL store because specs, requirements, and skill definitions have clear relationships (a requirement has many revisions, a spec belongs to a requirement) that are awkward to enforce without a schema.



\## Open Questions / Not Yet Decided



\- Auth approach (none yet — single-user local use for now, may add auth later).

\- Whether clarifying-question answers get versioned or just merged into one working draft.

\- Deployment target (not needed until later in the build).



