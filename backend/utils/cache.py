"""
Cache Manager for NYC Rental Assistant
纽约租房助手缓存管理器
"""

import logging
from typing import Any, Optional
import json
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class CacheManager:
    """
    Manages caching for the chatbot
    管理聊天机器人的缓存
    """
    
    def __init__(self):
        self.cache = {}  # Simple in-memory cache for MVP
        self._initialized = False
        
    async def initialize(self):
        """Initialize the cache manager"""
        try:
            logger.info("Initializing cache manager...")
            self._initialized = True
            logger.info("Cache manager initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize cache manager: {e}")
            raise e
    
    async def get(self, key: str) -> Optional[Any]:
        """
        Get value from cache
        从缓存中获取值
        """
        if not self._initialized:
            raise RuntimeError("Cache manager not initialized")
        
        if key in self.cache:
            entry = self.cache[key]
            if entry["expires"] > datetime.utcnow():
                return entry["value"]
            else:
                # Remove expired entry
                del self.cache[key]
        
        return None
    
    async def set(self, key: str, value: Any, ttl: int = 3600):
        """
        Set value in cache with TTL (time to live)
        在缓存中设置值，带有TTL（生存时间）
        """
        if not self._initialized:
            raise RuntimeError("Cache manager not initialized")
        
        expires = datetime.utcnow() + timedelta(seconds=ttl)
        self.cache[key] = {
            "value": value,
            "expires": expires
        }
    
    async def delete(self, key: str):
        """
        Delete key from cache
        从缓存中删除键
        """
        if key in self.cache:
            del self.cache[key]
    
    async def clear(self):
        """
        Clear all cache
        清除所有缓存
        """
        self.cache.clear()
    
    async def cleanup_expired(self):
        """
        Remove expired entries
        删除过期条目
        """
        now = datetime.utcnow()
        expired_keys = [
            key for key, entry in self.cache.items()
            if entry["expires"] <= now
        ]
        
        for key in expired_keys:
            del self.cache[key]
        
        logger.info(f"Cleaned up {len(expired_keys)} expired cache entries")