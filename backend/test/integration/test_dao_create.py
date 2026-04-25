import pytest
from src.util.dao import DAO


@pytest.fixture
def test_user_dao():
    dao = DAO("user")
    dao.drop()

    dao = DAO("user")
    yield dao

    dao.drop()


@pytest.mark.integration
def test_create_valid_user(test_user_dao):
    user = {
        "firstName": "Anna",
        "lastName": "Testsson",
        "email": "anna.integration@test.se"
    }

    result = test_user_dao.create(user)

    assert result["firstName"] == "Anna"
    assert result["lastName"] == "Testsson"
    assert result["email"] == "anna.integration@test.se"
    assert "_id" in result


@pytest.mark.integration
def test_create_user_missing_email(test_user_dao):
    user = {
        "firstName": "Anna",
        "lastName": "Testsson"
    }

    with pytest.raises(Exception):
        test_user_dao.create(user)


@pytest.mark.integration
def test_create_user_wrong_datatype(test_user_dao):
    user = {
        "firstName": 123,
        "lastName": "Testsson",
        "email": "datatype@test.se"
    }

    with pytest.raises(Exception):
        test_user_dao.create(user)


@pytest.mark.integration
def test_create_duplicate_email(test_user_dao):
    user1 = {
        "firstName": "Anna",
        "lastName": "One",
        "email": "duplicate@test.se"
    }

    user2 = {
        "firstName": "Eva",
        "lastName": "Two",
        "email": "duplicate@test.se"
    }

    test_user_dao.create(user1)

    with pytest.raises(Exception):
        test_user_dao.create(user2)