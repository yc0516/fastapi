from fastapi import APIRouter
from app.schemas.answer import (
    SubmitAnswerRequest,
    AnswerResultResponse
)

router = APIRouter()

@router.post("/", response_model=str)
def submit_answer(req: SubmitAnswerRequest):
    return "ok"


@router.get("/{room_id}", response_model=AnswerResultResponse)
def get_result(room_id: str):
    return {
        "room_id": room_id,
        "correct_user_id": "user_abc"
    }
