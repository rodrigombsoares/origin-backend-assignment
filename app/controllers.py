from fastapi import APIRouter

router = APIRouter(prefix="/insurance", tags=["insurance"])


@router.post("/risk")
async def calculate_risk():
    return [{"username": "Rick"}, {"username": "Morty"}]