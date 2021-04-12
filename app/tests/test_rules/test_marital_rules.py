from app.dto.user import UserInformationDTO
from app.insurance.risk import UserRisk
from app.insurance.rules.marital import IsMaried


def test_is_maried():
    # IsMaried
    user_info = {
        "age": 62,
        "dependents": 2,
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 1],
    }
    user_dto = UserInformationDTO(**user_info)
    user_base_risk = UserRisk(user_dto)
    # Build rules set
    rule = IsMaried()
    risk = rule.apply_rule(user_dto, user_base_risk)
    # User should not be eligible to disability
    assert risk.disability.risk == 1
    assert risk.auto.risk == 2
    assert risk.home.risk == 2
    assert risk.life.risk == 3


def test_is_single():
    # No rule to apply
    user_info = {
        "age": 62,
        "dependents": 0,
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user_dto = UserInformationDTO(**user_info)
    user_base_risk = UserRisk(user_dto)
    # Build rules set
    rule = IsMaried()
    risk = rule.apply_rule(user_dto, user_base_risk)
    # User risk should not change
    assert risk.disability.risk == 2
    assert risk.auto.risk == 2
    assert risk.home.risk == 2
    assert risk.life.risk == 2
