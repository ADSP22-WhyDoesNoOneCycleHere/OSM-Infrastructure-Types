from fastapi import FastAPI
import requests as req
import overpy

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
    query = "node(50.745,7.17,50.75,7.18);out;"
    print(api.query(query).nodes[0].id) 
    return { "message": "success" }
    