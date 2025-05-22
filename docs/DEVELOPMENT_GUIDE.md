# Development Guide - The Real Real Realtor

## 🏗️ Architecture Overview

### Tech Stack
- **Backend**: Python FastAPI + Pydantic + uvicorn
- **Frontend**: React + TypeScript + Tailwind CSS
- **AI/NLP**: Custom intent classification + bilingual processing
- **Database**: File-based knowledge base (expandable to vector DB)

### Key Components
- **Chatbot Engine**: Core conversation logic
- **Knowledge Base Manager**: Handles rental information
- **Translation Service**: Dynamic language switching
- **Intent Classifier**: Understands user queries
- **Bilingual UI**: Seamless language experience

## 🚀 Development Workflow

### Setting Up Development Environment
```bash
# Clone and navigate
cd "The Real Real Realty"

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install

# Start both servers
# Terminal 1: cd backend && source venv/bin/activate && uvicorn app.main:app --reload
# Terminal 2: cd frontend && npm start
```

### Adding New Features

#### Backend Development
1. **Models**: Define data structures in `app/models.py`
2. **Endpoints**: Add routes in `app/main.py`
3. **Logic**: Implement in appropriate modules
4. **Knowledge**: Update FAQ entries in `knowledge_base/manager.py`

#### Frontend Development
1. **Components**: Create in `src/components/`
2. **Types**: Define in `src/types/`
3. **Services**: Add API calls in `src/services/`
4. **Styling**: Use Tailwind CSS classes

### Bilingual Content Guidelines
- Always provide both English and Chinese versions
- Use consistent terminology across languages
- Consider cultural context in translations
- Test with native speakers when possible

## 🧪 Testing

### Manual Testing Checklist
- [ ] Both languages work correctly
- [ ] Chat responses are relevant and helpful
- [ ] Language switching works smoothly
- [ ] Mobile interface is responsive
- [ ] Error handling works properly
- [ ] Navigation flows are intuitive

### Automated Testing
```bash
# Backend tests
cd backend && python -m pytest

# Frontend tests  
cd frontend && npm test

# System integration tests
python scripts/test-system.py
```

## 📝 Content Management

### Adding New FAQ Entries
```python
# In knowledge_base/manager.py
await knowledge_manager.add_faq_entry(
    question="How do I...?",
    question_zh="如何...？", 
    answer="You can...",
    answer_zh="您可以...",
    topic="rental_process",
    keywords=["keyword1", "keyword2"]
)
```

### Knowledge Base Topics
- `rental_process`: Applications, leases, documentation
- `utilities`: Con Edison, internet, setup procedures
- `neighborhoods`: Manhattan vs Jersey City, safety, transport
- `university`: Campus-specific guidance
- `financial`: Banking, budgeting, costs
- `moving`: Logistics, timing, services

## 🌍 Internationalization

### Language Support
- **Primary**: English and Simplified Chinese
- **Future**: Traditional Chinese, Spanish, Korean

### Translation Workflow
1. Add English content first
2. Provide Chinese translation
3. Update translation service mappings
4. Test both language versions
5. Verify cultural appropriateness

## 📦 Deployment

### Development
Already configured with hot reload for development.

### Production Preparation
```bash
# Frontend build
cd frontend && npm run build

# Backend optimization
cd backend && pip install gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### Environment Variables
```bash
# Required for production
APP_NAME="The Real Real Realtor"
DEBUG=False
API_HOST=0.0.0.0
API_PORT=8000
```

## 🎯 Best Practices

### Code Quality
- Follow PEP 8 for Python
- Use TypeScript for type safety
- Implement proper error handling
- Write meaningful commit messages

### Performance
- Optimize knowledge base searches
- Implement caching for frequent queries
- Minimize API response times
- Optimize bundle sizes

### Security
- Validate all user inputs
- Sanitize chat messages
- Implement rate limiting
- Use HTTPS in production

## 🔄 Continuous Improvement

### User Feedback Integration
- Monitor chat logs for common questions
- Track unsuccessful query patterns
- Gather user satisfaction metrics
- Iterate on knowledge base content

### Feature Roadmap
- Voice input/output
- Image recognition for documents
- Integration with rental platforms
- Advanced analytics dashboard
- Multi-university expansion

## 📚 Resources

### Documentation
- **FastAPI**: https://fastapi.tiangolo.com/
- **React**: https://reactjs.org/docs
- **Tailwind CSS**: https://tailwindcss.com/docs
- **TypeScript**: https://www.typescriptlang.org/docs/

### NYC Rental Resources
- **Tenant Rights**: https://www1.nyc.gov/site/rentguidelinesboard/
- **Housing Authority**: https://www1.nyc.gov/site/nycha/
- **Student Resources**: University-specific housing offices

---

**Building bridges between international students and their new home in NYC! 🌉🏠**