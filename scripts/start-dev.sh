#!/bin/bash

# NYC Rental Assistant - Development Startup Script
# 纽约租房助手 - 开发启动脚本

echo "🏠 Starting The Real Real Realtor Development Environment"
echo "真正的房地产经纪人开发环境启动中..."

# Create necessary directories
mkdir -p logs data/embeddings data/documents data/faqs

# Check if Python virtual environment exists
if [ ! -d "backend/venv" ]; then
    echo "Creating Python virtual environment..."
    cd backend
    python3 -m venv venv
    cd ..
fi

# Activate Python virtual environment
echo "Activating Python virtual environment..."
source backend/venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
cd backend
pip install --upgrade pip
pip install -r requirements.txt
cd ..

# Start backend server in background
echo "Starting backend server..."
cd backend
source venv/bin/activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
cd ..

# Wait for backend to start
echo "Waiting for backend server to start..."
sleep 5

# Check if Node.js dependencies are installed
if [ ! -d "frontend/node_modules" ]; then
    echo "Installing Node.js dependencies..."
    cd frontend
    npm install
    cd ..
fi

# Start frontend development server
echo "Starting frontend development server..."
cd frontend
npm start &
FRONTEND_PID=$!
cd ..

echo ""
echo "🎉 Development environment started successfully!"
echo "开发环境启动成功！"
echo ""
echo "📡 Backend API: http://localhost:8000"
echo "🌐 Frontend App: http://localhost:3000"
echo "📚 API Documentation: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop all services"
echo "按 Ctrl+C 停止所有服务"

# Function to handle cleanup
cleanup() {
    echo ""
    echo "Stopping services..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    echo "Services stopped. Goodbye!"
    exit 0
}

# Trap Ctrl+C
trap cleanup INT

# Wait for user to stop
wait