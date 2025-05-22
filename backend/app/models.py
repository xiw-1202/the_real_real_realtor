"""
Pydantic models for the NYC Rental Assistant Chatbot
纽约租房助手聊天机器人的Pydantic模型
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

class Language(str, Enum):
    """Supported languages"""
    ENGLISH = "en"
    CHINESE = "zh"

class MessageType(str, Enum):
    """Types of messages"""
    QUERY = "query"
    GREETING = "greeting"
    FEEDBACK = "feedback"
    CLARIFICATION = "clarification"

class ChatMessage(BaseModel):
    """Input message from user"""
    message: str = Field(..., description="User message content")
    language: Language = Field(Language.ENGLISH, description="Message language")
    session_id: Optional[str] = Field(None, description="Session ID for conversation tracking")
    message_type: MessageType = Field(MessageType.QUERY, description="Type of message")
    context: Optional[Dict[str, Any]] = Field(None, description="Additional context")
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class Source(BaseModel):
    """Source document information"""
    title: str = Field(..., description="Document title")
    title_zh: Optional[str] = Field(None, description="Chinese title")
    content_snippet: str = Field(..., description="Relevant content snippet")
    relevance_score: float = Field(..., description="Relevance score (0-1)")
    document_type: str = Field(..., description="Type of document")
    topic: str = Field(..., description="Main topic")

class Suggestion(BaseModel):
    """Follow-up suggestions"""
    text: str = Field(..., description="Suggestion text")
    text_zh: Optional[str] = Field(None, description="Chinese suggestion text")
    intent: str = Field(..., description="Intent category")
    confidence: float = Field(..., description="Confidence score")

class ChatResponse(BaseModel):
    """Response from chatbot"""
    message: str = Field(..., description="Bot response message")
    language: Language = Field(..., description="Response language")
    confidence: float = Field(..., description="Response confidence score")
    sources: List[Source] = Field(default_factory=list, description="Source documents")
    suggestions: List[Suggestion] = Field(default_factory=list, description="Follow-up suggestions")
    session_id: Optional[str] = Field(None, description="Session ID")
    response_time_ms: Optional[int] = Field(None, description="Response time in milliseconds")
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class HealthResponse(BaseModel):
    """Health check response"""
    status: str = Field(..., description="Service status")
    timestamp: datetime = Field(..., description="Check timestamp")
    version: str = Field(..., description="Application version")
    chatbot_ready: bool = Field(..., description="Chatbot readiness status")

class DocumentMetadata(BaseModel):
    """Metadata for processed documents"""
    title: str = Field(..., description="Document title")
    title_zh: Optional[str] = Field(None, description="Chinese title")
    source_file: str = Field(..., description="Source file path")
    document_type: str = Field(..., description="Document type")
    topic: str = Field(..., description="Main topic")
    language: Language = Field(..., description="Primary language")
    processed_date: datetime = Field(default_factory=datetime.utcnow)
    chunk_count: int = Field(..., description="Number of text chunks")
    
class KnowledgeEntry(BaseModel):
    """Knowledge base entry"""
    id: str = Field(..., description="Unique identifier")
    question: str = Field(..., description="Question text")
    question_zh: Optional[str] = Field(None, description="Chinese question text")
    answer: str = Field(..., description="Answer text")
    answer_zh: Optional[str] = Field(None, description="Chinese answer text")
    topic: str = Field(..., description="Topic category")
    keywords: List[str] = Field(default_factory=list, description="Keywords")
    keywords_zh: List[str] = Field(default_factory=list, description="Chinese keywords")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")

class UserFeedback(BaseModel):
    """User feedback model"""
    session_id: str = Field(..., description="Session ID")
    message_id: Optional[str] = Field(None, description="Message ID")
    rating: int = Field(..., ge=1, le=5, description="Rating 1-5")
    feedback_text: Optional[str] = Field(None, description="Feedback text")
    feedback_type: str = Field(..., description="Type of feedback")
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class SystemStats(BaseModel):
    """System statistics model"""
    total_queries: int = Field(..., description="Total queries processed")
    queries_today: int = Field(..., description="Queries processed today")
    average_response_time: float = Field(..., description="Average response time in ms")
    knowledge_base_size: int = Field(..., description="Number of knowledge entries")
    active_sessions: int = Field(..., description="Number of active sessions")
    top_topics: List[Dict[str, Any]] = Field(default_factory=list, description="Most queried topics")
    
class Intent(BaseModel):
    """User intent classification"""
    name: str = Field(..., description="Intent name")
    confidence: float = Field(..., description="Confidence score")
    entities: Dict[str, Any] = Field(default_factory=dict, description="Extracted entities")
    
class ConversationContext(BaseModel):
    """Conversation context tracking"""
    session_id: str = Field(..., description="Session ID")
    user_language: Language = Field(..., description="User's preferred language")
    current_topic: Optional[str] = Field(None, description="Current conversation topic")
    user_university: Optional[str] = Field(None, description="User's university")
    user_location_preference: Optional[str] = Field(None, description="Location preference")
    conversation_history: List[Dict[str, Any]] = Field(default_factory=list, description="Recent messages")
    last_activity: datetime = Field(default_factory=datetime.utcnow)
    
class TopicCategory(BaseModel):
    """Topic category information"""
    name: str = Field(..., description="Topic name")
    name_zh: str = Field(..., description="Chinese topic name")
    description: str = Field(..., description="Topic description")
    description_zh: str = Field(..., description="Chinese description")
    keywords: List[str] = Field(..., description="Related keywords")
    keywords_zh: List[str] = Field(..., description="Chinese keywords")
    entry_count: int = Field(..., description="Number of entries in this topic")