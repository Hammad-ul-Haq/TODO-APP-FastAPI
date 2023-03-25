
from typing import List,Optional
from fastapi import APIRouter, Path
from pydantic import BaseModel

users=[]

router= APIRouter()

class User(BaseModel):
    email: str
    bio: Optional[str]
    is_active: bool


@router.get("/users",response_model=List[User])
async def get_users():
    return users

@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"

@router.get("/users/{id}")
async def get_user(
    id:int = Path(..., description = "The id of user you want to retrieve.",gt=2)
    ):
    return {'user':users[id]}