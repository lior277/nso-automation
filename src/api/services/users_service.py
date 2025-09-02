from src.api.clients.users_client import UsersClient
from src.api.models.user_models import User, UsersResponse

class UsersService:
    def __init__(self, client: UsersClient | None = None):
        self.client = client or UsersClient()

    def list_page_emails(self, limit: int = 10, skip: int = 0) -> list[str]:
        users_response: UsersResponse = self.client.list_users(limit=limit, skip=skip)
        return [str(u.email) for u in users_response.users if u.email]

    def get_user_email(self, user_id: int) -> str | None:
        try:
            user: User = self.client.get_user(user_id)
            return user.email
        except Exception:
            # if request fails (e.g. 404), return None
            return None
