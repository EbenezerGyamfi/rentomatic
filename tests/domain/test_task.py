

from operator import contains
import pytest
from domain.task import Task


def test_assert_instance():
    task = Task(2,'this title', 'this description')
    assert task.id == 2
    assert task.title == 'this title'
    assert isinstance(task, Task)

# @pytest.mark.skip()
def test_asdict():
    task = Task(4,'second title', 'second description')
    expected = {'id': 4, 'title': 'second title', 'description': 'second description'}
    assert task.to_dict() == expected


