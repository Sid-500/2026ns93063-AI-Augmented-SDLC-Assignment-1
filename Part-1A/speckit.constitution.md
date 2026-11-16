# Engineering Constitution - Smart Todo CLI

1. Technical Stack: Python 3.10+ using standard library modules for core logic and `pytest` for testing.
2. Storage & Persistence: Store task data strictly in a local JSON file (`tasks.json`). All file read/write operations must explicitly specify UTF-8 encoding (`encoding="utf-8"`).
3. Data Integrity & Validation:
   - Task titles must be non-empty strings after trimming whitespace.
   - Priority levels are strictly restricted to `LOW`, `MEDIUM`, or `HIGH` (defaults to `MEDIUM`).
   - Invalid field values must raise explicit `ValueError` exceptions.
4. Security & Quality Guards:
   - No hardcoded secrets, absolute paths, or unsafe shell execution calls.
   - Code must pass zero-defect static linting (`ruff check`) and SAST security scanning (`bandit`).