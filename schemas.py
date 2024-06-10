from pydantic import BaseModel
from typing import Optional
from decouple import config
from datetime import date

class Todo(BaseModel):
    id: str
    title: str
    url: str
    deadline: date

class TodoBody(BaseModel):
    title: str
    url: str
    deadline: date

class SuccessMsg(BaseModel):
    message: str
