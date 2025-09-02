from .base_client import BaseClient

class AuthClient(BaseClient):
    def login(self, username: str, password: str):
        return self.s.post(
            self._url("/auth/login"),
            json={"username": username, "password": password},
            headers={"Content-Type": "application/json"},
        )
