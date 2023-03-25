from typing import Optional,List
from fastapi import FastAPI,Query,Path
from pydantic import BaseModel

from api import users, sections,courses

app = FastAPI()

app.include_router(router=users.router)
app.include_router(router=sections.router)
app.include_router(router=courses.router)