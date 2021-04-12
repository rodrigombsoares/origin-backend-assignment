from fastapi import APIRouter

from app.dto.user import UserInformationDTO
from app.dto.insurance import InsuranceDTO
from app import services

router = APIRouter(prefix="/insurance", tags=["insurance"])


@router.post("/risk", response_model=InsuranceDTO)
async def calculate_risk(user_information: UserInformationDTO):
    return services.get_insurance_score(user_information)
