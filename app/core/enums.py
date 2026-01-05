# app/core/enums.py
from enum import Enum

class GameState(str, Enum):
    KEYWORD = "KEYWORD"
    LOBBY = "LOBBY"
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"
    ANSWER = "ANSWER"
    RESULT = "RESULT"

