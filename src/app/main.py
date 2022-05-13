from fastapi import FastAPI
import requests as req
import overpy
from app.queries.bicycle_infra import Cycleway

from app.queries.car_infra import Roads

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

    print(api.query(Cycleway.cycleway()).nodes[0].id) 
    
    return { "message": "success" }
    