from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)

# module-level tasks list
tasks = []


def add_task(title, description, due_date):
    """Add a task after validating input. Returns (True, msg) or (False, msg)."""
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
    except ValueError as e:
        return False, str(e)

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "completed": False,
    }
    tasks.append(task)
    return True, "Task added successfully!"


def mark_task_as_complete(index, tasks=tasks):
    """Mark task at 1-based index as complete. Returns (True,msg) or (False,msg)."""
    try:
        idx = int(index) - 1
    except (TypeError, ValueError):
        return False, "Invalid index."
    if idx < 0 or idx >= len(tasks):
        return False, "Index out of range."
    tasks[idx]["completed"] = True
    return True, "Task marked as complete!"


def view_pending_tasks(tasks=tasks):
    return [t for t in tasks if not t.get("completed", False)]


def calculate_progress(tasks=tasks):
    total = len(tasks)
    if total == 0:
        return 0.0
    completed = sum(1 for t in tasks if t.get("completed", False))
    progress = (completed / total) * 100
    return float(progress)
