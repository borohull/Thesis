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
                error         TEXT    DEFAULT NULL,
                session_id    TEXT    DEFAULT NULL
            )
        """)
        con.execute("""
            CREATE TABLE IF NOT EXISTS uploads (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp   TEXT    NOT NULL,
                file_name   TEXT    NOT NULL,
                sha256      TEXT    NOT NULL,
                size_bytes  INTEGER NOT NULL,
                chunk_count INTEGER NOT NULL,
                status      TEXT    NOT NULL
            )
        """)
        con.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                session_id  TEXT PRIMARY KEY,
                title       TEXT NOT NULL,
                created_at  TEXT NOT NULL,
                updated_at  TEXT NOT NULL
            )
        """)
        # Migrate existing chat_logs table if session_id column is missing
        try:
            con.execute("ALTER TABLE chat_logs ADD COLUMN session_id TEXT DEFAULT NULL")
        except sqlite3.OperationalError:
            pass  # column already exists


def log_chat(
    user_message: str,
    answer: str,
    sources: list[dict],
    response_ms: int,
    error: str | None = None,
    session_id: str | None = None,
) -> int:
    """Insert one chat interaction. Returns the new row id."""
    ts = datetime.now(timezone.utc).isoformat()
    with _connect() as con:
        cur = con.execute(
            """INSERT INTO chat_logs
               (timestamp, user_message, answer, sources, response_ms, error, session_id)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (ts, user_message, answer, json.dumps(sources), response_ms, error, session_id),
        )
        return cur.lastrowid


def upsert_session(session_id: str, first_message: str) -> None:
    """Create session on first message; update updated_at on subsequent ones."""
    title = first_message[:60] + ("…" if len(first_message) > 60 else "")
    ts = datetime.now(timezone.utc).isoformat()
    with _connect() as con:
        existing = con.execute(
            "SELECT session_id FROM sessions WHERE session_id = ?", (session_id,)
        ).fetchone()
        if existing is None:
            con.execute(
                "INSERT INTO sessions (session_id, title, created_at, updated_at) VALUES (?, ?, ?, ?)",
                (session_id, title, ts, ts),
            )
        else:
            con.execute(
                "UPDATE sessions SET updated_at = ? WHERE session_id = ?",
                (ts, session_id),
            )


def get_sessions(limit: int = 50) -> list[dict]:
    """Return recent sessions ordered by most recently updated."""
    with _connect() as con:
        rows = con.execute(
            "SELECT session_id, title, created_at, updated_at FROM sessions ORDER BY updated_at DESC LIMIT ?",
            (limit,),
        ).fetchall()
    return [dict(row) for row in rows]


def get_session_messages(session_id: str) -> list[dict]:
    """Return all chat messages for a session in chronological order."""
    with _connect() as con:
        rows = con.execute(
            "SELECT user_message, answer, sources, timestamp FROM chat_logs WHERE session_id = ? ORDER BY id ASC",
            (session_id,),
        ).fetchall()
    result = []
    for row in rows:
        entry = dict(row)
        entry["sources"] = json.loads(entry["sources"])
        result.append(entry)
    return result



def delete_session(session_id: str) -> None:
    """Delete a session and all its associated chat messages."""
    with _connect() as con:
        con.execute("DELETE FROM chat_logs WHERE session_id = ?", (session_id,))
        con.execute("DELETE FROM sessions WHERE session_id = ?", (session_id,))

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


def log_upload(
    file_name: str,
    sha256: str,
    size_bytes: int,
    chunk_count: int,
    status: str,
) -> int:
    """Insert one upload record. Returns the new row id."""
    init_db()
    ts = datetime.now(timezone.utc).isoformat()
    with _connect() as con:
        cur = con.execute(
            """INSERT INTO uploads
               (timestamp, file_name, sha256, size_bytes, chunk_count, status)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (ts, file_name, sha256, size_bytes, chunk_count, status),
        )
        return cur.lastrowid
