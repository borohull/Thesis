#!/usr/bin/env bash
set -e

echo "=== ELTE IK Assistant Setup ==="

# 1. Check ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "ERROR: Ollama not found."
    echo "Install it from https://ollama.com/download and re-run this script."
    exit 1
fi

# 2. Check Python 3.10+
python3 -c "import sys; assert sys.version_info >= (3,10), 'fail'" 2>/dev/null || {
    echo "ERROR: Python 3.10 or newer is required."
    echo "Current version: $(python3 --version 2>&1)"
    exit 1
}

# 3. Start ollama serve in background (safe to run if already running)
echo "[1/6] Starting Ollama service..."
ollama serve &>/dev/null &
sleep 2

# 4. Pull required models
echo "[2/6] Pulling language models (this may take several minutes)..."
ollama pull llama3.2:3b
ollama pull gemma3:4b

# 5. Create virtualenv if it doesn't exist
echo "[3/6] Setting up Python environment..."
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
source .venv/bin/activate
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet

# 6. Run crawler
echo "[4/6] Crawling ELTE documents (this will take several minutes)..."
python scripts/crawler.py

# 7. Build index
echo "[5/6] Building knowledge base (chunking + embedding)..."
python scripts/build_index.py

echo ""
echo "[6/6] Setup complete."
echo ""
echo "To start the server:"
echo "  source .venv/bin/activate && uvicorn app.main:app"
echo ""
echo "Then open: http://localhost:8000/static/index.html"
