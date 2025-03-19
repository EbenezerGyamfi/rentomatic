

from unittest import mock

from use_cases.room_list import list_rooms, save_registration

def test_room_list_without_parameter(domain_rooms):
    repo = mock.Mock()

    repo.list.return_value = domain_rooms

    result = list_rooms(repo)

    repo.list.assert_called_with()

    assert result == domain_rooms




