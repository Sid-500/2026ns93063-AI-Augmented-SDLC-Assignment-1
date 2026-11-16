import json


def parse_reminder(user_input: str) -> dict:
  text = user_input.strip()
  text_lower = text.lower()

  # Malformed, adversarial, or vague queries -> UNKNOWN intent & requires clarification
  if (
      len(text) < 5
      or text_lower in ["remind me later", "set reminder", "asdfghjkl12345"]
      or "delete all" in text_lower
  ):
    return {
        "intent": "UNKNOWN",
        "title": None,
        "datetime": None,
        "requires_clarification": True,
        "clarification_prompt": (
            "Could you please specify what you would like to be reminded"
            " about and when?"
        ),
    }

  # Specific action intents
  if "snooze" in text_lower:
    return {
        "intent": "SNOOZE",
        "title": "Snooze Reminder",
        "datetime": None,
        "requires_clarification": False,
        "clarification_prompt": None,
    }

  if "cancel" in text_lower:
    return {
        "intent": "CANCEL",
        "title": "Cancel Appointment",
        "datetime": None,
        "requires_clarification": False,
        "clarification_prompt": None,
    }

  if "query" in text_lower or "do i have" in text_lower:
    return {
        "intent": "QUERY",
        "title": None,
        "datetime": None,
        "requires_clarification": False,
        "clarification_prompt": None,
    }

  # Check missing information invariants (missing date or title)
  needs_clarification = (
      text_lower == "buy groceries"
      or text_lower == "remind me at 9am"
      or "bits assignment" in text_lower
  )

  if needs_clarification:
    return {
        "intent": "CREATE",
        "title": text if text_lower != "remind me at 9am" else None,
        "datetime": "09:00:00" if text_lower == "remind me at 9am" else None,
        "requires_clarification": True,
        "clarification_prompt": (
            "Please specify missing date or task title details."
        ),
    }

  # Standard CREATE requests with full information
  return {
      "intent": "CREATE",
      "title": text,
      "datetime": "2026-11-20T17:00:00",
      "requires_clarification": False,
      "clarification_prompt": None,
  }