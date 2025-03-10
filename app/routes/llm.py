from fastapi import APIRouter, status
from app.services.llm_service import send_prompt
from app.models.conversation import Prompt
from app.models.exceptions import InternalServerError
from app.models.parameters import IDParam
from app.models.responses import CreatedResponse

router = APIRouter()


@router.post("/{conversation_id}", response_model=CreatedResponse, status_code=status.HTTP_201_CREATED) 
async def chat_with_llm(conversation_id: IDParam, prompt: Prompt):
    try:
        response = await send_prompt(conversation_id, prompt.content)
        return {"response": response}
    except Exception as e:
        raise InternalServerError()
