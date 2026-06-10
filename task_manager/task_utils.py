from datetime import datetime
import json
from pathlib import Path
from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)

# Define tasks list
tasks = []

def add_task(title, description, due_date):
    ok, msg = validate_task_title(title)
    if not ok:
        return False, msg
    ok, msg = validate_task_description(description)
    if not ok:
        return False, msg
    ok, msg = validate_due_date(due_date)
    if not ok:
        return False, msg

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "completed": False,
    }
    tasks.append(task)
    return True, "Task added successfully."


def save_tasks(file_path="tasks.json", tasks=tasks):
    """Save tasks to a JSON file (default: tasks.json)."""
    p = Path(file_path)
    with p.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)
    return True


def load_tasks(file_path="tasks.json", tasks=tasks):
    """Load tasks from a JSON file into the module-level tasks list."""
    p = Path(file_path)
    if not p.exists():
        return False, "File not found."
    try:
        with p.open("r", encoding="utf-8") as f:
            data = json.load(f)
        # Validate structure minimally
        if not isinstance(data, list):
            return False, "Invalid file format."
        tasks.clear()
        for item in data:
            # Basic shape check
            if not isinstance(item, dict):
                continue
            tasks.append(item)
        return True, "Loaded tasks."
    except Exception as e:
        return False, str(e)

def mark_task_as_complete(index, tasks=tasks):
    try:
        idx = int(index) - 1
    except (TypeError, ValueError):
        return False, "Invalid index. Please enter a number."
    if idx < 0 or idx >= len(tasks):
        return False, "Index out of range."
    tasks[idx]["completed"] = True
    return True, "Task marked as complete."

def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t.get("completed", False)]
    return pending

def calculate_progress(tasks=tasks):
    total = len(tasks)
    if total == 0:
        return 0
    completed = sum(1 for t in tasks if t.get("completed", False))
    progress = int((completed / total) * 100)
    return progress
