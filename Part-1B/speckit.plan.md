# Technical Plan - Natural-Language Reminder Agent

## 1. System Architecture
- Application Module: `src/agent.py` implementing intent parsing and ambiguity detection.
- Benchmark Dataset: `evals/dataset.json` containing 15 test cases (normal, edge, ambiguous, missing info, malformed).
- Verification Harness: `.harness/eval_runner.py` executing a 3-layer evaluation pipeline:
  - **Layer 1:** JSON Schema Structural Validation
  - **Layer 2:** Rule/Invariant Validation (Clarification triggering)
  - **Layer 3:** Quality / Intent Heuristic Match

## 2. Evaluation Score Threshold
- Minimum Pass Gate: **85.0%**