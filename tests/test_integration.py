from app import create_app
import testing.postgresql
import pytest

@pytest.fixture
def flask_client():
    test_postgresql = testing.postgresql.Postgresql()
    app = create_app(test_postgresql.url())
    client = app.test_client()
    yield client
    try:
        test_postgresql.stop()
    except:
        if test_postgresql.child_process and test_postgresql.child_process.poll() is None:
            test_postgresql.child_process.terminate()
            test_postgresql.child_process.wait(timeout=20)
    finally:
        test_postgresql.cleanup()
    

def test_register_login(flask_client):
    response = flask_client.post("/register", data=dict(username="testusername", password="testpassword", confirm="testpassword"))
    assert response.status_code == 302
    response = flask_client.post("/login", data=dict(username="testusername", password="testpassword"))
    assert response.status_code == 302

def test_creating_task(flask_client):
    response = flask_client.post("/tasks/new", data=dict(title="testtitle", description="testdescription", due_date="2025-09-01"))
    assert response.status_code == 302

def test_delete_task(flask_client):
    response = flask_client.post("/tasks/new", data=dict(title="testtitle", description="testdescription", due_date="2025-09-01"))
    assert response.status_code == 302
    response = flask_client.post("/tasks/0/delete")
    assert response.status_code == 302

