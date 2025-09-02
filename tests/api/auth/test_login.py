def test_login_success(auth_client):
    r = auth_client.login("emilys", "emilyspass")  # ✅ working DummyJSON creds
    assert r.status_code == 200, r.text
    data = r.json()
    assert "accessToken" in data
    assert "refreshToken" in data
    assert data["username"] == "emilys"

def test_login_missing_password(auth_client):
    r = auth_client.login("emilys", "")
    # DummyJSON may return 400 Bad Request here
    assert r.status_code == 400
    assert "message" in r.json()
