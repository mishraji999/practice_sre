from fastapi.testclient import TestClient
from main import app
#httpx added

client = TestClient(app)

def test_health():
    response = client.get("/")
    assert response.status_code == 200
