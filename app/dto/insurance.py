from pydantic import (
    BaseModel,
    Field,
    ValidationError
)
from enum import Enum
from typing import Optional, List
from typing_extensions import TypedDict


class ScoreEnum(str, Enum):
    economic = "economic"
    regular = "regular"
    responsible = "responsible"
    ineligible = "ineligible"


class InsuranceDTO(BaseModel):
    auto: ScoreEnum
    disability: ScoreEnum
    home: ScoreEnum
    life: ScoreEnum
