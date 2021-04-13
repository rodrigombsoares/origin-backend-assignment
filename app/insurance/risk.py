from app.dto.user import UserInformationDTO
from app.dto.insurance import ScoreEnum, InsuranceDTO


class InsuranceRiskLine:
    """A line of insurance with two properties: a risk
    (value of the risk) and users eligibility for that line
    """
    risk: int
    is_eligible: bool

    def __init__(self, risk: int, is_eligible: bool) -> None:
        self.risk = risk
        self.is_eligible = is_eligible


class UserRisk:
    """A UserRisk has risk lines for every insurance line.
    Risk lines are InsuranceRiskLine instances.
    """
    def __init__(self, user_info: UserInformationDTO) -> None:
        # Calculate base risk from user_info risk_questions
        base_risk = sum([1 if x else 0 for x in user_info.risk_questions])
        # Set base values to risk lines
        self.auto = InsuranceRiskLine(base_risk, True)
        self.disability = InsuranceRiskLine(base_risk, True)
        self.home = InsuranceRiskLine(base_risk, True)
        self.life = InsuranceRiskLine(base_risk, True)

    def _score_from_risk_line(self, line: InsuranceRiskLine) -> ScoreEnum:
        """ Method to get score (ineligible, economic, regular, responsible)
        based on risk line value
        """
        if not line.is_eligible:
            return ScoreEnum.ineligible
        if line.risk <= 0:
            return ScoreEnum.economic
        if line.risk <= 2:
            return ScoreEnum.regular
        if line.risk >= 3:
            return ScoreEnum.responsible

    def evaluate_lines(self) -> InsuranceDTO:
        """ For each insurance line evaluate to get risk score
        then, return an InsuranceDTO object
        """
        lines = ["auto", "disability", "home", "life"]
        insurance_dict = dict()
        for line in lines:
            score = self._score_from_risk_line(getattr(self, line))
            insurance_dict[line] = score
        insurance = InsuranceDTO(**insurance_dict)
        return insurance
