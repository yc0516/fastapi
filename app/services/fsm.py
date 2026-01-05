# app/services/game_fsm.py
import asyncio, time
from app.core.enums import GameState

async def advance_state(room, broadcast):
    async def change(state, duration=None):
        room.state = state
        await broadcast({
            "type": "STATE_CHANGE",
            "state": state,
            "ends_at": time.time() + duration if duration else None
        })
        if duration:
            await asyncio.sleep(duration)

    await change(GameState.AUDIO, 10)
    await change(GameState.VIDEO, 10)
    await change(GameState.ANSWER, 15)
    await change(GameState.RESULT)

