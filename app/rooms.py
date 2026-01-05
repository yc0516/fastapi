# app/api/rooms.py
from fastapi import APIRouter
import uuid

router = APIRouter()
rooms = {}

@router.post("/join")
def join_room(keyword: str, user_name: str):
    room_id = rooms.get(keyword) or str(uuid.uuid4())
    rooms[keyword] = room_id
    return {
        "room_id": room_id,
        "user_id": str(uuid.uuid4())
    }
