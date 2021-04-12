from datetime import date

from app.insurance.rules.base import BaseRule
from app.dto.user import UserInformationDTO
from app.insurance.risk import UserRisk


class HasNoVehicle(BaseRule):
    def apply_rule(
        self,
        user_info: UserInformationDTO,
        user_risk: UserRisk
    ) -> UserRisk:
        if not user_info.vehicle:
            user_risk.auto.is_eligible = False
        return super().apply_rule(user_info, user_risk)


class HasNewVehicle(BaseRule):
    def apply_rule(
        self,
        user_info: UserInformationDTO,
        user_risk: UserRisk
    ) -> UserRisk:
        current_year = date.today().year
        if not user_info.vehicle:
            return super().apply_rule(user_info, user_risk)
        if user_info.vehicle["year"] > current_year-5:
            user_risk.auto.risk += 1
        return super().apply_rule(user_info, user_risk)
