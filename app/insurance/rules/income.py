from app.insurance.rules.base import BaseRule
from app.dto.user import UserInformationDTO
from app.insurance.risk import UserRisk


class HasNoIncome(BaseRule):
    def apply_rule(
        self,
        user_info: UserInformationDTO,
        user_risk: UserRisk
    ) -> str:
        if not user_info.income:
            user_risk.disability.is_eligible = False
        return super().apply_rule(user_info, user_risk)


class IncomeAboveTwoHundredK(BaseRule):
    def apply_rule(
        self,
        user_info: UserInformationDTO,
        user_risk: UserRisk
    ) -> str:
        if user_info.income > 200000:
            user_risk.auto -= 1
            user_risk.disability -= 1
            user_risk.life -= 1
            user_risk.home -= 1
        return super().apply_rule(user_info, user_risk)
