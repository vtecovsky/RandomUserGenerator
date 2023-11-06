from pydantic import BaseModel


class User(BaseModel):
    sex: str
    age: int
    fullname: str
    address: str
    email: str
    username: str
