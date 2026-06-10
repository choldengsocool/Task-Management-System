from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str):
        raise ValueError("Title must be a string.")
    # check using len()
    if len(title.strip()) == 0:
        raise ValueError("Title cannot be empty.")
    if len(title) > 100:
        raise ValueError("Title must be 100 characters or fewer.")
    return True


def validate_task_description(description):
    if not isinstance(description, str):
        raise ValueError("Description must be a string.")
    if len(description.strip()) == 0:
        raise ValueError("Description cannot be empty.")
    if len(description) > 500:
        raise ValueError("Description must be 500 characters or fewer.")
    return True


def validate_due_date(due_date):
    if not isinstance(due_date, str):
        raise ValueError("Due date must be a string in YYYY-MM-DD format.")
    try:
        parsed = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")
    today = datetime.today().date()
    if parsed < today:
        raise ValueError("Due date cannot be in the past.")
    return True
