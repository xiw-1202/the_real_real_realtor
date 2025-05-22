# 🚨 Startup Fix Guide - NYC Rental Assistant
# 启动修复指南 - 纽约租房助手

## Quick Fix for Current Issues / 当前问题快速修复

### Issue 1: Missing `pydantic-settings` Package
**Error**: `ModuleNotFoundError: No module named 'pydantic_settings'`

**Fix / 修复:**
```bash
cd backend
source venv/bin/activate
pip install pydantic-settings==2.1.0
```

### Issue 2: Frontend Dev Server Configuration
**Error**: `Invalid options object. Dev Server has been initialized...`

**Fix / 修复:**
This has been fixed in the configuration. The frontend should now start properly.

## 🚀 Complete Fix and Start Process

### Step 1: Run the Fix Script / 第一步：运行修复脚本
```bash
./scripts/fix-dependencies.sh
```

### Step 2: Start Backend (Terminal 1) / 第二步：启动后端（终端1）
```bash
cd backend
source venv/bin/activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Expected Success Output / 预期成功输出:**
```
INFO:     Will watch for changes in these directories: ['/Users/sam/Documents/Projects/The Real Real Realty/backend']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxxx] using StatReload
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Step 3: Start Frontend (Terminal 2) / 第三步：启动前端（终端2）
```bash
cd frontend
npm start
```

**Expected Success Output / 预期成功输出:**
```
Compiled successfully!

You can now view nyc-rental-assistant-frontend in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://192.168.x.x:3000

Note that the development build is not optimized.
To create a production build, use npm run build.
```

### Step 4: Test the System / 第四步：测试系统

1. **Open browser / 打开浏览器**: http://localhost:3000
2. **You should see / 应该看到**: Welcome screen with chat interface
3. **Test English / 测试英文**: "What documents do I need to rent?"
4. **Test Chinese / 测试中文**: Switch language and ask "租房需要什么文件？"

## 🔍 Verification Commands / 验证命令

### Test Backend API / 测试后端API
```bash
# Test health endpoint
curl http://localhost:8000/health

# Expected response:
# {"status":"healthy","timestamp":"...","version":"1.0.0","chatbot_ready":true}
```

### Test Chat Endpoint / 测试聊天端点
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello", "language": "en"}'
```

## 🎯 If Still Having Issues / 如果仍有问题

### Backend Issues / 后端问题
```bash
# Check Python version (should be 3.8+)
python --version

# Reinstall dependencies
cd backend
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Frontend Issues / 前端问题
```bash
# Clear cache and reinstall
cd frontend
rm -rf node_modules package-lock.json
npm cache clean --force
npm install
```

### Port Conflicts / 端口冲突
```bash
# Kill processes on ports 3000 and 8000
lsof -ti:3000 | xargs kill -9 2>/dev/null || true
lsof -ti:8000 | xargs kill -9 2>/dev/null || true
```

## ✅ Success Checklist / 成功检查清单

- [ ] Backend starts without errors on port 8000
- [ ] Frontend starts without errors on port 3000
- [ ] Can access http://localhost:3000 in browser
- [ ] Welcome screen displays correctly
- [ ] Can switch between English and Chinese
- [ ] Chat responses work in both languages
- [ ] API documentation accessible at http://localhost:8000/docs

## 🎉 Once Working / 工作后

Try these sample questions to test the system:

**English Questions:**
- "What documents do I need to rent an apartment?"
- "How do I find apartments near NYU?"
- "What's the difference between Manhattan and Jersey City?"

**Chinese Questions:**
- "租房需要什么文件？"
- "如何找到纽约大学附近的公寓？"
- "曼哈顿和泽西市有什么区别？"

**Enjoy your NYC Rental Assistant! 🏠**