from pydantic import BaseModel

class SubmitAnswerRequest(BaseModel):
    room_id: str
    user_id: str
    answer_user_id: str


class AnswerResultResponse(BaseModel):
    room_id: str
    correct_user_id: str | None

