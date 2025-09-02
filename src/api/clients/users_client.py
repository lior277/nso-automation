from requests import Response

from api.clients.base_client import BaseClient
from src.api.models.user_models import UsersResponse, User

class UsersClient(BaseClient):
    def list_users(self, limit: int = 10, skip: int = 0) -> UsersResponse:
        resp: Response = self.s.get(self._url("/users"), params={"limit": limit, "skip": skip})
        resp.raise_for_status()
        return UsersResponse.model_validate(resp.json())

    def get_user(self, user_id: int) -> User:
        resp: Response = self.s.get(self._url(f"/users/{user_id}"))
        resp.raise_for_status()
        return User.model_validate(resp.json())
