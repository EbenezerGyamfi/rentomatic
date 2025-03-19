import uuid
import pytest
from application.app import create_app
from domain.room import Room


@pytest.fixture(scope='module')
def domain_rooms():
    room_1 = Room(
    code=uuid.uuid4(),
    size=215,
    price=39,
    long=-0.09998975,
    lat=51.75436293,
    )

    room_2 = Room(
    code=uuid.uuid4(),
    size=405,
    price=66,
    long=0.18228006,
    lat=51.74640997,
    )

    room_3 = Room(
    code=uuid.uuid4(),
    size=56,
    price=60,
    long=0.27891577,
    lat=51.45994069,
    )

    room_4 = Room(
    code=uuid.uuid4(),
    size=93,
    price=48,
    long=0.33894476,
    lat=51.39916678,
    )


    return [room_1, room_2, room_3, room_4]



def app():
    app = create_app("testing")

    return app
