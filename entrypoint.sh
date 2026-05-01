#!/bin/bash
set -e

if [ ! -d "/app/data/processed/chroma_db" ]; then
    echo "Knowledge base not found — building from scratch."
    echo "This will take several minutes on first run."
    python scripts/crawler.py
    python scripts/build_index.py
else
    echo "Knowledge base found — skipping build."
fi

exec uvicorn app.main:app --host 0.0.0.0 --port 8000