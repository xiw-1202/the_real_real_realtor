"""
Intent Classifier for NYC Rental Assistant
纽约租房助手意图分类器
"""

import logging
from typing import Dict, List, Any, Optional, Tuple
import re
from datetime import datetime

from app.models import Intent

logger = logging.getLogger(__name__)

class IntentClassifier:
    """
    Classifies user intents for the chatbot
    为聊天机器人分类用户意图
    """
    
    def __init__(self):
        self.intent_patterns = {}
        self._initialized = False
        
    async def initialize(self):
        """Initialize the intent classifier"""
        try:
            logger.info("Initializing intent classifier...")
            
            # Define intent patterns for both English and Chinese
            self.intent_patterns = {
                "greeting": {
                    "patterns": [
                        r"(hello|hi|hey|good morning|good afternoon|good evening)",
                        r"(你好|您好|早上好|下午好|晚上好|嗨)",
                        r"^(hi|hello)$",
                        r"(start|begin|help me)"
                    ],
                    "keywords": ["hello", "hi", "hey", "你好", "您好", "嗨", "start", "help"]
                },
                
                "rental_question": {
                    "patterns": [
                        r"(rent|rental|lease|apartment|housing)",
                        r"(documents|paperwork|application|apply)",
                        r"(deposit|security|first month)",
                        r"(landlord|broker|agent)",
                        r"(租房|租赁|公寓|房子|住房)",
                        r"(文件|申请|押金|房东|中介)",
                        r"(what.*need|how.*rent|where.*find)",
                        r"(需要什么|怎么租|在哪找|如何申请)"
                    ],
                    "keywords": ["rent", "rental", "lease", "apartment", "documents", "application", 
                               "deposit", "landlord", "租房", "租赁", "公寓", "申请", "押金", "房东"]
                },
                
                "university_info": {
                    "patterns": [
                        r"(NYU|nyu|new york university)",
                        r"(Columbia|columbia university)",
                        r"(FIT|fashion institute)",
                        r"(new school|newschool)",
                        r"(SVA|visual arts)",
                        r"(Fordham|fordham)",
                        r"(Stevens|stevens institute)",
                        r"(纽约大学|哥伦比亚|时装技术|新学院|视觉艺术|福德汉姆|史蒂文斯)",
                        r"(university|college|campus|school)",
                        r"(大学|学校|校园|学院)",
                        r"(near.*university|close to campus|commute to)"
                    ],
                    "keywords": ["NYU", "Columbia", "FIT", "university", "campus", "school", 
                               "纽约大学", "哥伦比亚", "大学", "学校", "校园"]
                },
                
                "location_query": {
                    "patterns": [
                        r"(Manhattan|manhattan|Jersey City|jersey city)",
                        r"(neighborhood|area|location|district)",
                        r"(Greenwich Village|East Village|SoHo|Chelsea)",
                        r"(Upper East|Upper West|Lower East|Midtown)",
                        r"(曼哈顿|泽西市|社区|地区|位置|区域)",
                        r"(格林威治|东村|苏荷|切尔西)",
                        r"(where.*live|which area|best neighborhood)",
                        r"(住在哪|哪个地区|最好的社区|附近)"
                    ],
                    "keywords": ["Manhattan", "Jersey City", "neighborhood", "area", "location",
                               "曼哈顿", "泽西市", "社区", "地区", "位置"]
                }
            }
            
            self._initialized = True
            logger.info("Intent classifier initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize intent classifier: {e}")
            raise e
    
    async def classify(self, text: str, language: str = "en") -> Intent:
        """
        Classify user intent from text
        从文本分类用户意图
        """
        if not self._initialized:
            raise RuntimeError("Intent classifier not initialized")
        
        text_lower = text.lower()
        intent_scores = {}
        
        # Calculate scores for each intent
        for intent_name, intent_data in self.intent_patterns.items():
            score = 0.0
            
            # Check pattern matches
            for pattern in intent_data["patterns"]:
                if re.search(pattern, text_lower):
                    score += 0.8
            
            # Check keyword matches
            for keyword in intent_data["keywords"]:
                if keyword.lower() in text_lower:
                    score += 0.6
            
            if score > 0:
                intent_scores[intent_name] = score
        
        # Determine best intent
        if intent_scores:
            best_intent = max(intent_scores, key=intent_scores.get)
            confidence = min(intent_scores[best_intent] / 2.0, 1.0)  # Normalize confidence
            
            # Extract entities for the best intent
            entities = await self._extract_entities(text, best_intent, language)
            
            return Intent(
                name=best_intent,
                confidence=confidence,
                entities=entities
            )
        else:
            # Default to general query if no specific intent detected
            return Intent(
                name="general_query",
                confidence=0.5,
                entities={}
            )
    
    async def _extract_entities(
        self, 
        text: str, 
        intent: str, 
        language: str
    ) -> Dict[str, Any]:
        """Extract entities based on intent"""
        
        entities = {}
        text_lower = text.lower()
        
        # University extraction
        university_patterns = {
            "nyu": [r"nyu", r"new york university", r"纽约大学"],
            "columbia": [r"columbia", r"哥伦比亚"],
            "fit": [r"fit", r"fashion institute", r"时装技术"],
            "newschool": [r"new school", r"新学院"],
            "sva": [r"sva", r"visual arts", r"视觉艺术"],
            "fordham": [r"fordham", r"福德汉姆"],
            "stevens": [r"stevens", r"史蒂文斯"]
        }
        
        for uni_key, patterns in university_patterns.items():
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    entities["university"] = uni_key
                    break
            if "university" in entities:
                break
        
        # Location extraction
        location_patterns = {
            "manhattan": [r"manhattan", r"曼哈顿"],
            "jersey_city": [r"jersey city", r"泽西市"],
            "greenwich_village": [r"greenwich village", r"格林威治村"],
            "east_village": [r"east village", r"东村"]
        }
        
        for loc_key, patterns in location_patterns.items():
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    entities["location"] = loc_key
                    break
            if "location" in entities:
                break
        
        return entities