from sqlite3 import adapt
from fastapi import FastAPI
import requests as req
from osmapi import OsmApi

app = FastAPI()

osm = OsmApi()

@app.on_event("startup")
async def startup_event():
    print("startup")

@app.on_event("shutdown")
async def shutdown_event():
    print("shutdown")

@app.get("/")
async def test():

    return osm.NodeGet(123)
    