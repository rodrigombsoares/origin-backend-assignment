from fastapi import APIRouter
from dto import UserInformation


router = APIRouter(prefix="/insurance", tags=["insurance"])


@router.post("/risk")
async def calculate_risk(user_information: UserInformation):
    return [{"username": "Rick"}, {"username": "Morty"}]
