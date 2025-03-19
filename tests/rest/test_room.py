import json
from domain.room import Room


room_dict = {
    'code': 'room1',
    'size': 10,
    'price': 1000,
    'lat': 51.5074,
    'long': -0.1278
}

room = Room.from_dict(room_dict)


@mock.patch("application.rest.room.room_list_use_case")

def test_get(mock_use_case, client):
    mock_use_case.return_value = [room]

    response = client.get("/rooms/room1")

    assert json.loads(http_response.data.decode("UTF-8") == [room_dict])
    mock_use_case.assert_called()
    assert response.status_code == 200
    assert response.mimetype == "application/json"

