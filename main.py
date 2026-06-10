from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress,
    save_tasks,
    load_tasks,
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
    # attempt to load existing tasks from tasks.json
    load_tasks()

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            ok, msg = add_task(title, description, due_date)
            print(msg)
            if ok:
                save_tasks()

        elif choice == "2":
            print("All tasks:")
            print_tasks(tasks)
            idx = input("Enter task number to mark complete: ")
            ok, msg = mark_task_as_complete(idx, tasks=tasks)
            print(msg)
            if ok:
                save_tasks()

        elif choice == "3":
            pending = view_pending_tasks(tasks=tasks)
            if not pending:
                print("No pending tasks. Good job!")
            else:
                print("Pending tasks:")
                print_tasks(pending)

        elif choice == "4":
            progress = calculate_progress(tasks=tasks)
            print(f"Progress: {progress}% complete")

        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
