from abc import ABC, abstractmethod
from app.insurance.risk import UserRisk
from app.dto.user import UserInformationDTO


class RuleInterface(ABC):
    @abstractmethod
    def apply_rule(self, request) -> UserRisk:
        pass


class BaseRule(RuleInterface):
    next_rule: RuleInterface = None

    def __init__(self, rule: RuleInterface = None):
        self.next_rule = rule

    def __or__(self, other) -> RuleInterface:
        return other(self)

    @abstractmethod
    def apply_rule(
        self,
        user_info: UserInformationDTO,
        user_risk: UserRisk
    ) -> UserRisk:
        if self.next_rule:
            return self.next_rule.apply_rule(user_info, user_risk)
        return user_risk
