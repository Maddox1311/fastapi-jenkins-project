import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test /get_version
def test_get_version():
    response = client.get("/get_version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

# Test /check_prime với số nguyên tố
def test_check_prime_prime_number():
    response = client.get("/check_prime/7")
    assert response.status_code == 200
    assert response.json() == {"number": 7, "is_prime": True}

# Test /check_prime với số không phải nguyên tố
def test_check_prime_non_prime_number():
    response = client.get("/check_prime/4")
    assert response.status_code == 200
    assert response.json() == {"number": 4, "is_prime": False}

# Test /check_prime với số âm
def test_check_prime_negative_number():
    response = client.get("/check_prime/-5")
    assert response.status_code == 400
    assert response.json() == {"detail": "Number must be a non-negative integer"}

# Test /check_prime với số 0
def test_check_prime_zero():
    response = client.get("/check_prime/0")
    assert response.status_code == 200
    assert response.json() == {"number": 0, "is_prime": False}

# Test /check_prime với số 1
def test_check_prime_one():
    response = client.get("/check_prime/1")
    assert response.status_code == 200
    assert response.json() == {"number": 1, "is_prime": False}

# Test /check_prime với số nguyên tố lớn
def test_check_prime_large_prime():
    response = client.get("/check_prime/104729")
    assert response.status_code == 200
    assert response.json() == {"number": 104729, "is_prime": True}

# Test /check_prime với số chia hết cho 2
def test_check_prime_divisible_by_2():
    response = client.get("/check_prime/8")
    assert response.status_code == 200
    assert response.json() == {"number": 8, "is_prime": False}

# Test /check_prime với số chẵn không phải nguyên tố
def test_check_prime_even_non_prime():
    response = client.get("/check_prime/6")
    assert response.status_code == 200
    assert response.json() == {"number": 6, "is_prime": False}

# Test /check_prime với số nguyên tố lẻ
def test_check_prime_odd_prime():
    response = client.get("/check_prime/3")
    assert response.status_code == 200
    assert response.json() == {"number": 3, "is_prime": True}
