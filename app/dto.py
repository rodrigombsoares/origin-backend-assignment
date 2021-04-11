from pydantic import BaseModel


class UserInformation(BaseModel):
    age: int,
    dependents: int,
    house: {"ownership_status": "owned"},
    income: int,
    marital_status: "married",
    risk_questions: [0, 1, 0],
    vehicle: {"year": 2018}
