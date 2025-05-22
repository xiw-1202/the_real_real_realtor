"""
Knowledge Base Manager for NYC Rental Assistant
纽约租房助手知识库管理器
"""

import os
import asyncio
import logging
from typing import List, Dict, Any, Optional, Tuple
import json
import uuid
from datetime import datetime

from app.config import settings

logger = logging.getLogger(__name__)

class KnowledgeBaseManager:
    """
    Manages the knowledge base for the chatbot
    管理聊天机器人的知识库
    """
    
    def __init__(self):
        self.knowledge_entries = {}
        self.topics = {}
        self._initialized = False
        
    async def initialize(self):
        """Initialize the knowledge base manager"""
        try:
            logger.info("Initializing knowledge base manager...")
            
            # For now, create sample data
            await self._create_sample_knowledge_base()
            
            self._initialized = True
            logger.info("Knowledge base manager initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize knowledge base manager: {e}")
            raise e
    
    async def search(
        self,
        query: str,
        language: str = "en",
        max_results: int = 5,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """
        Search the knowledge base for relevant information
        在知识库中搜索相关信息
        """
        if not self._initialized:
            raise RuntimeError("Knowledge base manager not initialized")
        
        try:
            # Simple keyword-based search for MVP
            query_lower = query.lower()
            results = []
            
            for entry_id, entry in self.knowledge_entries.items():
                score = 0.0
                
                # Check question match
                if query_lower in entry.get("question", "").lower():
                    score += 0.8
                
                # Check answer match
                if query_lower in entry.get("answer", "").lower():
                    score += 0.6
                
                # Check keywords match
                for keyword in entry.get("keywords", []):
                    if keyword.lower() in query_lower:
                        score += 0.4
                
                # Check Chinese content if available
                if language == "zh":
                    if entry.get("question_zh") and query_lower in entry.get("question_zh", "").lower():
                        score += 0.9
                    if entry.get("answer_zh") and query_lower in entry.get("answer_zh", "").lower():
                        score += 0.7
                
                if score > 0.2:  # Minimum threshold
                    results.append({
                        "id": entry_id,
                        "title": entry.get("question", ""),
                        "title_zh": entry.get("question_zh"),
                        "content": entry.get("answer", ""),
                        "content_zh": entry.get("answer_zh"),
                        "score": score,
                        "topic": entry.get("topic", ""),
                        "document_type": "faq",
                        "type": "faq"
                    })
            
            # Sort by score
            results.sort(key=lambda x: x["score"], reverse=True)
            
            return results[:max_results]
            
        except Exception as e:
            logger.error(f"Error searching knowledge base: {e}")
            return []
    
    async def get_topics(self) -> List[Dict[str, Any]]:
        """Get available topics in the knowledge base"""
        return [
            {
                "name": topic_data["name"],
                "name_zh": topic_data.get("name_zh", ""),
                "description": topic_data.get("description", ""),
                "description_zh": topic_data.get("description_zh", ""),
                "entry_count": topic_data.get("entry_count", 0),
                "keywords": topic_data.get("keywords", [])
            }
            for topic_data in self.topics.values()
        ]
    
    async def get_stats(self) -> Dict[str, Any]:
        """Get knowledge base statistics"""
        return {
            "total_entries": len(self.knowledge_entries),
            "total_topics": len(self.topics),
            "last_updated": datetime.utcnow().isoformat(),
            "top_topics": [
                {
                    "name": topic_data["name"],
                    "count": topic_data.get("entry_count", 0)
                }
                for topic_data in sorted(
                    self.topics.values(),
                    key=lambda x: x.get("entry_count", 0),
                    reverse=True
                )[:5]
            ]
        }
    
    async def _create_sample_knowledge_base(self):
        """Create sample knowledge base for MVP"""
        
        # Sample FAQ entries
        sample_faqs = [
            {
                "question": "What documents do I need to rent an apartment in NYC?",
                "question_zh": "在纽约租房需要什么文件？",
                "answer": "To rent an apartment in NYC, you typically need: 1) Proof of income (pay stubs, employment letter, or bank statements), 2) Government-issued ID (passport for international students), 3) Social Security Number or ITIN, 4) Rental application, 5) Security deposit (usually 1-2 months rent), 6) First month's rent, 7) Guarantor information if your income is less than 40x the monthly rent.",
                "answer_zh": "在纽约租房，您通常需要：1）收入证明（工资单、雇佣信或银行对账单），2）政府颁发的身份证件（国际学生需要护照），3）社会安全号码或ITIN，4）租房申请，5）押金（通常为1-2个月租金），6）第一个月的租金，7）如果您的收入少于月租金的40倍，需要担保人信息。",
                "topic": "rental_process",
                "keywords": ["documents", "rent", "application", "passport", "income", "guarantor"]
            },
            {
                "question": "How do I find apartments near NYU?",
                "question_zh": "如何找到纽约大学附近的公寓？",
                "answer": "To find apartments near NYU: 1) Check areas like Greenwich Village, East Village, SoHo, and Lower East Side, 2) Use websites like StreetEasy, Zillow, or Apartments.com, 3) Consider NYU's off-campus housing resources, 4) Look for roommate opportunities on Facebook groups or university boards, 5) Visit apartments in person, 6) Budget for higher rents in Manhattan (typically $2,500-$4,000+ for studios/1BR).",
                "answer_zh": "找纽约大学附近的公寓：1）查看格林威治村、东村、苏荷区和下东区等地区，2）使用StreetEasy、Zillow或Apartments.com等网站，3）考虑纽约大学的校外住房资源，4）在Facebook群组或大学布告板上寻找室友机会，5）亲自参观公寓，6）为曼哈顿较高的租金做预算（工作室/一居室通常为$2,500-$4,000+）。",
                "topic": "university",
                "keywords": ["NYU", "Greenwich Village", "East Village", "apartment hunting", "roommate"]
            },
            {
                "question": "How do I set up utilities in my new apartment?",
                "question_zh": "如何在新公寓设置水电煤气？",
                "answer": "To set up utilities in NYC: 1) Electricity: Contact Con Edison (ConEd) at least 2 weeks before move-in, 2) Gas: Also through Con Edison if needed, 3) Internet: Choose from providers like Verizon Fios, Spectrum, or Optimum, 4) Water: Usually included in rent or handled by landlord, 5) Heat: Often included in rent, 6) Bring ID, lease agreement, and be prepared for deposits. Some landlords may handle certain utilities.",
                "answer_zh": "在纽约设置水电煤气：1）电力：至少在搬入前2周联系Con Edison（ConEd），2）燃气：如果需要也通过Con Edison，3）网络：选择Verizon Fios、Spectrum或Optimum等供应商，4）水：通常包含在租金中或由房东处理，5）暖气：通常包含在租金中，6）携带身份证、租约，并准备押金。有些房东可能会处理某些公用事业。",
                "topic": "utilities",
                "keywords": ["utilities", "Con Edison", "electricity", "gas", "internet", "Verizon", "Spectrum"]
            },
            {
                "question": "What's the difference between living in Manhattan vs Jersey City?",
                "question_zh": "住在曼哈顿和泽西市有什么区别？",
                "answer": "Manhattan vs Jersey City: MANHATTAN - Pros: Close to universities, vibrant nightlife, no commute to Manhattan, walkable. Cons: Very expensive ($3,000+ for 1BR), crowded, small spaces. JERSEY CITY - Pros: More affordable ($2,000-3,000 for 1BR), larger apartments, PATH train to Manhattan in 10-20 minutes, parking available. Cons: Commute required, less nightlife, groceries may be limited. Many students choose Jersey City for better value.",
                "answer_zh": "曼哈顿 vs 泽西市：曼哈顿 - 优点：靠近大学，夜生活丰富，无需通勤到曼哈顿，步行友好。缺点：非常昂贵（一居室$3,000+），拥挤，空间小。泽西市 - 优点：更实惠（一居室$2,000-3,000），公寓更大，PATH地铁10-20分钟到曼哈顿，有停车位。缺点：需要通勤，夜生活较少，购物可能有限。许多学生选择泽西市获得更好的性价比。",
                "topic": "neighborhood",
                "keywords": ["Manhattan", "Jersey City", "PATH train", "commute", "rent comparison", "cost"]
            },
            {
                "question": "How do I avoid rental scams in NYC?",
                "question_zh": "如何在纽约避免租房诈骗？",
                "answer": "To avoid rental scams: 1) Never send money before seeing the apartment in person, 2) Be wary of prices significantly below market rate, 3) Verify the landlord's identity and ownership, 4) Don't wire money or pay with gift cards, 5) Meet at the actual property, not just photos, 6) Check the landlord's references, 7) Use reputable websites and licensed brokers, 8) Trust your instincts - if it seems too good to be true, it probably is.",
                "answer_zh": "避免租房诈骗：1）在亲自看房前绝不汇款，2）警惕明显低于市场价的价格，3）验证房东身份和所有权，4）不要电汇或用礼品卡付款，5）在实际房产见面，不仅仅看照片，6）检查房东的推荐信，7）使用信誉良好的网站和持证经纪人，8）相信直觉 - 如果看起来好得不真实，那可能就是假的。",
                "topic": "rental_process",
                "keywords": ["scam", "fraud", "safety", "wire transfer", "verification", "landlord"]
            },
            {
                "question": "What should I know about apartment partitions (隔断) in NYC?",
                "question_zh": "关于纽约公寓隔断我应该了解什么？",
                "answer": "Apartment partitions (隔断) in NYC: 1) Often used to create extra bedrooms in shared apartments, 2) May not be legal - check building regulations, 3) Usually temporary walls that don't reach the ceiling, 4) Can affect ventilation and fire safety, 5) May impact lease terms and deposit, 6) Cheaper option but less privacy, 7) Discuss with landlord and roommates before installing, 8) Some buildings prohibit partitions entirely.",
                "answer_zh": "纽约公寓隔断：1）通常用于在合租公寓中创建额外卧室，2）可能不合法 - 检查建筑法规，3）通常是不到天花板的临时墙，4）可能影响通风和消防安全，5）可能影响租约条款和押金，6）更便宜的选择但隐私较少，7）安装前与房东和室友讨论，8）某些建筑完全禁止隔断。",
                "topic": "rental_process",
                "keywords": ["partition", "隔断", "temporary wall", "roommate", "legal", "building regulations"]
            }
        ]
        
        # Add FAQ entries to knowledge base
        for i, faq in enumerate(sample_faqs):
            entry_id = f"faq_{i+1}"
            faq["id"] = entry_id
            faq["type"] = "faq"
            faq["created_date"] = datetime.utcnow().isoformat()
            self.knowledge_entries[entry_id] = faq
        
        # Initialize topics
        await self._initialize_topics()
        
        logger.info(f"Created sample knowledge base with {len(sample_faqs)} FAQ entries")
    
    async def _initialize_topics(self):
        """Initialize topic categories"""
        
        # Count entries per topic
        topic_counts = {}
        for entry in self.knowledge_entries.values():
            topic = entry.get("topic", "general")
            topic_counts[topic] = topic_counts.get(topic, 0) + 1
        
        # Define topic information
        topic_definitions = {
            "rental_process": {
                "name": "Rental Process",
                "name_zh": "租赁流程",
                "description": "Apartment hunting, applications, lease signing",
                "description_zh": "找房子、申请、签租约",
                "keywords": ["lease", "application", "apartment", "rental", "documents"]
            },
            "utilities": {
                "name": "Utilities Setup",
                "name_zh": "水电煤气设置",
                "description": "Setting up electricity, gas, internet, etc.",
                "description_zh": "设置电力、燃气、网络等",
                "keywords": ["electricity", "gas", "internet", "utilities", "Con Edison"]
            },
            "moving": {
                "name": "Moving Process",
                "name_zh": "搬家流程",
                "description": "Moving procedures and tips",
                "description_zh": "搬家程序和技巧",
                "keywords": ["moving", "relocation", "truck", "boxes"]
            },
            "neighborhood": {
                "name": "Neighborhoods",
                "name_zh": "社区",
                "description": "Area information and recommendations",
                "description_zh": "地区信息和推荐",
                "keywords": ["neighborhood", "area", "location", "safety", "Manhattan", "Jersey City"]
            },
            "university": {
                "name": "University Information",
                "name_zh": "大学信息",
                "description": "University-specific housing guidance",
                "description_zh": "大学特定住房指导",
                "keywords": ["university", "campus", "student", "commute", "NYU", "Columbia"]
            },
            "financial": {
                "name": "Financial Guidance",
                "name_zh": "财务指导",
                "description": "Banking, budgeting, financial tips",
                "description_zh": "银行、预算、财务建议",
                "keywords": ["banking", "budget", "money", "financial"]
            }
        }
        
        # Create topic entries
        for topic, count in topic_counts.items():
            topic_info = topic_definitions.get(topic, {
                "name": topic.title(),
                "name_zh": topic,
                "description": f"Information about {topic}",
                "description_zh": f"关于{topic}的信息",
                "keywords": [topic]
            })
            
            topic_info["entry_count"] = count
            self.topics[topic] = topic_info
        
        logger.info(f"Initialized {len(self.topics)} topic categories")