import sqlite3
import json
from datetime import datetime, timezone
from pathlib import Path

_DB_PATH = Path(__file__).parent.parent / "data" / "logs" / "chat_logs.db"


def _connect() -> sqlite3.Connection:
    _DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(_DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def init_db() -> None:
    """Create tables if they don't exist. Called once on startup."""
    with _connect() as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS chat_logs (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp     TEXT    NOT NULL,
                user_message  TEXT    NOT NULL,
                answer        TEXT    NOT NULL,
                sources       TEXT    NOT NULL,  -- JSON array
                response_ms   INTEGER NOT NULL,
                error         TEXT    DEFAULT NULL
            )
        """)


def log_chat(
    user_message: str,
    answer: str,
    sources: list[dict],
    response_ms: int,
    error: str | None = None,
) -> int:
    """Insert one chat interaction. Returns the new row id."""
    ts = datetime.now(timezone.utc).isoformat()
    with _connect() as con:
        cur = con.execute(
            """INSERT INTO chat_logs
               (timestamp, user_message, answer, sources, response_ms, error)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (ts, user_message, answer, json.dumps(sources), response_ms, error),
        )
        return cur.lastrowid


def get_logs(limit: int = 100, offset: int = 0) -> list[dict]:
    """Return recent chat logs as a list of dicts."""
    with _connect() as con:
        rows = con.execute(
            "SELECT * FROM chat_logs ORDER BY id DESC LIMIT ? OFFSET ?",
            (limit, offset),
        ).fetchall()
    result = []
    for row in rows:
        entry = dict(row)
        entry["sources"] = json.loads(entry["sources"])
        result.append(entry)
    return result
