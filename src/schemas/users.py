from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    fullname: str
    gender: str
    age: int
    address: str
    email: str
    username: str

    model_config = ConfigDict(from_attributes=True)
