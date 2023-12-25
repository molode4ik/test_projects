import httpx
from fastapi import APIRouter, HTTPException
from src.services.google_service import GoogleService
from src.config.cofig import SECRET_PATH, DOCUMENT_URL


gs = GoogleService(SECRET_PATH=SECRET_PATH, sheet_url=DOCUMENT_URL)
router = APIRouter(
    prefix='/github',
    tags=['GitHub']
)


@router.post("/get_info/{username}")
async def get_github_info(username: str, sheet_index: int):
    github_url = f"https://api.github.com/users/{username}"
    async with httpx.AsyncClient() as client:
        response = await client.get(github_url)

    if response.status_code == 200:
        github_data = response.json()
        row_data = [github_data["id"], github_data["login"], github_data["name"], github_data["public_repos"],
                    github_data["location"]]
        gs.append_data(sheet_index, row_data)
        return github_data
    else:
        raise HTTPException(status_code=response.status_code, detail="GitHub API request failed")
