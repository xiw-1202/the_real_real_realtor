"""
Language Detector for NYC Rental Assistant
纽约租房助手语言检测器
"""

import logging
from typing import Optional
import re

logger = logging.getLogger(__name__)

class LanguageDetector:
    """
    Detects language of user input
    检测用户输入的语言
    """
    
    def __init__(self):
        self._initialized = False
        
    async def initialize(self):
        """Initialize the language detector"""
        try:
            logger.info("Initializing language detector...")
            self._initialized = True
            logger.info("Language detector initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize language detector: {e}")
            raise e
    
    async def detect(self, text: str) -> str:
        """
        Detect language of text
        检测文本语言
        """
        if not self._initialized:
            raise RuntimeError("Language detector not initialized")
        
        # Simple heuristic-based language detection
        # Check for Chinese characters
        chinese_pattern = re.compile(r'[\u4e00-\u9fff]+')
        
        if chinese_pattern.search(text):
            return "zh"
        else:
            return "en"