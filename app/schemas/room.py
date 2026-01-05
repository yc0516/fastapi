from pydantic import BaseModel

class CreateRoomRequest(BaseModel):
    name: str
    keyword: str


class CreateRoomResponse(BaseModel):
    room_id: str

