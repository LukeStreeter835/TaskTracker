# TaskTrack

TaskTrack is a command-line task manager created for CPS 310. The purpose of this program is to allow the user to
keep a list of tasks the user needs to do. It does this by letting the user add new tasks for themselves, and letting them view all tasks they need to do in a list style format. 

## Current Features

-Allows useres to store tasks in program
-Allows users to see tasks they added
-Will save all tasks added onto tasks text file

## Requirements

-Python 3

## Project Files

-`tasktrack.py` - Main program that user use to add, view, and save tasks
-`tasks.txt` - Text file used to preserved tasks added from tasktrack.py
-`.gitignore` - Holds the files that git and git hub should ignore and not see

## Running the Program

cd C:\Users\stree\OneDrive\Desktop\CPS310\TastTracker // Change directory to the correct filepath
python tasktrack.py // run the program

## Task Persistance 

-Tasks are immediately saved once you add a task, there is not specific save task optiion avalible

## Sample Interaction

```text
Booting up the program I wish to see all my current tasks i have saved. So I type "1" into the terminal.
After viewing tasks, Im brought back to main menu. Now I would like to add a task, so I type "2". Now I'm prompted to write in the task I'd like to add, so I type "Clean house" and hit enter. Program tells me it was added
and I'm taken back to the main menu. Now I'd like to see my new task on the task list, so I type "1" to see
that my new tasks is automatically added into the list with the other tasks. Afterwards, I'm taken back to the main menu and now I wish to close the program so I type "3". The program tells me "Goodbye!" and ends. 
```


## Current Limitation

NOTE: There is no current way to remove/complete a task within the program. Once a task is added, the only way to remove it is by going into the text file and doing it yourself.