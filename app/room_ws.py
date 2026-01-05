# app/ws/room_ws.py
from fastapi import APIRouter, WebSocket

router = APIRouter()
connections = {}

@router.websocket("/ws/rooms/{room_id}")
async def room_ws(ws: WebSocket, room_id: str):
    await ws.accept()
    connections.setdefault(room_id, []).append(ws)

    try:
        while True:
            msg = await ws.receive_text()
            for conn in connections[room_id]:
                await conn.send_text(msg)
    except:
        connections[room_id].remove(ws)
