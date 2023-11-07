from pydantic import BaseModel


class User(BaseModel):
    fullname: str
    gender: str
    age: int
    address: str
    email: str
    username: str
