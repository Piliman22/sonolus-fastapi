from enum import Enum

class StorageBackend(str, Enum):
    MEMORY = "memory"
    JSON = "json"
    DATABASE = "database"