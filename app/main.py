from fastapi import FastAPI, Response, HTTPException, status
from datetime import datetime

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World", "time": str(datetime.now())}
