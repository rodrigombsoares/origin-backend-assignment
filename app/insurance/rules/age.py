from app.insurance.rules.base import BaseRule
from app.dto.user import UserInformationDTO
from app.insurance.risk import UserRisk


class AgeOverSixty(BaseRule):
    def apply_rule(
        self,
        user_info: UserInformationDTO,
        user_risk: UserRisk
    ) -> UserRisk:
        if user_info.age > 60:
            user_risk.disability.is_eligible = False
            user_risk.life.is_eligible = False
        return super().apply_rule(user_info, user_risk)


class AgeUnderThirty(BaseRule):
    def apply_rule(
        self,
        user_info: UserInformationDTO,
        user_risk: UserRisk
    ) -> UserRisk:
        if user_info.age < 30:
            user_risk.disability.risk -= 2
            user_risk.auto.risk -= 2
            user_risk.home.risk -= 2
            user_risk.life.risk -= 2
        return super().apply_rule(user_info, user_risk)


class AgeBetweenThirtyAndForty(BaseRule):
    def apply_rule(
        self,
        user_info: UserInformationDTO,
        user_risk: UserRisk
    ) -> UserRisk:
        if user_info.age >= 30 and user_info.age < 40:
            user_risk.disability.risk -= 1
            user_risk.auto.risk -= 1
            user_risk.home.risk -= 1
            user_risk.life.risk -= 1
        return super().apply_rule(user_info, user_risk)
