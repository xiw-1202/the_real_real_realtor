#!/usr/bin/env python3
"""
System Test Script for NYC Rental Assistant
纽约租房助手系统测试脚本
"""

import asyncio
import aiohttp
import json
import time
from typing import Dict, Any

API_BASE_URL = "http://localhost:8000"

class SystemTester:
    def __init__(self):
        self.session = None
        self.test_results = []
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def test_health_check(self):
        """Test system health endpoint"""
        print("🔍 Testing health check...")
        try:
            async with self.session.get(f"{API_BASE_URL}/health") as response:
                if response.status == 200:
                    data = await response.json()
                    print(f"✅ Health check passed: {data['status']}")
                    return True
                else:
                    print(f"❌ Health check failed: {response.status}")
                    return False
        except Exception as e:
            print(f"❌ Health check error: {e}")
            return False
    
    async def test_chat_english(self):
        """Test English chat functionality"""
        print("🔍 Testing English chat...")
        try:
            payload = {
                "message": "What documents do I need to rent an apartment?",
                "language": "en",
                "session_id": "test-session-en"
            }
            
            async with self.session.post(f"{API_BASE_URL}/chat", json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    print(f"✅ English chat response: {data['message'][:100]}...")
                    return True
                else:
                    print(f"❌ English chat failed: {response.status}")
                    return False
        except Exception as e:
            print(f"❌ English chat error: {e}")
            return False
    
    async def test_chat_chinese(self):
        """Test Chinese chat functionality"""
        print("🔍 Testing Chinese chat...")
        try:
            payload = {
                "message": "租房需要什么文件？",
                "language": "zh",
                "session_id": "test-session-zh"
            }
            
            async with self.session.post(f"{API_BASE_URL}/chat", json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    print(f"✅ Chinese chat response: {data['message'][:100]}...")
                    return True
                else:
                    print(f"❌ Chinese chat failed: {response.status}")
                    return False
        except Exception as e:
            print(f"❌ Chinese chat error: {e}")
            return False
    
    async def test_topics_endpoint(self):
        """Test topics endpoint"""
        print("🔍 Testing topics endpoint...")
        try:
            async with self.session.get(f"{API_BASE_URL}/topics") as response:
                if response.status == 200:
                    data = await response.json()
                    print(f"✅ Topics endpoint returned {len(data)} topics")
                    return True
                else:
                    print(f"❌ Topics endpoint failed: {response.status}")
                    return False
        except Exception as e:
            print(f"❌ Topics endpoint error: {e}")
            return False
    
    async def run_all_tests(self):
        """Run all system tests"""
        print("🚀 Starting NYC Rental Assistant System Tests")
        print("=" * 50)
        
        tests = [
            ("Health Check", self.test_health_check),
            ("English Chat", self.test_chat_english),
            ("Chinese Chat", self.test_chat_chinese),
            ("Topics Endpoint", self.test_topics_endpoint)
        ]
        
        passed = 0
        total = len(tests)
        
        for test_name, test_func in tests:
            print(f"\n📋 Running: {test_name}")
            try:
                result = await test_func()
                if result:
                    passed += 1
                    print(f"✅ {test_name} PASSED")
                else:
                    print(f"❌ {test_name} FAILED")
            except Exception as e:
                print(f"❌ {test_name} ERROR: {e}")
        
        print("\n" + "=" * 50)
        print(f"📊 Test Results: {passed}/{total} tests passed")
        
        if passed == total:
            print("🎉 All tests passed! System is working correctly.")
        else:
            print("⚠️  Some tests failed. Check the output above for details.")
        
        return passed == total

async def main():
    """Main test runner"""
    print("NYC Rental Assistant - System Test")
    print("纽约租房助手 - 系统测试")
    print()
    
    # Check if backend is running
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{API_BASE_URL}/") as response:
                if response.status != 200:
                    raise Exception("Backend not responding")
    except Exception as e:
        print("❌ Backend server is not running!")
        print("Please start the backend server first:")
        print("  cd backend && uvicorn app.main:app --reload")
        return
    
    # Run tests
    async with SystemTester() as tester:
        success = await tester.run_all_tests()
        
    if success:
        print("\n🎯 Next steps:")
        print("1. Open http://localhost:3000 to test the frontend")
        print("2. Try asking questions in both English and Chinese")
        print("3. Check the API documentation at http://localhost:8000/docs")
    else:
        print("\n🔧 Troubleshooting:")
        print("1. Make sure the backend server is running")
        print("2. Check the backend logs for errors")
        print("3. Verify all dependencies are installed")

if __name__ == "__main__":
    asyncio.run(main())