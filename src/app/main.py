from pprint import pprint
from fastapi import FastAPI
import requests as req
import overpy
from app.queries.bicycle_infra import Cycleway

from .queries import *

app = FastAPI()

api = overpy.Overpass()

@app.on_event("startup")
async def startup_event():
    print("startup")

@app.on_event("shutdown")
async def shutdown_event():
    print("shutdown")

@app.get("/")
async def test():

    c = Cycleway()

    result = api.query(Cycleway.shared_residential_parking(c))

    pprint(result.ways)

    return { "message": "success" }