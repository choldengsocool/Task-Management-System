from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
    tasks,
)


def print_tasks(all_tasks):
    if not all_tasks:
        print("No tasks available.")
        return
    for i, t in enumerate(all_tasks, start=1):
        status = "✓" if t.get("completed") else " "
        print(f"{i}. [{status}] {t['title']} (Due: {t['due_date']})")


def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input()
            description = input()
            due_date = input()
            ok, msg = add_task(title, description, due_date)
            print(msg)

        elif choice == "2":
            # show tasks then mark
            print_tasks(tasks)
            idx = input()
            ok, msg = mark_task_as_complete(idx)
            print(msg)

        elif choice == "3":
            pending = view_pending_tasks()
            if not pending:
                print("No pending tasks.")
            else:
                print_tasks(pending)

        elif choice == "4":
            progress = calculate_progress()
            print(progress)

        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
