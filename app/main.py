//1月6日　作成者　nao.0516

from fastapi import FastAPI
from app.api import rooms, answers
from app.ws.room_ws import router as ws_router

app = FastAPI()

app.include_router(rooms.router, prefix="/rooms")
app.include_router(answers.router, prefix="/answers")
app.include_router(ws_router)
