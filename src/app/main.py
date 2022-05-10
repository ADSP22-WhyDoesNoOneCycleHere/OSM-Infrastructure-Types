from fastapi import FastAPI
import requests as req

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("startup")

@app.on_event("shutdown")
async def shutdown_event():
    print("shutdown")

@app.get("/test/{id}")
async def test(id):
    print(id)

    return { "message": "Success!" }