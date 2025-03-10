from fastapi import APIRouter, status
from app.models.conversation import Conversation, ConversationPOST, ConversationPUT, ConversationFull
from app.models.responses import (
    CreatedResponse,
    DeletedResponse,
    UpdatedResponse
)
from app.models.exceptions import InternalServerError, NotFoundError
from typing import List

router = APIRouter()


@router.post("/", response_model=CreatedResponse, status_code=status.HTTP_201_CREATED)
async def create_conversation(conversation_post: ConversationPOST):
    """
    Create a new conversation with an LLM model.
    """
    conversation = Conversation(
        name=conversation_post.name, params=conversation_post.params
    )
    try:
        await conversation.insert()
        return conversation
    except Exception as e:
        raise InternalServerError()


@router.get(
    "/",
    response_model=List[Conversation],
    status_code=status.HTTP_200_OK,
    responses={201: {"description": "Successfully retrieved a list of Conversations"}},
)
async def get_conversations():
    try:
        conversations = await Conversation.find_all().to_list(length=None)
        print(conversations)
        return conversations
    except Exception as e:
        raise InternalServerError()


@router.put("/{conversation_id}", response_model=UpdatedResponse)
async def update_conversation(conversation_id: str, conversation_put: ConversationPUT):
    """
    Updates an existing conversation by modifying its name and/or parameters.
    """
    try:
        # Fetch the existing conversation
        conversation = await Conversation.get(conversation_id)
        if not conversation:
            raise NotFoundError()

        # Update fields only if they are provided
        if conversation_put.name:
            conversation.name = conversation_put.name
        if conversation_put.params:
            conversation.params.update(
                conversation_put.params
            )  # Merge new params with existing

        await conversation.save()

    except Exception as e:
        raise InternalServerError()


@router.get(
    "/{conversation_id}",
    response_model=ConversationFull,
    status_code=status.HTTP_200_OK,
    responses={200: {"description": "Successfully retrieved a Conversation"}},
)
async def get_conversation(conversation_id: str):
    """
    Retrieve a conversation by ID.
    """
    try:
        conversation = await Conversation.get(conversation_id)
        if not conversation:
            raise NotFoundError()

        return conversation.messages
    except Exception as e:
        raise InternalServerError()

@router.delete("/{conversation_id}", response_model=DeletedResponse)
async def delete_conversation(conversation_id: str):
    """Deletes a conversation by ID."""
    try:
        conversation = await Conversation.get(conversation_id)
        if not conversation:
            raise NotFoundError()

        await conversation.delete()

    except Exception as e:
        raise InternalServerError()
