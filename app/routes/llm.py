from fastapi import APIRouter, HTTPException
from app.services.llm_service import send_prompt

router = APIRouter()


@router.post("/{conversation_id}")
async def chat_with_llm(conversation_id: str, prompt: str):
    try:
        response = await send_prompt(conversation_id, prompt)
        return {"response": response}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
