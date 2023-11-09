from pydantic import BaseModel, ConfigDict


class RandomUser(BaseModel):
    fullname: str
    gender: str
    age: int
    address: str
    email: str
    username: str

    model_config = ConfigDict(from_attributes=True)


class RandomUserResponse(BaseModel):
    quantity: int
    users: list[RandomUser]
