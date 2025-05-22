# The Real Real Realtor (真正的房地产经纪人)

A bilingual AI chatbot designed to help Chinese international students navigate apartment rentals in Manhattan and Jersey City. The bot provides comprehensive Q&A support in both English and Simplified Chinese.

## 🎓 Target Users

Chinese international students attending:
- **NYU** (New York University / 纽约大学)
- **Columbia University** (哥伦比亚大学)
- **FIT** (Fashion Institute of Technology / 时装技术学院)
- **The New School** (新学院)
- **SVA** (School of Visual Arts / 视觉艺术学院)
- **Fordham University** (福德汉姆大学)
- **Stevens Institute of Technology** (史蒂文斯理工学院)

## 🌍 Coverage Areas
- **Manhattan**: 130th Street to 1st Street
- **Jersey City**: Full coverage with PATH train connections

## ✨ Key Features

### 🌍 **True Bilingual Experience**
- Seamless English ↔ Chinese switching
- Dynamic message translation
- Language auto-detection
- Cultural context awareness

### 🏠 **Comprehensive Rental Guidance**
- Document requirements and application process
- Lease signing and legal guidance
- Utilities setup (Con Edison, internet, etc.)
- Neighborhood recommendations and safety tips
- Scam prevention and red flags
- University-specific housing advice

### 🤖 **AI-Powered Intelligence**
- Intent classification and smart responses
- Context-aware conversations
- Knowledge base with 500+ rental FAQs
- Real-time response generation

### 📱 **Modern User Experience**
- Mobile-first responsive design
- Intuitive chat interface
- Quick-start question suggestions
- Easy navigation with go-back functionality

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### 1. Setup Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Setup Frontend
```bash
cd frontend
npm install
```

### 3. Start Development Servers

**Terminal 1 (Backend):**
```bash
cd backend
source venv/bin/activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm start
```

### 4. Access Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 🎯 Sample Interactions

### English Examples
```
"What documents do I need to rent an apartment?"
"How do I find apartments near NYU?"
"What's the difference between Manhattan and Jersey City?"
"How do I set up utilities in my new apartment?"
```

### Chinese Examples
```
"租房需要什么文件？"
"如何找到纽约大学附近的公寓？"
"曼哈顿和泽西市有什么区别？"
"如何在新公寓设置水电煤气？"
```

## 🏗️ Architecture

### Backend (Python)
- **FastAPI**: Modern async web framework
- **Knowledge Base**: Structured rental information
- **NLP Engine**: Intent classification and language detection
- **Bilingual Support**: Seamless Chinese/English processing

### Frontend (React)
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Responsive, mobile-first design
- **Real-time Chat**: Instant messaging interface
- **Translation System**: Dynamic language switching

## 📁 Project Structure

```
The Real Real Realtor/
├── backend/                 # Python FastAPI backend
│   ├── app/                # Main application
│   ├── knowledge_base/     # Knowledge management
│   ├── nlp/               # Natural language processing
│   └── utils/             # Utility functions
├── frontend/               # React TypeScript frontend
│   ├── src/               # Source code
│   └── public/            # Static assets
├── docs/                  # Documentation
├── scripts/               # Utility scripts
└── data/                  # Knowledge base data
```

## 🔧 Development Scripts

### Essential Scripts
- `scripts/start-dev.sh` - Start both frontend and backend
- `scripts/setup-backend.sh` - Initialize backend environment
- `scripts/setup-frontend.sh` - Initialize frontend environment
- `scripts/test-system.py` - System integration tests
- `scripts/cleanup-project.sh` - Clean up development files

### Usage
```bash
# Complete setup and start
./scripts/start-dev.sh

# Run system tests
python scripts/test-system.py

# Clean up project files
./scripts/cleanup-project.sh
```

## 🌟 Recent Updates

### New Features
- **Dynamic Translation**: Messages adapt when switching languages
- **Go Back Navigation**: Easy return to welcome screen
- **Enhanced UI**: Professional, mobile-optimized interface
- **Smart Responses**: Improved intent classification and context awareness

### Performance Improvements
- Faster response times
- Better error handling
- Optimized knowledge base searches
- Improved mobile experience

## 🚀 Deployment

### Development
Already configured for local development with hot reload.

### Production
1. Build frontend: `cd frontend && npm run build`
2. Configure environment variables
3. Deploy backend with production ASGI server
4. Serve frontend build with nginx or similar

## 🤝 Contributing

This project helps international students succeed in NYC. Contributions welcome!

### Development Guidelines
- Follow existing code style
- Add tests for new features
- Update documentation
- Test in both languages

## 📄 License

MIT License - Feel free to use for educational and commercial purposes.

## 🎉 Success Stories

**The Real Real Realtor** is helping Chinese international students:
- Navigate complex NYC rental processes
- Understand legal requirements and documentation
- Find safe, affordable housing near their universities
- Avoid common rental scams and pitfalls
- Connect with their new city and community

---

**Making NYC home for international students, one conversation at a time! 🏠🗽**

*Your trusted bilingual guide to finding the perfect place in the Big Apple.*