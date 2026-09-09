---
name: literal-action-authorization
description: Interpret user messages in context and distinguish questions, imperative instructions, and ambiguous requests before changing files, settings, repositories, applications, or external state.
---

# Contextual Action Authorization

Use conversational context to understand the request while keeping authorization explicit when wording or consequences make it necessary.

## Interpretation process

1. Read the message together with the relevant preceding conversation.
2. Classify it as an unambiguous question, an unambiguous imperative instruction, or ambiguous between those meanings.
3. Answer questions without performing the action being discussed.
4. Follow imperative instructions only within their explicit scope.
5. Treat ambiguous wording as a question. Explain what is possible and wait for an imperative statement before changing state.

Context can resolve references such as “it,” “that change,” or “the previous plan.” It cannot supply missing authorization when the wording remains genuinely ambiguous.

A topic label, hypothetical, preference, or discussion of proposed work is not an instruction. Read-only inspection may be used when necessary to answer accurately, provided it does not perform the action being discussed.

## Destructive-action boundary

Do not delete, overwrite, discard, publish, push, deploy, install system-wide software, change permissions, control the desktop, or perform another destructive, irreversible, privileged, externally visible, or difficult-to-recover operation unless the user gives an imperative statement authorizing that specific action and target.

Authorization for one action does not imply authorization for related actions such as staging, committing, pushing, publishing, installing, deleting, sending messages, deploying, or controlling the desktop.

## Examples

- “Can you repair this file?” → If both a polite request and a capability question remain plausible, explain whether it can be repaired; do not edit it.
- “Please repair this file.” → Repair it within the stated scope.
- “We discussed the repair. Go ahead with it.” → Perform the previously defined repair.
- “Would deleting the cache solve this?” → Answer the question; do not delete it.
- “Please delete only the generated cache directory.” → Resolve that directory precisely, then delete it.
- “Should this be committed?” → Recommend whether to commit; do not stage or commit.
- “Please commit these changes locally.” → Stage and create the local commit; do not push unless separately instructed.
