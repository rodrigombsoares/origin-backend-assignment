from app.insurance.rules.base import BaseRule
from app.dto.user import UserInformationDTO
from app.insurance.risk import UserRisk


class HasNoHouse(BaseRule):
    def apply_rule(
        self,
        user_info: UserInformationDTO,
        user_risk: UserRisk
    ) -> UserRisk:
        if not user_info.house:
            user_risk.home.is_eligible = False
        return super().apply_rule(user_info, user_risk)


class HasMotgagedHouse(BaseRule):
    def apply_rule(
        self,
        user_info: UserInformationDTO,
        user_risk: UserRisk
    ) -> UserRisk:
        if not user_info.house:
            return super().apply_rule(user_info, user_risk)

        if user_info.house["ownership_status"] == "mortgaged":
            user_risk.disability.risk += 1
            user_risk.home.risk += 1
        return super().apply_rule(user_info, user_risk)
