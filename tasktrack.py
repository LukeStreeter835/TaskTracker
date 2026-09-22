"""A command-line task manager created for CPS 310.

Author: Luke Streeter
Course: CPS 310
"""


def display_menu():
    """Display the available TaskTrack menu options."""
    print("\nTaskTrack Menu")
    print("1. View tasks")
    print("2. Add task")
    print("3. Exit")


def add_task(tasks):
    """Prompt the user for a task and add it to the task list."""
    #TODO: Complete this function in Step 8.
    task = input("Enter a new Task: ")
    tasks.append(task)
    print("Task added successfully")


def view_tasks(tasks):
    """Display all tasks currently stored in the task list."""
    if not tasks:
        """If there are no tasks, go back to main loop"""

        print("There are no tasks in list, please add some tasks")
        return

    print("\nTasks:")

    """run through array and print all tasks"""
    for number, task in enumerate(tasks, start=1):
         print(f"Task #{number}: {tasks[number - 1]}")

    


def main():
    """Run the TaskTrack menu until the user chooses to exit."""
    tasks = []

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()