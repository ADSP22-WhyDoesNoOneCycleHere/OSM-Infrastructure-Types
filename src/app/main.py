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

    return Highway.query_area()

class Area(BaseModel):
    sw: str
    ne: str

@app.post("/area")
async def area(area: Area):
    print(area)

    sw = area.sw
    ne = area.ne

    print(sw)
    print(ne)

    result = Highway.query_area(sw, ne)

    if result is None:
        raise HTTPException(status_code=400, detail="No features found.")

    return result
