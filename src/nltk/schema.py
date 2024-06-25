from pydantic import BaseModel


class Token(BaseModel):
    text: str
