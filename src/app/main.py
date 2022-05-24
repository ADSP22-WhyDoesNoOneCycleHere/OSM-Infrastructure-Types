import json
from pprint import pprint
from fastapi import FastAPI
import requests as req
import overpass
from app.queries.bicycle_infra import Cycleway

from .queries import *

app = FastAPI()

api = overpass.API()

@app.on_event("startup")
async def startup_event():
    print("startup")

@app.on_event("shutdown")
async def shutdown_event():
    print("shutdown")

@app.get("/")
async def test():

    c = Cycleway()

    result = api.get('area[name=Halensee]->.a; way(area.a)[highway]',
                     responseformat='json')

    ways = result.get('elements')

    result = []

    for w in ways:
        w['tags']['infra_type'] = Cycleway.get_types(c, w['tags'])
        result.append(w)

    return result
