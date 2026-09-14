from .utils import *
from ..routers.auth import get_db, authenticate_user

app.dependency_overrides[get_db] = override_get_db

def test_authenticate_user(test_user):
    db = TestingSessionLocal()

    user = authenticate_user(db, test_user.username, 'testpassword')

    assert user is not None
    assert user.username == test_user.username

    non_existent_user = authenticate_user(db,'WrongUserName', 'testpassword')
    assert non_existent_user is False