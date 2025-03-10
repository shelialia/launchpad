from fastapi import APIRouter
from app.services.llm_service import send_prompt
from app.models.conversation import Prompt
from app.models.exceptions import InternalServerError
from app.models.parameters import IDParam

router = APIRouter()


@router.post("/{conversation_id}")
async def chat_with_llm(conversation_id: IDParam, prompt: Prompt):
    try:
        response = await send_prompt(conversation_id, prompt.content)
        return {"response": response}
    except Exception as e:
        raise InternalServerError()
