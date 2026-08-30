# Codex Instructions

## Project documentation

Use when present and relevant:

- `Requirements.md` — requirements and constraints
- `Design.md` — architecture and open design questions
- `Dependencies.md` — external baselines and versions
- `DECISIONS/` — engineering decisions
- `CONTRIBUTING.md` — repository practices
- `README.md` — project overview

## Working rules

- Do not silently change requirements or established design decisions.
- Identify contradictions, missing requirements, important assumptions, and materially significant alternatives.
- Do not invent missing information; identify unresolved gaps.
- Prefer the simplest implementation that satisfies documented requirements.
- Do not assume conventional PC-floppy geometry, signaling, or Windows drive behavior where documented as programmable or unresolved.
- Keep host-command semantics independent of temporary development transports where practical.
- Verify external versions, electrical limits, hardware capabilities, PCIe requirements, and driver behavior; otherwise mark them unresolved.
- Keep documentation synchronized with implementation.
- Record significant architectural choices or reversals in `DECISIONS/`.
- Avoid unrelated changes.

## Verification

- Run applicable tests, simulations, formatters, and linters.
- Report what was and was not verified.
- Do not claim hardware verification without hardware testing or authoritative evidence.

## Scope

Use the established repository structure. Add subsystem `AGENTS.md` files only for narrower-scope instructions.
