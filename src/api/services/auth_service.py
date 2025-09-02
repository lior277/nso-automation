from src.api.clients.auth_client import AuthClient

class AuthService:
    def __init__(self, client: AuthClient | None = None):
        self.client = client or AuthClient()

    def get_token(self, email: str, password: str) -> str:
        r = self.client.login(email, password)
        r.raise_for_status()
        data = r.json()
        return data.get("token", "")
