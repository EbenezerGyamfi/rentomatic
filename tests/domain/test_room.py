import json
import uuid

from domain.room import Room
from serializers.room import RoomJsonEncoder




def test_room_model_init():
    code = uuid.uuid4()

    room = Room(code, 10, 1000,51.5074,-0.1278)

    assert room.code == code
    assert room.size == 10

    assert room.price == 1000
    assert room.lat == 51.5074
    assert room.long == -0.1278


def test_room_model_from_dict():
    code = uuid.uuid4()
    init_dict = {
        'code': code,
        'size': 10,
        'price': 1000,
        'lat': 51.5074,
        'long': -0.1278
    }


    room = Room.from_dict(init_dict)

    assert room.code == code
    assert room.size == 10
    assert room.price == 1000
    assert room.lat == 51.5074
    assert room.long == -0.1278

    assert room.to_dict() == init_dict
    room1 = Room.from_dict(init_dict)
    room2 = Room.from_dict(init_dict)

    assert room1 == room2

def test_serialize_domain_room():
    code = uuid.uuid4()

    room = Room(code, 10, 1000,51.5074,-0.1278)

    expected_json = f"""

    {{

        "code": "{code}",
        "size": 10,
        "price": 1000,
        "lat": 51.5074,
        "long": -0.1278
    }}

    """

    json_room = json.dumps(room, cls=RoomJsonEncoder)

    assert json.loads(json_room) == json.loads(expected_json)

