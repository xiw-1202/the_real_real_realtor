"""
NLP Processor for NYC Rental Assistant
纽约租房助手NLP处理器
"""

import logging
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)

class NLPProcessor:
    """
    Main NLP processing class
    主要NLP处理类
    """
    
    def __init__(self):
        self._initialized = False
        
    async def initialize(self):
        """Initialize the NLP processor"""
        try:
            logger.info("Initializing NLP processor...")
            self._initialized = True
            logger.info("NLP processor initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize NLP processor: {e}")
            raise e
    
    async def preprocess_text(self, text: str) -> str:
        """
        Preprocess text for better processing
        预处理文本以便更好地处理
        """
        if not self._initialized:
            raise RuntimeError("NLP processor not initialized")
        
        # Basic text preprocessing
        text = text.strip()
        text = text.lower()
        
        return text
    
    async def extract_keywords(self, text: str, language: str = "en") -> List[str]:
        """
        Extract keywords from text
        从文本中提取关键词
        """
        if not self._initialized:
            raise RuntimeError("NLP processor not initialized")
        
        # Simple keyword extraction
        # Remove common stop words
        stop_words_en = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by", "is", "are", "was", "were", "be", "been", "have", "has", "had", "do", "does", "did", "will", "would", "could", "should", "may", "might", "can", "i", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them"}
        stop_words_zh = {"的", "了", "在", "是", "我", "你", "他", "她", "们", "这", "那", "有", "和", "与", "或", "但", "如果", "因为", "所以", "可以", "能够", "需要", "应该", "会", "要", "想", "给", "对", "从", "到", "用", "把", "被", "让"}
        
        stop_words = stop_words_zh if language == "zh" else stop_words_en
        
        # Split and filter
        words = text.lower().split()
        keywords = [word for word in words if word not in stop_words and len(word) > 2]
        
        return keywords[:10]  # Return top 10 keywords