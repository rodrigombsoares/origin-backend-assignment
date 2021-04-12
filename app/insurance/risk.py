from app.dto.user import UserInformationDTO
from app.dto.insurance import ScoreEnum, InsuranceDTO


class InsuranceRiskLine:
    risk: int
    is_eligible: bool

    def __init__(self, risk: int, is_eligible: bool) -> None:
        self.risk = risk
        self.is_eligible = is_eligible


class UserRisk:

    def __init__(self, user_info: UserInformationDTO) -> None:
        base = sum([1 if x else 0 for x in user_info.risk_questions])
        self.auto = InsuranceRiskLine(base, True)
        self.disability = InsuranceRiskLine(base, True)
        self.home = InsuranceRiskLine(base, True)
        self.life = InsuranceRiskLine(base, True)

    def _score_from_risk_line(self, line: InsuranceRiskLine) -> ScoreEnum:
        if not line.is_eligible:
            return ScoreEnum.ineligible
        if line.risk <= 0:
            return ScoreEnum.economic
        if line.risk <= 2:
            return ScoreEnum.regular
        if line.risk >= 3:
            return ScoreEnum.responsible

    def evaluate_lines(self) -> InsuranceDTO:
        lines = ["auto", "disability", "home", "life"]
        insurance_dict = dict()
        for line in lines:
            score = self._score_from_risk_line(getattr(self, line))
            insurance_dict[line] = score
        insurance = InsuranceDTO(**insurance_dict)
        return insurance
