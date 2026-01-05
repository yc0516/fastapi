from fastapi import APIRouter
from app.schemas.room import CreateRoomRequest, CreateRoomResponse

router = APIRouter()

@router.post("/", response_model=CreateRoomResponse)
def create_room(req: CreateRoomRequest):
    return {
        "room_id": "room_123"
    }
