#!/bin/bash

echo "🧹 Cleaning up The Real Real Realtor project files"
echo "清理真正的房地产经纪人项目文件"

# Create archive directory for old files
mkdir -p docs/archive

# Move troubleshooting and fix files to archive
echo "📁 Archiving troubleshooting files..."
mv FINAL_FIX.md docs/archive/ 2>/dev/null || true
mv TYPESCRIPT_FIX.md docs/archive/ 2>/dev/null || true
mv CACHE_FIX.md docs/archive/ 2>/dev/null || true
mv STARTUP_FIX.md docs/archive/ 2>/dev/null || true
mv IMMEDIATE_FIX.md docs/archive/ 2>/dev/null || true
mv SYSTEM_RUNNING_PERFECTLY.md docs/archive/ 2>/dev/null || true
mv REBRANDING_COMPLETE.md docs/archive/ 2>/dev/null || true

# Move development status files to docs
echo "📁 Organizing documentation..."
mv SYSTEM_STATUS.md docs/ 2>/dev/null || true
mv NEW_FEATURES.md docs/ 2>/dev/null || true

# Remove redundant scripts
echo "🗑️ Removing redundant scripts..."
rm -f scripts/fix-dependencies.sh
rm -f scripts/fix-frontend.sh
rm -f scripts/fix-module-resolution.sh
rm -f scripts/fix-npm-cache.sh
rm -f scripts/simple-frontend-server.js

# Create logs directory
mkdir -p logs

# Create data directories
mkdir -p data/documents data/embeddings data/faqs

echo "✅ Cleanup complete!"
echo "清理完成！"
echo ""
echo "📂 Project structure is now organized:"
echo "项目结构现已整理："
echo "  ├── docs/           - Main documentation"
echo "  ├── docs/archive/    - Old troubleshooting files"
echo "  ├── scripts/        - Essential scripts only"
echo "  ├── logs/           - Application logs"
echo "  └── data/           - Knowledge base data"