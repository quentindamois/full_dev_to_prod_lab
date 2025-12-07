from models import User, Task
from app import _build_postgres_uri
import os
import datetime
from werkzeug.security import check_password_hash

def test_is_overdue():
    task = Task(
                title="testtask",
                description="testderscription",
                due_date=datetime.datetime.strptime("2022-01-01", "%Y-%m-%d").date(),
                user_id="1",
            )
    assert task.is_overdue()

def test_set_password():
    user = User(username="testuser")
    user.set_password("123password")
    assert check_password_hash(user.password_hash, "123password")

def test_check_pasword():
    user = User(username="testuser")
    user.set_password("123password")
    assert user.check_password("123password")

def test__build_postgres_uri():
    user = os.environ.get("POSTGRES_USER", "postgres")
    password = os.environ.get("POSTGRES_PASSWORD", "postgres")
    host = os.environ.get("POSTGRES_HOST", "localhost")
    port = os.environ.get("POSTGRES_PORT", "5432")
    name = os.environ.get("POSTGRES_DB", "taskmanager")
    assert _build_postgres_uri() == f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"