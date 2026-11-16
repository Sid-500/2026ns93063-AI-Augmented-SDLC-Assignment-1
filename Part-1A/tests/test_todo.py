import pytest
from src.todo import TaskManager


def test_add_task_success(tmp_path):
  db = tmp_path / "test_tasks.json"
  tm = TaskManager(storage_path=str(db))
  task = tm.add_task("Buy Groceries", "HIGH", "shopping")
  assert task["title"] == "Buy Groceries"
  assert task["priority"] == "HIGH"
  assert task["status"] == "PENDING"


def test_invalid_priority_raises_error(tmp_path):
  db = tmp_path / "test_tasks.json"
  tm = TaskManager(storage_path=str(db))
  with pytest.raises(ValueError):
    tm.add_task("Task", "URGENT")


def test_list_tasks_filtering(tmp_path):
  db = tmp_path / "test_tasks.json"
  tm = TaskManager(storage_path=str(db))
  tm.add_task("Fix Bug", "HIGH", "work")
  tm.add_task("Buy Milk", "LOW", "personal")
  work_tasks = tm.list_tasks(tag="WORK")
  assert len(work_tasks) == 1
  assert work_tasks[0]["title"] == "Fix Bug"