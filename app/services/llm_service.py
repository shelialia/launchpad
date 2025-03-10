import openai
import os
from dotenv import load_dotenv
from app.models.conversation import Conversation
from app.models.conversation import Prompt, QueryRoleType
from app.models.exceptions import NotFoundError, InvalidCreationError

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


async def send_prompt(conversation_id: str, user_prompt: str):
    """Sends a prompt to the conversation and appends the response."""

    # Fetch conversation from database
    conversation = await Conversation.get(conversation_id)
    if not conversation:
        raise NotFoundError()

    # Convert conversation history to OpenAI format
    conversation_history = [
        {"role": msg.role.value, "content": msg.content}
        for msg in conversation.messages
    ]

    try:
        # Call OpenAI API with updated conversation history
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history + [{"role": "user", "content": user_prompt}],
        )

        assistant_reply = response.choices[0].message.content

        # Create messages using Prompt model and QueryRoleType Enum
        user_message = Prompt(role=QueryRoleType.USER, content=user_prompt)
        assistant_message = Prompt(role=QueryRoleType.ASSISTANT, content=assistant_reply)

        # Append new messages to conversation
        conversation.messages.extend([user_message, assistant_message])

        # Save updated conversation
        await conversation.save()

        return assistant_reply
    except Exception as e:
        raise InvalidCreationError()
