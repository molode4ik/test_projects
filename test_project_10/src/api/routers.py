from api.routes.google import router as google_router
from api.routes.github import router as github_router


all_routers = [
    google_router,
    github_router,
]