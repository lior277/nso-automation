def test_list_users(users_client):
    r = users_client.list_users(limit=5, skip=0)  # ✅ DummyJSON uses limit+skip
    assert r.status_code == 200, r.text
    data = r.json()
    assert "users" in data
    assert len(data["users"]) > 0
