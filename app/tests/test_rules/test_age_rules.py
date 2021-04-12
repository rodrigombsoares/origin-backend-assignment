from app.dto.user import UserInformationDTO
from app.insurance.risk import UserRisk
from app.insurance.rules.age import (
    AgeOverSixty,
    AgeUnderThirty,
    AgeBetweenThirtyAndForty
)


def test_age_over_sixty():
    # AgeOverSixty
    user1_info = {
        "age": 62,
        "dependents": 2,
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user1_dto = UserInformationDTO(**user1_info)
    user1_base_risk = UserRisk(user1_dto)
    # Build rules set
    rule = (AgeOverSixty()
            | AgeBetweenThirtyAndForty
            | AgeUnderThirty
            )
    risk = rule.apply_rule(user1_dto, user1_base_risk)
    # User 1 should not be eligible to life nor disability
    assert risk.disability.is_eligible == False
    assert risk.auto.risk == 2
    assert risk.home.risk == 2
    assert risk.life.is_eligible == False


def test_age_under_thirty():
    # AgeUnderThirty
    user2_info = {
        "age": 20,
        "dependents": 2,
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user2_dto = UserInformationDTO(**user2_info)
    user2_base_risk = UserRisk(user2_dto)
    # Build rules set
    rule = (AgeOverSixty()
            | AgeBetweenThirtyAndForty
            | AgeUnderThirty
            )
    risk = rule.apply_rule(user2_dto, user2_base_risk)
    # User 2 should have 2 risk points reduced  in all lines
    assert risk.disability.risk == 0
    assert risk.auto.risk == 0
    assert risk.home.risk == 0
    assert risk.life.risk == 0


def test_age_between_thirty_and_forty():
    # AgeBetweenThirtyAndForty
    user3_info = {
        "age": 38,
        "dependents": 2,
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user3_dto = UserInformationDTO(**user3_info)
    user3_base_risk = UserRisk(user3_dto)
    # Build rules set
    rule = (AgeOverSixty()
            | AgeBetweenThirtyAndForty
            | AgeUnderThirty
            )
    risk = rule.apply_rule(user3_dto, user3_base_risk)
    # User 3 should 1 risk point reduced in all lines
    assert risk.disability.risk == 1
    assert risk.auto.risk == 1
    assert risk.home.risk == 1
    assert risk.life.risk == 1


def test_age_no_rule():
    # No rule
    user4_info = {
        "age": 40,
        "dependents": 2,
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user4_dto = UserInformationDTO(**user4_info)
    user4_base_risk = UserRisk(user4_dto)
    # Build rules set
    rule = (AgeOverSixty()
            | AgeBetweenThirtyAndForty
            | AgeUnderThirty
            )
    risk = rule.apply_rule(user4_dto, user4_base_risk)
    # User 4 should have the same base score
    assert risk.disability.risk == 2
    assert risk.auto.risk == 2
    assert risk.home.risk == 2
    assert risk.life.risk == 2
