from fastapi import FastAPI, Request,Response
from fastapi.middleware.cors import CORSMiddleware
from .routes import challenge, webhooks

app = FastAPI()

app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"], allow_credentials=True)
app.include_router(challenge.router, prefix="/api")
app.include_router(webhooks.router, prefix="/webhooks")