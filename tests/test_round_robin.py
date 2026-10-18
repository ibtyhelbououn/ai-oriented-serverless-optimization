
import importlib.util
from pathlib import Path
import pytest

# Load the existing algorithm from its file path.
project_root = Path(__file__).resolve().parents[1]
algorithm_path = (
    project_root
    / "implementation"
    / "round-robin-scheduling"
    / "round-robin-scheduling.py"
)

spec = importlib.util.spec_from_file_location(
    "round_robin_scheduling", algorithm_path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

round_robin = module.round_robin


def test_task_finishes_after_multiple_quanta(capsys):
    tasks = [("A", 5), ("B", 2)]

    round_robin(tasks, 3)

    output = capsys.readouterr().out

    assert "Task A executed for 3 units. Remaining: 2." in output
    assert "Task B completed at time 5." in output
    assert "Task A completed at time 7." in output


def test_task_finishes_within_one_quantum(capsys):
    round_robin([("A", 2)], 3)

    output = capsys.readouterr().out

    assert "Task A completed at time 2." in output


def test_empty_task_list(capsys):
    round_robin([], 3)

    output = capsys.readouterr().out

    assert "Starting Round-Robin Scheduling..." in output
    assert "completed at time" not in output
    assert "executed for" not in output


def test_original_task_list_is_not_modified():
    tasks = [("A", 5), ("B", 2)]
    original_tasks = tasks.copy()

    round_robin(tasks, 3)

    assert tasks == original_tasks


def test_zero_time_quantum_raises_error():
    with pytest.raises(ValueError, match="Time quantum"):
        round_robin([("A", 5)], 0)


def test_negative_time_quantum_raises_error():
    with pytest.raises(ValueError, match="Time quantum"):
        round_robin([("A", 5)], -1)


def test_negative_execution_time_raises_error():
    with pytest.raises(ValueError, match="execution time"):
        round_robin([("A", -2)], 3)

