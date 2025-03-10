from fastapi import FastAPI, Response, HTTPException, status
from app.config.database import init_db
from app.routes import conversations, llm

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await init_db()


app.include_router(
    conversations.router, prefix="/conversations", tags=["Conversations"]
)
app.include_router(llm.router, prefix="/queries", tags=["LLM Interaction"])
