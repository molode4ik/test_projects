from fastapi import APIRouter, HTTPException
from src.services.google_service import GoogleService
from src.config.cofig import SECRET_PATH, DOCUMENT_URL


gs = GoogleService(SECRET_PATH=SECRET_PATH, sheet_url=DOCUMENT_URL)
router = APIRouter(
    prefix='/google',
    tags=['Google']
)


@router.get("/get_sheet_data")
async def get_sheet_data(sheet_index: int):
    data = gs.get_worksheet_data(sheet_index)
    return data
