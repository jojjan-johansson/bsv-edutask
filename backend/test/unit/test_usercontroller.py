import pytest
from unittest.mock import MagicMock

from src.controllers.usercontroller import UserController


@pytest.fixture
def mock_dao():
    return MagicMock()


@pytest.mark.unit
def test_get_user_by_email_returns_user_when_one_user_found(mock_dao):
    user = {"email": "anna@test.se", "name": "Anna"}
    mock_dao.find.return_value = [user]

    controller = UserController(mock_dao)

    result = controller.get_user_by_email("anna@test.se")

    assert result == user
    mock_dao.find.assert_called_once_with({"email": "anna@test.se"})


@pytest.mark.unit
def test_get_user_by_email_returns_none_when_no_user_found(mock_dao):
    mock_dao.find.return_value = []

    controller = UserController(mock_dao)

    result = controller.get_user_by_email("missing@test.se")

    assert result is None


@pytest.mark.unit
def test_get_user_by_email_returns_first_user_when_multiple_users_found(mock_dao):
    first_user = {"email": "duplicate@test.se", "name": "First"}
    second_user = {"email": "duplicate@test.se", "name": "Second"}
    mock_dao.find.return_value = [first_user, second_user]

    controller = UserController(mock_dao)

    result = controller.get_user_by_email("duplicate@test.se")

    assert result == first_user
    mock_dao.find.assert_called_once_with({"email": "duplicate@test.se"})


@pytest.mark.unit
def test_get_user_by_email_raises_value_error_when_email_is_invalid(mock_dao):
    controller = UserController(mock_dao)

    with pytest.raises(ValueError):
        controller.get_user_by_email("wrong-email")

    mock_dao.find.assert_not_called()


@pytest.mark.unit
def test_get_user_by_email_raises_value_error_when_email_is_empty(mock_dao):
    controller = UserController(mock_dao)

    with pytest.raises(ValueError):
        controller.get_user_by_email("")

    mock_dao.find.assert_not_called()