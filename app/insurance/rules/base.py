from abc import ABC, abstractmethod
from app.insurance.risk import UserRisk
from app.dto.user import UserInformationDTO


class RuleInterface(ABC):
    @abstractmethod
    def apply_rule(self, request) -> UserRisk:
        pass


class BaseRule(RuleInterface):
    """ An Abstract Rule """
    next_rule: RuleInterface = None

    def __init__(self, rule: RuleInterface = None):
        self.next_rule = rule

    def __or__(self, OtherRule: RuleInterface) -> RuleInterface:
        """
        Overload the | operator to chain rules
        """
        return OtherRule(self)

    @abstractmethod
    def apply_rule(
        self,
        user_info: UserInformationDTO,
        user_risk: UserRisk
    ) -> UserRisk:
    """ Apply rule in a chain setting user_risk based on user_info

    Args:
        user_info: An object containing user information
        user_risk: An object containing user risk lines

    Returns:
        An user risk object
    """
        if self.next_rule:
            return self.next_rule.apply_rule(user_info, user_risk)
        return user_risk
