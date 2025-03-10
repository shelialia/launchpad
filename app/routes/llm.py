from fastapi import APIRouter, HTTPException
from app.services.llm_service import send_prompt
from app.models.conversation import Prompt
from app.models.responses import InternalServerError

router = APIRouter()


@router.post("/{conversation_id}")
async def chat_with_llm(conversation_id: int, prompt: Prompt):
    try:
        response = await send_prompt(conversation_id, prompt.content)
        return {"response": response}
    except Exception as e:
        raise InternalServerError()
