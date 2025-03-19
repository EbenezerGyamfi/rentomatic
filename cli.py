#!/usr/bin/env python

from domain.room import Room
from repository.memrepo import MemRepo
from use_cases.room_list import list_rooms
rooms = [
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

repo = MemRepo(rooms)

result = list_rooms(repo)

print([room.to_dict() for room in result])
