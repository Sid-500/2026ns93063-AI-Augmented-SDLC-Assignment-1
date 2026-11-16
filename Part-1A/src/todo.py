import json
import os
import uuid
from datetime import datetime

DATA_FILE = "tasks.json"


class TaskManager:

  def __init__(self, storage_path: str = DATA_FILE):
    self.storage_path = storage_path
    self.tasks = self._load()

  def _load(self) -> list:
    if not os.path.exists(self.storage_path):
      return []
    with open(self.storage_path, "r", encoding="utf-8") as f:
      return json.load(f)

  def _save(self) -> None:
    with open(self.storage_path, "w", encoding="utf-8") as f:
      json.dump(self.tasks, f, indent=2)

  def add_task(
      self, title: str, priority: str = "MEDIUM", tag: str = "general"
  ) -> dict:
    if not title or not isinstance(title, str) or not title.strip():
      raise ValueError("Title must be a non-empty string.")
    if priority.upper() not in ["LOW", "MEDIUM", "HIGH"]:
      raise ValueError("Priority must be LOW, MEDIUM, or HIGH.")

    task = {
        "id": str(uuid.uuid4())[:8],
        "title": title.strip(),
        "priority": priority.upper(),
        "tag": tag.lower(),
        "status": "PENDING",
        "created_at": datetime.now().isoformat(),
    }
    self.tasks.append(task)
    self._save()
    return task

  def list_tasks(self, tag: str | None = None) -> list:
    if tag:
      return [t for t in self.tasks if t["tag"] == tag.lower()]
    return self.tasks