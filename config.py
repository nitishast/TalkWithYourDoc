import os
from dotenv import load_dotenv

load_dotenv()

# MODEL = "gemini-1.5-pro"
CHAT_MODEL = "gemini-1.5-pro-exp-0801"
EMBEDDINGS_MODEL = "models/embeddings-001"
API_KEY = os.getenv("GOOGLE_API_KEY")

CHUNK_SIZE = 10000
CHUNK_OVERLAP = 1000
