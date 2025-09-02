def test_users_to_db(users_client, users_repo):
    r = users_client.list_users(limit=5, skip=0)
    users = r.json()["users"]
    rows = [(u["id"], u.get("email", "n/a"), u["firstName"], u["lastName"]) for u in users]
    users_repo.upsert_many(rows)
    assert users_repo.count() == len(users)
