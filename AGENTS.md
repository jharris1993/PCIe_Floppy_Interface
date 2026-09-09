# Codex Instructions

## Project documentation

Use when present and relevant:

- `Requirements.md` — authoritative project requirements
- `Design.md` — current, non-authoritative design and open design questions
- `Dependencies.md` — external baselines and versions
- `Project_Decisions/` — non-authoritative engineering notebook
- `CONTRIBUTING.md` — repository practices
- `README.md` — project overview

When researching technical questions, consult the applicable `Reference_*` directories.

Reference material is not authoritative project specification merely because it is present in the repository.

## Working rules

- Do not silently change requirements or established design decisions.
- Identify contradictions, missing requirements, important assumptions, and materially significant alternatives.
- Do not invent missing information; identify unresolved gaps.
- Prefer the simplest implementation that satisfies documented requirements.
- Do not assume conventional PC-floppy geometry, signaling, or Windows drive behavior where documented as programmable or unresolved.
- Keep host-command semantics independent of temporary development transports where practical.
- Verify external versions, electrical limits, hardware capabilities, PCIe requirements, and driver behavior; otherwise mark them unresolved.
- Keep documentation synchronized with implementation.
- Record significant architectural choices or reversals in `Project_Decisions/`.
- When a project choice changes the current requirements or design, update `Requirements.md` or `Design.md`, as applicable.
- Avoid unrelated changes.

## Action authorization

Interpret each message in its conversational context.

- A clear imperative statement authorizes the stated action within its stated scope. Examples include “Please create…”, “Edit…”, “Run…”, “Install…”, “Delete…”, “Commit…”, “Go ahead…”, and “Continue with…”.
- A clear question requests information and does not authorize the action being discussed.
- If a message can reasonably be interpreted as either a question or an instruction, treat it as a question. Explain what is possible and wait for an imperative statement before changing state.
- Context may clarify references, scope, and whether wording is unambiguous. Context must not convert genuinely ambiguous wording into authorization.
- A topic label, hypothetical discussion, statement of preference, or request to explain what would be required does not authorize the described action.
- Read-only inspection needed to answer accurately is allowed when it does not perform the action being discussed.
- Never perform a destructive, irreversible, externally visible, privileged, or difficult-to-recover action without an imperative statement authorizing that specific action.
- Authorization for one action does not imply authorization for related actions such as staging, committing, pushing, publishing, installing, deleting, sending messages, deploying, or controlling the desktop.

## Verification

- Run applicable tests, simulations, formatters, and linters.
- Report what was and was not verified.
- Do not claim hardware verification without hardware testing or authoritative evidence.

## Scope

Use the established repository structure. Add subsystem `AGENTS.md` files only for narrower-scope instructions.
