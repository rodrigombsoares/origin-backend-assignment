from app.dto.user import UserInformationDTO
from app.insurance.risk import UserRisk
from app.insurance.rules.house import HasMotgagedHouse, HasNoHouse


def test_motgaged_house():
    # MortgagedHouse
    user_info = {
        "age": 62,
        "dependents": 2,
        "house": {"ownership_status": "mortgaged"},
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user_dto = UserInformationDTO(**user_info)
    user_base_risk = UserRisk(user_dto)
    # Build rules set
    rule = HasMotgagedHouse() | HasNoHouse
    risk = rule.apply_rule(user_dto, user_base_risk)
    # User should have 1 score point added to home and disability
    assert risk.disability.risk == 3
    assert risk.auto.risk == 2
    assert risk.home.risk == 3
    assert risk.life.risk == 2


def test_owned_house():
    # OwnedHouse
    user_info = {
        "age": 62,
        "dependents": 2,
        "income": 1000,
        "house": {"ownership_status": "owned"},
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user_dto = UserInformationDTO(**user_info)
    user_base_risk = UserRisk(user_dto)
    # Build rules set
    rule = HasMotgagedHouse() | HasNoHouse
    risk = rule.apply_rule(user_dto, user_base_risk)
    # User should have same scores
    assert risk.disability.risk == 2
    assert risk.auto.risk == 2
    assert risk.home.risk == 2
    assert risk.life.risk == 2


def test_no_house():
    # No house
    user_info = {
        "age": 62,
        "dependents": 2,
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user_dto = UserInformationDTO(**user_info)
    user_base_risk = UserRisk(user_dto)
    # Build rules set
    rule = HasMotgagedHouse() | HasNoHouse
    risk = rule.apply_rule(user_dto, user_base_risk)
    # User should not be eligible to home insurance
    assert risk.disability.risk == 2
    assert risk.auto.risk == 2
    assert risk.home.is_eligible == False
    assert risk.life.risk == 2
