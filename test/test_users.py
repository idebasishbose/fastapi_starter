from app import schemas
import pytest


def test_create_user(client):
    res = client.post("/users", json={"email": "hello1@gmail.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello1@gmail.com"
    assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    print(res.json())
    assert res.status_code == 200
