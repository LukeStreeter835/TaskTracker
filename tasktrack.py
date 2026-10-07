"""A command-line task manager created for CPS 310.

Author: Luke Streeter
Course: CPS 310
"""

TASK_FILE = "Tasks.txt"

def display_menu():
    """Display the available TaskTrack menu options."""
    print("\nTaskTrack Menu")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove Task")
    print("4. Exit")


def add_task(tasks):
    """Prompt the user for a task and add it to the task list."""
    
    task = input("Enter a new Task: ")
    task = task.strip()
    if(task != ""):
        tasks.append(task)
        print("Task added successfully")
    else:
        print("A task cannot be empty")


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

def load_tasks(filename):
    """Load tasks from a text file and return them as a list."""
    tasks = []

    try:
        with open(filename, "r") as file:
            for line in file:
                task = line.strip()


                if task != "":
                    tasks.append(task)

                
    except FileNotFoundError:
        # A new project may not have a task file yet.
        return []

    return tasks

def save_tasks(tasks, filename):
    """Save all tasks to a text file."""
    with open(filename, "w") as file:
        
        for i in range(len(tasks)):
            
            file.write(f"{tasks[i]}\n")


def remove_task_by_number(tasks, task_number):
    """Remove a task by its displayed number and return the removed task.

    Return None when the task number is outside the valid range.
    """
    
    #make sure number is in range of list
    if task_number > len(tasks) or task_number <= 0:
        return None
    else:
        #actually remove the task return it
        removedtask = tasks.pop(task_number -1)
        return removedtask
        


def remove_task(tasks):
    """Prompt the user to select and remove a task.

    Return True when a task is removed and False otherwise.
    """
    if not tasks:
        print("No tasks are available to remove.")
        return False

    view_tasks(tasks)
    selection = input("Enter the number of the task to remove: ").strip()

    #Verify that the user input is actually a number
    if not selection.isdigit():
        print("Input given was not a number.")
        return False

    task_number = int(selection)

    removedtask = remove_task_by_number(tasks, task_number)

    #Make sure input is in bounds of task array
    if removedtask == None:
        print("Number input was out of range of numnber of tasks.")
        return False
    else:
        print("Task #" + str(task_number) + ": " + removedtask + " was successfully removed.")
        
        return True

    #remove task user wants gone
    removedtask = tasks.pop(task_number - 1)

    #display was task got removed
    #print("Task #" + str(task_number) + ": " + removedtask + " was successfully removed.")

    #return True

def main():
    """Run the TaskTrack menu until the user chooses to exit."""
    tasks = load_tasks(TASK_FILE)

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks, TASK_FILE)
        elif choice == "3":
            if remove_task(tasks):
                save_tasks(tasks, TASK_FILE)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()