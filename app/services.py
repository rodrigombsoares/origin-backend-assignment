from app.dto.insurance import InsuranceDTO
from app.dto.user import UserInformationDTO

from app.insurance.risk import UserRisk
from app.insurance.rules.age import (
    AgeOverSixty,
    AgeUnderThirty,
    AgeBetweenThirtyAndForty
)
from app.insurance.rules.dependents import HasDependents
from app.insurance.rules.house import HasMotgagedHouse, HasNoHouse
from app.insurance.rules.income import HasNoIncome, IncomeAboveTwoHundredK
from app.insurance.rules.marital import IsMaried
from app.insurance.rules.vehicle import HasNoVehicle, HasNewVehicle


def get_insurance_score(user_info: UserInformationDTO) -> InsuranceDTO:
    """
    Set rules in the pipeline using the | (pipe operator) to chain
    so that
        AgeUnderThirty(AgeOverSixty())
    is equivalent to
        AgeOverSixty() | AgeUnderThirty
    """
    # Risk lines are stored using a UserRisk object
    base_risk = UserRisk(user_info)
    # Rules are chained to be applied, add or remove rules here
    rules = (AgeOverSixty()
             | AgeUnderThirty
             | AgeBetweenThirtyAndForty
             | HasDependents
             | HasMotgagedHouse
             | HasNoHouse
             | HasNoIncome
             | IncomeAboveTwoHundredK
             | IsMaried
             | HasNoVehicle
             | HasNewVehicle
             )
    risk = rules.apply_rule(user_info, base_risk)
    return risk.evaluate_lines()
