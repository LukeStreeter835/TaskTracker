import pytest

from tasktrack import load_tasks, remove_task_by_number, save_tasks


################################ load_task_by_number tests ###############################
@pytest.fixture
def simple_task():
    return ["Study", "Exercise", "Shop"]


@pytest.mark.parametrize(
        "task_number",
        [
            0,
            -1,
            10
        ],
        ids= [
            "zero",
            "negative_number",
            "number_too_large"
        ]
)
def test_invalid_task_numbers_return_none(task_number, simple_task):
    #Arrange 

    #Act
    results = remove_task_by_number(simple_task, task_number)

    #Assert
    assert results is None
    assert simple_task == ["Study", "Exercise", "Shop"]


def test_remove_first_task(simple_task):
    """Removing task 1 should remove the first task."""
    # Arrange
    expected_task = "Study"

    # Act
    removed_task = remove_task_by_number(simple_task, 1)

    # Assert
    assert removed_task == expected_task
    assert simple_task == ["Exercise", "Shop"]

def test_remove_middle_task(simple_task):
    """Input number 2 should remove the second task"""
    #Arrange
    expected_task = "Exercise"

    #Act
    removed_task = remove_task_by_number(simple_task, 2)

    #Assert
    assert removed_task == expected_task
    assert simple_task == ["Study", "Shop"]

def test_remove_last_task(simple_task):
    """putting in task's length as input should remove final task from list"""
    #Arrange
    expected_task = "Shop"

    #Act
    removed_task = remove_task_by_number(simple_task, len(simple_task))

    #Assert
    assert removed_task == expected_task
    assert simple_task == ["Study", "Exercise"]

def test_remove_task_from_empty_list():
    """Should not be able to remove task from an empty list"""

    #Arrange
    tasks = []
    expected_tasks = []

    #Act
    removed_task = remove_task_by_number(tasks, 1)

    #Assert
    assert removed_task is None
    assert tasks == expected_tasks

############################# save_tasks tests #################################

def test_save_tasks_writes_all_tasks(tmp_path):
    # Arrange
    test_file = tmp_path / "tasks.txt"
    tasks = ["Study", "Exercise", "Shop"]
    expected_text = "Study\nExercise\nShop\n"

    # Act
    save_tasks(tasks, test_file)

    # Assert
    assert test_file.read_text() == expected_text

def test_save_tasks_writes_empty_list(tmp_path):
    #Arrange
    test_file = tmp_path / "tasks.txt"

    #Act
    save_tasks([], test_file)

    #Assert
    assert test_file.read_text() == ""


############################# load_tasks tests ################################

def test_load_tasks_reads_all_tasks(tmp_path):
    # Arrange
    test_file = tmp_path / "tasks.txt"
    test_file.write_text("Study\nExercise\nShop\n")
    expected_tasks = ["Study", "Exercise", "Shop"]

    # Act
    result = load_tasks(test_file)

    # Assert
    assert result == expected_tasks

def test_load_tasks_ignores_blank_lines(tmp_path, simple_task):
    # Arrange
    test_file = tmp_path / "tasks.txt"
    test_file.write_text("Study\n\nExercise\nShop\n")

    # Act
    result = load_tasks(test_file)

    # Assert
    assert result == simple_task

def test_load_tasks_no_file_found(tmp_path):
    #Arrange
    test_file = tmp_path / "not_tasks.txt"

    #Act
    result = load_tasks(test_file)

    #Assert
    assert result == []
