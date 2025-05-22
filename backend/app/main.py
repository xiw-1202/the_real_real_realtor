"""
The Real Real Realtor - Main FastAPI Application
真正的房地产经纪人 - 主FastAPI应用程序
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import logging
from datetime import datetime

from app.config import settings
from app.chatbot import ChatbotEngine
from app.models import ChatMessage, ChatResponse, HealthResponse

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="The Real Real Realtor API",
    description="Bilingual chatbot for Chinese students renting in NYC",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize chatbot engine
chatbot_engine = None

@app.on_event("startup")
async def startup_event():
    """Initialize the chatbot engine on startup"""
    global chatbot_engine
    try:
        logger.info("Initializing chatbot engine...")
        chatbot_engine = ChatbotEngine()
        await chatbot_engine.initialize()
        logger.info("Chatbot engine initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize chatbot engine: {e}")
        raise e

@app.get("/", response_model=Dict[str, str])
async def root():
    """Root endpoint"""
    return {
        "message": "The Real Real Realtor API is running",
        "message_zh": "真正的房地产经纪人API正在运行",
        "status": "healthy"
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow(),
        version="1.0.0",
        chatbot_ready=chatbot_engine is not None and chatbot_engine.is_ready()
    )

@app.post("/chat", response_model=ChatResponse)
async def chat(message: ChatMessage):
    """
    Main chat endpoint for processing user queries
    主要聊天端点，用于处理用户查询
    """
    try:
        if not chatbot_engine or not chatbot_engine.is_ready():
            raise HTTPException(
                status_code=503, 
                detail="Chatbot engine not ready"
            )
        
        # Process the user message
        response = await chatbot_engine.process_message(
            user_message=message.message,
            language=message.language,
            session_id=message.session_id,
            user_context=message.context
        )
        
        return response
        
    except Exception as e:
        logger.error(f"Error processing chat message: {e}")
        error_msg = "Sorry, I encountered an error processing your request."
        error_msg_zh = "抱歉，处理您的请求时遇到了错误。"
        
        return ChatResponse(
            message=error_msg if message.language == "en" else error_msg_zh,
            language=message.language,
            confidence=0.0,
            sources=[],
            suggestions=[],
            session_id=message.session_id
        )

@app.get("/topics", response_model=List[Dict[str, Any]])
async def get_available_topics():
    """
    Get list of available topics in the knowledge base
    获取知识库中可用主题列表
    """
    try:
        if not chatbot_engine:
            raise HTTPException(status_code=503, detail="Chatbot engine not ready")
        
        topics = await chatbot_engine.get_available_topics()
        return topics
        
    except Exception as e:
        logger.error(f"Error fetching topics: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch topics")

@app.post("/feedback")
async def submit_feedback(feedback: Dict[str, Any]):
    """
    Submit user feedback for improving responses
    提交用户反馈以改进回复
    """
    try:
        # Log feedback for analysis
        logger.info(f"User feedback received: {feedback}")
        
        # Here you could store feedback in database
        # await chatbot_engine.store_feedback(feedback)
        
        return {"status": "success", "message": "Feedback received"}
        
    except Exception as e:
        logger.error(f"Error processing feedback: {e}")
        raise HTTPException(status_code=500, detail="Failed to process feedback")

@app.get("/stats")
async def get_system_stats():
    """Get system statistics (for monitoring)"""
    try:
        if not chatbot_engine:
            return {"error": "Chatbot engine not available"}
        
        stats = await chatbot_engine.get_stats()
        return stats
        
    except Exception as e:
        logger.error(f"Error fetching stats: {e}")
        return {"error": "Failed to fetch statistics"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True,
        log_level="info"
    )