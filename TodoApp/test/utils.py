from sqlalchemy import create_engine, StaticPool, text
from sqlalchemy.orm import sessionmaker
from ..database import Base
from fastapi.testclient import TestClient
import pytest
from ..main import app
from ..models import Todos, Users
from ..routers.auth import bcrypt_context

SQLALCHEMY_DATABASE_URI = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    connect_args={"check_same_thread": False},
    poolclass = StaticPool,

)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind = engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {'username': 'robi','id': 1, 'user_role': 'admin'}

client = TestClient(app)

@pytest.fixture
def test_todo():
    todo = Todos(
        title="Learn to Code",
        description="Learn Code",
        priority=5,
        complete=False,
        owner_id=1,
    )

    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("Delete from todos;"))
        connection.commit()



@pytest.fixture
def test_user():
    user = Users(
        username="robi",
        email="robi@gmail.com",
        first_name="eric",
        last_name="robi",
        hashed_password=bcrypt_context.hash("testpassword"),
        role="admin",
        phone_number="+1 555 555 555"
    )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("Delete from users;"))
        connection.commit()