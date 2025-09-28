from typing import Optional
#from pydantic import BaseModel, ConfigDict
from pydantic import BaseModel, Field

class Item(BaseModel):
    #id: int
    #name: str
    #description: Optional[str] = None
    #price: float

    #model_config = ConfigDict(extra="forbid")
    username: str = Field(
        ...,
        min_length=3,
        max_length=10,
        pattern=r'^[a-zA-Z0-9]+$',
        title='Username',
        description='must be alpha-numeric',
        example='johndoe777'
    )
    age: Optional[int] = Field(
        None,
        ge=18,
        le=20,
        description="User age must be between 18 and 30",
        example=25
    )

class ItemResponse(BaseModel):
    #id: int
    #name: str
    username: str = Field(
        ...,
        min_length=3,
        max_length=10,
        pattern=r'^[a-zA-Z0-9]+$',
        title='Username',
        description='must be alpha-numeric',
        example='johndoe777'
    )
    age: Optional[int] = Field(
        None,
        ge=18,
        le=20,
        description="User age must be between 18 and 30",
        example=25
    )

class ResponseModel(BaseModel):
    success: bool
    message: str
    data: ItemResponse