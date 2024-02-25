import os


class DBConfig:
    DATABASE_CONNECTION = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "text_craft_synthoseeker")

class Config(DBConfig):
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50
