def test_users_to_db(users_client, users_repo):
    users_response = users_client.list_users(limit=5, skip=0)
    users = users_response.users   # ✅ already a list[User]
    rows = [(u.id, u.email, u.firstName, u.lastName) for u in users]
    users_repo.upsert_many(rows)
    assert users_repo.count() == len(users)
