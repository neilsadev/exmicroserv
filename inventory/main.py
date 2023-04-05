import os
from fastapi import FastAPI
from redis_om import get_redis_connection

app = FastAPI()
redis = get_redis_connection(
    host=os.getenv("HOST"),
    port=os.getenv("PORT"),
    password=os.getenv("PASSWORD"),
    decode_responses=True
)

@app.get("/")
async def root():
    return {"message": "hello world"}