import os
import motor.motor_asyncio
from beanie import init_beanie
from app.models.conversation import Conversation
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv(
    "MONGO_URI", "mongodb://localhost:27017/llm_db"
)  # Default to local if not set


async def init_db():
    """Initialize MongoDB connection and Beanie ODM."""
    try:
        client = motor.motor_asyncio.AsyncIOMotorClient(
            MONGO_URI, tlsAllowInvalidCertificates=True
        )

        # Extract database name from the URI
        db_name = MONGO_URI.rsplit("/", 1)[-1].split("?")[0]
        db = client[db_name]

        # Initialize Beanie with document models
        await init_beanie(database=db, document_models=[Conversation])

        print("✅ Database initialized successfully!")

    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
