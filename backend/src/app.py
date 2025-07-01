from fastapi import FastAPI, Request,Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middlware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"], allow_credentials=True)