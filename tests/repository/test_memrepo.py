import pytest

from domain.room import Room
from repository.memrepo import MemRepo


@pytest.fixture()
def room_dicts():
    return [
        {
            "code": "room1",
            "size": 10,
            "price": 100,
            "lat": 51.5,
            "long": -0.1
        },
        {
            "code": "room2",
            "size": 15,
            "price": 150,
            "lat": 51.6,
            "long": -0.2
        },
        {
            "code": "room3",
            "size": 20,
            "price": 200,
            "lat": 51.7,
            "long": -0.3
        }

    ]


def test_reposity_list_without_parameters(room_dicts):
    repo = MemRepo(room_dicts)

    rooms = [Room.from_dict(i) for i in room_dicts]

    assert repo.list() == rooms
