#!/usr/bin/env python3
"""
Simple Backend Test for NYC Rental Assistant
纽约租房助手后端简单测试
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

def test_imports():
    """Test that all imports work"""
    print("🔍 Testing imports...")
    try:
        from app.main import app
        from app.models import ChatMessage, ChatResponse
        from app.config import settings
        print("✅ All imports successful!")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_basic_functionality():
    """Test basic app functionality"""
    print("🔍 Testing basic functionality...")
    try:
        from app.main import app
        print("✅ FastAPI app created successfully!")
        
        # Test settings
        from app.config import settings
        print(f"✅ Settings loaded: {settings.APP_NAME}")
        
        return True
    except Exception as e:
        print(f"❌ Functionality error: {e}")
        return False

def main():
    print("NYC Rental Assistant - Backend Test")
    print("纽约租房助手 - 后端测试")
    print("=" * 40)
    
    tests = [
        ("Import Test", test_imports),
        ("Functionality Test", test_basic_functionality)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 Running: {test_name}")
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} PASSED")
            else:
                print(f"❌ {test_name} FAILED")
        except Exception as e:
            print(f"❌ {test_name} ERROR: {e}")
    
    print("\n" + "=" * 40)
    print(f"📊 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 Backend is working correctly!")
        print("Next step: Start the server with:")
        print("cd backend && source venv/bin/activate && python -m uvicorn app.main:app --reload")
    else:
        print("⚠️ Some tests failed. Check the setup.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)