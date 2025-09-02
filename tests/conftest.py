import pytest
from src.api.clients.users_client import UsersClient
from src.api.clients.auth_client import AuthClient
from src.api.services.users_service import UsersService
from src.data.db.sqlite import open_mem
from src.data.repositories.users_repo import UsersRepo

# ---- API Fixtures ----
@pytest.fixture(scope="session")
def users_client() -> UsersClient:
    return UsersClient()

@pytest.fixture(scope="session")
def auth_client() -> AuthClient:
    return AuthClient()

@pytest.fixture(scope="session")
def users_service(users_client) -> UsersService:
    return UsersService(users_client)

# ---- DB Fixtures ----
@pytest.fixture
def db_con():
    con = open_mem()
    yield con
    con.close()

@pytest.fixture
def users_repo(db_con):
    return UsersRepo(db_con)
