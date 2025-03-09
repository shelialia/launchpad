import os
import motor.motor_asyncio
from beanie import init_beanie
from app.models.conversation import Conversation
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
    db = client.get_database()
    await init_beanie(database=db, document_models=[Conversation])
