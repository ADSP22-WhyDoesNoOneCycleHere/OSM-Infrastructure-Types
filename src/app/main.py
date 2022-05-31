from lib2to3.pytree import Base
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .highway import *

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("startup")

@app.on_event("shutdown")
async def shutdown_event():
    print("shutdown")

@app.get("/")
async def test():

    return Highway.get_types()

class Area(BaseModel):
    sw: str
    ne: str
    infra_type: str

@app.post("/area")
async def area(area: Area):
    sw = area["sw"]
    ne = area["ne"]
    infra_type = area["infra_type"]

    result = Highway.get_types(sw, ne, infra_type)

    if result is None:
        raise HTTPException(status_code=400, detail="Wrong feature!")

    return result
