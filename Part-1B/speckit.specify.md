# Feature Specification - Natural-Language Reminder Agent

## Schema Contract
Output JSON format:
```json
{
  "intent": "CREATE | SNOOZE | CANCEL | QUERY | UNKNOWN",
  "title": "string | null",
  "datetime": "string | null",
  "requires_clarification": "boolean",
  "clarification_prompt": "string | null"
}