
from typing import List,Optional
from fastapi import APIRouter, Path
from pydantic import BaseModel

users=[]

router= APIRouter()


@router.get("/sections/:{id}")
async def read_section():
    return {"courses":[]}

@router.get("/sections/:{id}/content-blocks")
async def read_section_content_blocks():
    return {"courses":[]}

@router.get("/content-blocks/:{id}")
async def read_content_block():
    return {"courses":[]}