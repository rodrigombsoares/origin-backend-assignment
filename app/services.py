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
    base_risk = UserRisk(user_info)
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
