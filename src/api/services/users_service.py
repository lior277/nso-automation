from src.api.clients.users_client import UsersClient

class UsersService:
    def __init__(self, client: UsersClient | None = None):
        self.client = client or UsersClient()

    def list_page_emails(self, page: int = 1) -> list[str]:
        r = self.client.list_users(page)
        r.raise_for_status()
        return [u["email"] for u in r.json().get("data", [])]

    def get_user_email(self, user_id: int) -> str | None:
        r = self.client.get_user(user_id)
        if r.status_code == 404:
            return None
        r.raise_for_status()
        return r.json().get("data", {}).get("email")
