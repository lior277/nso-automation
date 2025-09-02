from src.api.models.user_models import UsersResponse

def test_users_page_contract(users_client):
    users_response: UsersResponse = users_client.list_users(limit=5, skip=0)
    assert users_response.limit == 5
    assert isinstance(users_response.users, list)
    assert len(users_response.users) > 0

    # contract check for one user
    user = users_response.users[0]
    assert hasattr(user, "id")
    assert hasattr(user, "email")
    assert hasattr(user, "firstName")
    assert hasattr(user, "lastName")
