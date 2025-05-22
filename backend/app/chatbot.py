"""
Core Chatbot Engine for The Real Real Realtor
真正的房地产经纪人核心聊天机器人引擎
"""

import asyncio
import logging
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
import json
import uuid

from app.config import settings
from app.models import (
    ChatResponse, Language, Source, Suggestion, 
    ConversationContext, SystemStats, Intent
)
# Temporarily create simple mock classes for MVP
class KnowledgeBaseManager:
    async def initialize(self): pass
    async def search(self, query, language="en", max_results=5, filters=None): return []
    async def get_topics(self): return []
    async def get_stats(self): return {"total_entries": 0, "top_topics": []}

class NLPProcessor:
    async def initialize(self): pass

class IntentClassifier:
    async def initialize(self): pass
    async def classify(self, text, language="en"):
        from app.models import Intent
        return Intent(name="general_query", confidence=0.5, entities={})

class LanguageDetector:
    async def initialize(self): pass
    async def detect(self, text): return "zh" if any('\u4e00' <= c <= '\u9fff' for c in text) else "en"

class TranslationService:
    async def initialize(self): pass

class CacheManager:
    async def initialize(self): pass

logger = logging.getLogger(__name__)

class ChatbotEngine:
    """
    Main chatbot engine that orchestrates all components
    主聊天机器人引擎，协调所有组件
    """
    
    def __init__(self):
        self.knowledge_manager = KnowledgeBaseManager()
        self.nlp_processor = NLPProcessor()
        self.intent_classifier = IntentClassifier()
        self.language_detector = LanguageDetector()
        self.translator = TranslationService()
        self.cache_manager = CacheManager()
        
        self.active_sessions: Dict[str, ConversationContext] = {}
        self.stats = {
            "total_queries": 0,
            "queries_today": 0,
            "total_sessions": 0,
            "start_time": datetime.utcnow()
        }
        self._ready = False
        
    async def initialize(self):
        """Initialize all components"""
        try:
            logger.info("Initializing chatbot engine components...")
            
            # Initialize knowledge base
            await self.knowledge_manager.initialize()
            logger.info("Knowledge base initialized")
            
            # Initialize NLP components
            await self.nlp_processor.initialize()
            await self.intent_classifier.initialize()
            await self.language_detector.initialize()
            logger.info("NLP components initialized")
            
            # Initialize translation service
            await self.translator.initialize()
            logger.info("Translation service initialized")
            
            # Initialize cache
            await self.cache_manager.initialize()
            logger.info("Cache manager initialized")
            
            self._ready = True
            logger.info("Chatbot engine fully initialized")
            
        except Exception as e:
            logger.error(f"Failed to initialize chatbot engine: {e}")
            raise e
    
    def is_ready(self) -> bool:
        """Check if chatbot is ready to process requests"""
        return self._ready
    
    async def process_message(
        self,
        user_message: str,
        language: str = "auto",
        session_id: Optional[str] = None,
        user_context: Optional[Dict[str, Any]] = None
    ) -> ChatResponse:
        """
        Process user message and generate response
        处理用户消息并生成回复
        """
        start_time = datetime.utcnow()
        
        try:
            # Generate session ID if not provided
            if not session_id:
                session_id = str(uuid.uuid4())
            
            # Detect language if set to auto
            if language == "auto":
                detected_lang = await self.language_detector.detect(user_message)
                language = detected_lang
            
            # Get or create conversation context
            context = await self._get_conversation_context(session_id, language)
            
            # Update context with user message
            context.conversation_history.append({
                "role": "user",
                "message": user_message,
                "timestamp": start_time.isoformat(),
                "language": language
            })
            
            # Extract intent and entities
            intent = await self.intent_classifier.classify(user_message, language)
            logger.info(f"Classified intent: {intent.name} (confidence: {intent.confidence})")
            
            # Handle different types of intents
            if intent.name == "greeting":
                response = await self._handle_greeting(language, context)
            elif intent.name == "rental_question":
                response = await self._handle_rental_question(
                    user_message, language, intent, context
                )
            elif intent.name == "university_info":
                response = await self._handle_university_question(
                    user_message, language, intent, context
                )
            elif intent.name == "location_query":
                response = await self._handle_location_question(
                    user_message, language, intent, context
                )
            else:
                response = await self._handle_general_query(
                    user_message, language, intent, context
                )
            
            # Add response to conversation history  
            context.conversation_history.append({
                "role": "assistant",
                "message": response.message,
                "timestamp": datetime.utcnow().isoformat(),
                "language": response.language,
                "confidence": response.confidence
            })
            
            # Update session context
            context.last_activity = datetime.utcnow()
            self.active_sessions[session_id] = context
            
            # Calculate response time
            response_time = (datetime.utcnow() - start_time).total_seconds() * 1000
            response.response_time_ms = int(response_time)
            response.session_id = session_id
            
            # Update statistics
            self.stats["total_queries"] += 1
            
            return response
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            
            # Return error response in user's language
            error_messages = {
                "en": "I'm sorry, I encountered an error while processing your request. Please try again.",
                "zh": "抱歉，处理您的请求时遇到了错误。请再试一次。"
            }
            
            return ChatResponse(
                message=error_messages.get(language, error_messages["en"]),
                language=Language(language),
                confidence=0.0,
                sources=[],
                suggestions=[],
                session_id=session_id
            )
    
    async def _get_conversation_context(
        self, 
        session_id: str, 
        language: str
    ) -> ConversationContext:
        """Get or create conversation context for session"""
        if session_id in self.active_sessions:
            return self.active_sessions[session_id]
        
        # Create new context
        context = ConversationContext(
            session_id=session_id,
            user_language=Language(language),
            conversation_history=[]
        )
        
        self.active_sessions[session_id] = context
        self.stats["total_sessions"] += 1
        
        return context
    
    async def _handle_greeting(
        self, 
        language: str, 
        context: ConversationContext
    ) -> ChatResponse:
        """Handle greeting messages"""
        greetings = {
            "en": "Hello! I'm The Real Real Realtor, your trusted NYC rental assistant. I can help you with apartment hunting, lease processes, utilities setup, and general living tips for international students in Manhattan and Jersey City. What would you like to know?",
            "zh": "您好！我是真正的房地产经纪人，您可信赖的纽约租房助手。我可以帮助您找房子、了解租赁流程、设置水电煤气、以及为曼哈顿和泽西市的国际学生提供一般生活建议。您想了解什么？"
        }
        
        suggestions = await self._get_greeting_suggestions(language)
        
        return ChatResponse(
            message=greetings.get(language, greetings["en"]),
            language=Language(language),
            confidence=1.0,
            sources=[],
            suggestions=suggestions
        )
    
    async def get_available_topics(self) -> List[Dict[str, Any]]:
        """Get list of available topics in knowledge base"""
        return await self.knowledge_manager.get_topics()
    
    async def get_stats(self) -> SystemStats:
        """Get system statistics"""
        
        # Get knowledge base stats
        kb_stats = await self.knowledge_manager.get_stats()
        
        return SystemStats(
            total_queries=self.stats["total_queries"],
            queries_today=self.stats["queries_today"],
            average_response_time=0.0,  # TODO: Calculate from actual data
            knowledge_base_size=kb_stats.get("total_entries", 0),
            active_sessions=len(self.active_sessions),
            top_topics=kb_stats.get("top_topics", [])
        )
    
    async def _get_greeting_suggestions(self, language: str) -> List[Suggestion]:
        """Get suggestions for greeting responses"""
        
        if language == "zh":
            texts = [
                "如何在纽约找房子？",
                "租房需要准备什么文件？",
                "我的大学附近有什么好社区？",
                "如何设置水电煤气？"
            ]
        else:
            texts = [
                "How do I find an apartment in NYC?",
                "What documents do I need for renting?",
                "What are good neighborhoods near my university?",
                "How do I set up utilities?"
            ]
        
        return [Suggestion(
            text=text,
            intent="rental_question",
            confidence=0.9
        ) for text in texts]

    async def _handle_general_query(
        self,
        user_message: str,
        language: str,
        intent: Intent,
        context: ConversationContext
    ) -> ChatResponse:
        """Handle general queries by searching knowledge base"""
        
        # Use the knowledge manager to search for relevant information
        search_results = await self.knowledge_manager.search(
            query=user_message,
            language=language,
            max_results=3
        )
        
        if search_results:
            # Use the first/best result
            best_result = search_results[0]
            response_message = best_result.get("content", "")
            
            # If no content, use answer field
            if not response_message:
                response_message = best_result.get("answer", "")
            
            # Fallback response based on language
            if not response_message:
                if language == "zh":
                    response_message = "我理解您的问题，但我需要更多信息才能提供准确的答案。您能具体说明您想了解租房的哪个方面吗？"
                else:
                    response_message = "I understand your question, but I need more information to provide an accurate answer. Could you be more specific about what aspect of renting you'd like to know about?"
            
            # Create sources from search results
            sources = []
            for result in search_results[:2]:  # Top 2 sources
                source = Source(
                    title=result.get("title", "Rental Information"),
                    title_zh=result.get("title_zh", "租房信息"),
                    content_snippet=result.get("content", "")[:150] + "...",
                    relevance_score=result.get("score", 0.0),
                    document_type="faq",
                    topic=result.get("topic", "general")
                )
                sources.append(source)
            
            # Generate follow-up suggestions
            suggestions = await self._get_general_suggestions(language)
            
            return ChatResponse(
                message=response_message,
                language=Language(language),
                confidence=search_results[0].get("score", 0.5),
                sources=sources,
                suggestions=suggestions
            )
        else:
            # No search results found
            return await self._handle_no_results(user_message, language)

    async def _handle_no_results(
        self, 
        user_message: str, 
        language: str
    ) -> ChatResponse:
        """Handle when no relevant results are found"""
        
        no_results_messages = {
            "en": "I don't have specific information about that topic in my knowledge base. However, I can help you with general rental processes, utilities setup, moving procedures, and student life in NYC. Could you try rephrasing your question or ask about a different topic?",
            "zh": "我的知识库中没有关于该主题的具体信息。但是，我可以帮助您了解一般的租赁流程、水电设置、搬家程序和纽约的学生生活。您能重新表述问题或询问其他主题吗？"
        }
        
        return ChatResponse(
            message=no_results_messages.get(language, no_results_messages["en"]),
            language=Language(language),
            confidence=0.1,
            sources=[],
            suggestions=await self._get_general_suggestions(language)
        )

    async def _get_general_suggestions(self, language: str) -> List[Suggestion]:
        """Get general suggestions when no specific results found"""
        
        if language == "zh":
            texts = [
                "纽约租房入门指南",
                "国际学生租房注意事项", 
                "如何避免租房骗局",
                "搬家准备清单"
            ]
        else:
            texts = [
                "NYC rental basics guide",
                "International student rental tips",
                "How to avoid rental scams", 
                "Moving preparation checklist"
            ]
        
        return [Suggestion(
            text=text,
            intent="general_info",
            confidence=0.7
        ) for text in texts]