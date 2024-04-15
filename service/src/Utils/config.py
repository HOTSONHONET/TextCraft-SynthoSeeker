import os

class OpenAI:
    API_KEY = os.getenv("OPENAI_KEY", "I_WILL_NOT_TELL_YOU")
    MODEL = "gpt-3.5-turbo-1106"

class DBConfig:
    DATABASE_CONNECTION = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "text_craft_synthoseeker")

class Config(DBConfig):
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50
