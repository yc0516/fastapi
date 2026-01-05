# app/ws/room_ws.py
from fastapi import APIRouter, WebSocket
from collections import defaultdict
from app.services.fsm import advance_state

router = APIRouter()
connections = defaultdict(list)

@router.websocket("/ws/rooms/{room_id}")
async def room_ws(ws: WebSocket, room_id: str):
    await ws.accept()
    connections[room_id].append(ws)

    async def broadcast(msg):
        for c in connections[room_id]:
            await c.send_json(msg)

    try:
        while True:
            data = await ws.receive_json()

            if data["type"] == "RTC_SIGNAL":
                await broadcast(data)

            if data["type"] == "START_GAME":
                await advance_state(data["room"], broadcast)

    except:
        connections[room_id].remove(ws)

