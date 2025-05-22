#!/bin/bash

echo "🚀 Setting up Backend for NYC Rental Assistant"
echo "设置纽约租房助手后端"

cd backend

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "✅ Backend setup complete!"
echo "后端设置完成！"
echo ""
echo "To start the backend server:"
echo "启动后端服务器："
echo "cd backend"
echo "source venv/bin/activate"
echo "python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"