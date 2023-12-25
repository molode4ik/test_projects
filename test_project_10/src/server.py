from fastapi import FastAPI
from src.config.cofig import HOST, PORT
from api.routers import all_routers


app = FastAPI()
for router in all_routers:
    app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)
