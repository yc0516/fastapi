# app/services/room_manager.py
import uuid
from app.models.room import Room

class RoomManager:
    def __init__(self):
        self.rooms = {}

    def get_or_create(self, keyword: str) -> Room:
        if keyword not in self.rooms:
            self.rooms[keyword] = Room(room_id=str(uuid.uuid4()))
        return self.rooms[keyword]

room_manager = RoomManager()

