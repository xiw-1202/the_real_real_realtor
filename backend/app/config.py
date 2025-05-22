"""
Configuration settings for the NYC Rental Assistant Chatbot
纽约租房助手聊天机器人配置设置
"""

try:
    from pydantic_settings import BaseSettings
except ImportError:
    from pydantic import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    """Application settings"""
    
    # Application settings
    APP_NAME: str = "The Real Real Realtor"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # API settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    
    # Database settings
    CHROMA_PERSIST_DIRECTORY: str = "./data/embeddings"
    VECTOR_COLLECTION_NAME: str = "nyc_rental_knowledge"
    
    # NLP settings
    DEFAULT_EMBEDDING_MODEL: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    DEFAULT_LANGUAGE: str = "en"
    SUPPORTED_LANGUAGES: List[str] = ["en", "zh"]
    
    # Search settings
    MAX_SEARCH_RESULTS: int = 5
    MIN_SIMILARITY_THRESHOLD: float = 0.3
    
    # Document processing
    MAX_CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200
    
    # Universities and their locations
    TARGET_UNIVERSITIES: dict = {
        "nyu": {
            "name": "New York University",
            "name_zh": "纽约大学",
            "locations": ["Washington Square Park", "Brooklyn", "Manhattan"],
            "coordinates": [40.7295, -73.9965]
        },
        "columbia": {
            "name": "Columbia University", 
            "name_zh": "哥伦比亚大学",
            "locations": ["Morningside Heights", "Manhattan"],
            "coordinates": [40.8075, -73.9626]
        },
        "fit": {
            "name": "Fashion Institute of Technology",
            "name_zh": "时装技术学院", 
            "locations": ["Chelsea", "Manhattan"],
            "coordinates": [40.7465, -73.9959]
        },
        "newschool": {
            "name": "The New School",
            "name_zh": "新学院",
            "locations": ["Greenwich Village", "Manhattan"],
            "coordinates": [40.7359, -73.9959]
        },
        "sva": {
            "name": "School of Visual Arts",
            "name_zh": "视觉艺术学院",
            "locations": ["Chelsea", "Gramercy", "Manhattan"],
            "coordinates": [40.7441, -73.9914]
        },
        "fordham": {
            "name": "Fordham University",
            "name_zh": "福德汉姆大学", 
            "locations": ["Lincoln Center", "Manhattan"],
            "coordinates": [40.7719, -73.9873]
        },
        "stevens": {
            "name": "Stevens Institute of Technology",
            "name_zh": "史蒂文斯理工学院",
            "locations": ["Hoboken", "New Jersey"],
            "coordinates": [40.7447, -74.0248]
        }
    }
    
    # Coverage areas
    MANHATTAN_BOUNDS: dict = {
        "north": "130th Street",
        "south": "1st Street", 
        "west": "Hudson River",
        "east": "East River"
    }
    
    # External API keys (set via environment variables)
    GOOGLE_TRANSLATE_API_KEY: str = ""
    OPENAI_API_KEY: str = ""
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "./logs/chatbot.log"
    
    # Cache settings
    REDIS_URL: str = "redis://localhost:6379"
    CACHE_TTL: int = 3600  # 1 hour
    
    # Rate limiting
    RATE_LIMIT_PER_MINUTE: int = 60
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create global settings instance
settings = Settings()