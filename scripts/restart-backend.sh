#!/bin/bash

echo "🔄 Restarting Backend with Fixes"
echo "重启后端并应用修复"

# Kill any existing backend process
echo "🛑 Stopping existing backend..."
pkill -f "uvicorn app.main:app" 2>/dev/null || true
sleep 2

# Go to backend directory and restart
cd backend
source venv/bin/activate

echo "🚀 Starting backend server..."
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000