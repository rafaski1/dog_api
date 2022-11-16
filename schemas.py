from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import uuid4

from dog_api.enums import Gender


class Dog(BaseModel):
    name: str = Field(
        default=None,
        description="Input your pet's name"
    )
    breed: str
    age: int = Field(ge=0)
    gender: Gender
    city: str
    country: str

    @property
    def dog_id(self) -> str:
        return str(uuid4())

    def to_dict(self) -> dict:
        original_dict = self.dict()
        original_dict.update({"id": self.dog_id})
        return original_dict


class Output(BaseModel):
    success: bool
    message: Optional[str] = None
    results: Optional[List[dict]] = None
