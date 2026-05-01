@echo off
setlocal enabledelayedexpansion

echo === ELTE IK Assistant Setup ===

:: 1. Check ollama is installed
where ollama >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Ollama not found.
    echo Install it from https://ollama.com/download and re-run this script.
    exit /b 1
)

:: 2. Check Python 3.10+
python -c "import sys; assert sys.version_info >= (3,10), 'fail'" >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python 3.10 or newer is required.
    python --version
    exit /b 1
)

:: 3. Start ollama serve in background
echo [1/6] Starting Ollama service...
start /b ollama serve >nul 2>&1
timeout /t 2 /nobreak >nul

:: 4. Pull required models
echo [2/6] Pulling language models (this may take several minutes)...
ollama pull llama3.2:3b
ollama pull gemma3:4b

:: 5. Create virtualenv if it doesn't exist
echo [3/6] Setting up Python environment...
if not exist ".venv" (
    python -m venv .venv
)
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet

:: 6. Run crawler
echo [4/6] Crawling ELTE documents (this will take several minutes)...
python scripts\crawler.py

:: 7. Build index
echo [5/6] Building knowledge base (chunking + embedding)...
python scripts\build_index.py

echo.
echo [6/6] Setup complete.
echo.
echo To start the server:
echo   .venv\Scripts\Activate.ps1 ^&^& uvicorn app.main:app
echo.
echo Then open: http://localhost:8000/static/index.html
