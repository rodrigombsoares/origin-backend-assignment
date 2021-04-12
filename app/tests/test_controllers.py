from app.tests.client import client


def test_calculate_risk():
    body = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018}
    }
    expected_response = {
        "auto": "regular",
        "disability": "ineligible",
        "home": "economic",
        "life": "regular"
    }
    response = client.post("/insurance/risk", json=body)
    assert response.status_code == 200
    assert response.json() == expected_response


def test_calculate_risk_with_responsible():
    body = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 1],
        "vehicle": {"year": 2018}
    }
    expected_response = {
        "auto": "regular",
        "disability": "ineligible",
        "home": "regular",
        "life": "responsible"
    }
    response = client.post("/insurance/risk", json=body)
    assert response.status_code == 200
    assert response.json() == expected_response


def test_calculate_risk_bad_request():
    body = {
        "age": 35,
        "dependents": 2,
        "house": {"unknown_property": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018}
    }
    response = client.post("/insurance/risk", json=body)
    assert response.status_code == 422
