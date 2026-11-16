# Engineering Constitution - Natural-Language Reminder Agent

1. Non-Deterministic Evaluation: Evaluate LLM/AI output via a multi-layered verification pipeline rather than exact string comparison.
2. Output Contract: Every AI response must strictly conform to a structured JSON schema contract containing intent, title, datetime, and clarification fields.
3. Behavioral Invariants:
   - If mandatory information (title or datetime) is missing or ambiguous, `requires_clarification` MUST be set to `true`.
   - Datetime strings, when present, must conform to ISO 8601 formatting.
4. Evaluation Threshold: Aggregate score across the benchmark dataset must equal or exceed **85.0%**.