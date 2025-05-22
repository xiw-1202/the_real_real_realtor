# 🚀 Quick Start Guide - The Real Real Realtor

## ⚡ 5-Minute Setup

### Step 1: Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Step 2: Frontend Setup (New Terminal)
```bash
cd frontend
npm install
npm start
```

### Step 3: Access & Test
- **Open**: http://localhost:3000
- **Test English**: "What documents do I need to rent?"
- **Switch to Chinese**: Click "中文" 
- **Test Chinese**: "租房需要什么文件？"

## ✅ Success Indicators
- Backend: "Application startup complete" + Health checks responding
- Frontend: "Compiled successfully!" + Browser opens to localhost:3000
- Both: Real-time chat working in both languages

## 🔧 Quick Troubleshooting

**Backend won't start?**
```bash
cd backend && source venv/bin/activate && pip install pydantic-settings
```

**Frontend won't start?**
```bash
cd frontend && rm -rf node_modules package-lock.json && npm install
```

**Need help?** Check `docs/DEVELOPMENT_GUIDE.md` for detailed instructions.

## 🎯 What You'll Have
A fully functional bilingual AI chatbot helping Chinese students navigate NYC rentals!

**Time to completion: ~5 minutes** ⏱️