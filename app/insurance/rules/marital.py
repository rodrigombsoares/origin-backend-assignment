from app.insurance.rules.base import BaseRule
from app.dto.user import UserInformationDTO
from app.insurance.risk import UserRisk


class IsMaried(BaseRule):
    def apply_rule(
        self,
        user_info: UserInformationDTO,
        user_risk: UserRisk
    ) -> UserRisk:
        if user_info.marital_status == "married":
            user_risk.life.risk += 1
            user_risk.disability.risk -= 1
        return super().apply_rule(user_info, user_risk)
