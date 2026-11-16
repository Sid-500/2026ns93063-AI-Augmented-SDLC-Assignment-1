# Feature Specification - Smart Todo CLI

## User Stories & Acceptance Criteria

- **US-01: Create Task**
  - **AC-1.1:** Given a non-empty title string, when `add_task(title, priority, tag)` is called, the system creates a task record with a unique 8-character ID, ISO 8601 creation timestamp, and `PENDING` status.
  - **AC-1.2:** If priority is omitted, it defaults to `MEDIUM`.
  - **AC-1.3:** If priority is not `LOW`, `MEDIUM`, or `HIGH`, the system raises a `ValueError`.

- **US-02: Status Lifecycle & Filtering**
  - **AC-2.1:** Status transitions must strictly follow `PENDING` -> `IN_PROGRESS` -> `COMPLETED`.
  - **AC-2.2:** `list_tasks(tag="work")` returns only task items matching the specified tag case-insensitively.

- **US-03: Persistence & File Safety**
  - **AC-3.1:** All task modifications immediately save to `tasks.json` using UTF-8 encoding.
  - **AC-3.2:** If `tasks.json` does not exist on startup, it initializes an empty array without throwing an exception.