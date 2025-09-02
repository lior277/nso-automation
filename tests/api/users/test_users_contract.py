from pydantic import BaseModel, EmailStr
from typing import List, Optional

class DUser(BaseModel):
    id: int
    username: str
    email: Optional[EmailStr] = None
    firstName: str
    lastName: str

class DUsersResponse(BaseModel):
    users: List[DUser]
    total: int
    skip: int
    limit: int

def test_users_page_contract(users_client):
    r = users_client.list_users(limit=5, skip=0)  # ✅ DummyJSON uses limit+skip
    assert r.status_code == 200, r.text
    model = DUsersResponse.model_validate(r.json())
    assert model.limit == 5
    assert len(model.users) == 5
