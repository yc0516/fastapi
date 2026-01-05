# app/models/room.py
from typing import Dict
from app.core.enums import GameState
from app.models.user import User

class Room:
    def __init__(self, room_id: str):
        self.room_id = room_id
        self.state = GameState.LOBBY
        self.users: Dict[str, User] = {}
        self.answers: Dict[str, str] = {}

