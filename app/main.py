from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.utils import get_server_data
from app.routes.auth.router import router as router_auth

host, port = get_server_data()
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

app.include_router(router_auth)