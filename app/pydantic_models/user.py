from pydantic import BaseModel

class CreateUser(BaseModel):
    name: str
    surname: str
    email: str
