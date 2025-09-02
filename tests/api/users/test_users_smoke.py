def test_list_users(users_client):
    r = users_client.list_users(limit=5, skip=0)  # returns UsersResponse
    assert r.limit == 5
    assert len(r.users) > 0
    assert all(u.id for u in r.users)
