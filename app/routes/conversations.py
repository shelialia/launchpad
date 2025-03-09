from fastapi import APIRouter, status
from app.models.conversation import Conversation, ConversationPOST, ConversationPUT
from app.models.responses import (
    CreatedResponse,
    InternalServerError,
    NotFoundError,
    DeletedResponse,
)

router = APIRouter()


@router.post("/", response_model=CreatedResponse, status_code=status.HTTP_201_CREATED)
async def create_conversation(conversation_post: ConversationPOST):
    conversation = Conversation(
        name=conversation_post.name, params=conversation_post.params
    )
    try:
        await conversation.insert()
        return conversation
    except Exception as e:
        raise InternalServerError()


@router.get("/{conversation_id}", response_model=Conversation)
async def get_conversation(conversation_id: str):
    try:
        conversation = await Conversation.get(conversation_id)
        return conversation
    except Exception as e:
        raise InternalServerError()

