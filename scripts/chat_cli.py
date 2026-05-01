#!/usr/bin/env python3
"""
chat_cli.py — Interactive command-line client for the ELTE IK Assistant.

Usage:
    python scripts/chat_cli.py

Commands:
    /sessions          — list all past sessions
    /resume            — resume a previous session
    /model             — switch the active language model
    /session           — show the current session name and model
    exit / quit / Ctrl+C  — quit the client
"""

import sys
import uuid
import requests

BASE_URL = "http://127.0.0.1:8000"

BLUE  = "\033[94m"
CYAN  = "\033[96m"
BOLD  = "\033[1m"
DIM   = "\033[2m"
RESET = "\033[0m"

BANNER = f"""{BOLD}{BLUE}
  ███████╗██╗  ████████╗███████╗    ██╗██╗  ██╗
  ██╔════╝██║  ╚══██╔══╝██╔════╝    ██║██║ ██╔╝
  █████╗  ██║     ██║   █████╗      ██║█████╔╝
  ██╔══╝  ██║     ██║   ██╔══╝      ██║██╔═██╗
  ███████╗███████╗██║   ███████╗    ██║██║  ██╗
  ╚══════╝╚══════╝╚═╝   ╚══════╝    ╚═╝╚═╝  ╚═╝
{RESET}{CYAN}{BOLD}
        AI Assistant for ELTE Faculty of Informatics
{RESET}"""


# Server helpers

def check_server() -> bool:
    """Return True if the server is reachable and Ollama is running."""
    try:
        resp = requests.get(f"{BASE_URL}/health", timeout=5)
        data = resp.json()
        if not data.get("ollama"):
            print("ERROR: Server is running but Ollama is not available.")
            print("       Start Ollama with: ollama serve")
            return False
        return True
    except requests.exceptions.ConnectionError:
        print("ERROR: Cannot connect to the server.")
        print("       Start it with: uvicorn app.main:app")
        return False
    except requests.exceptions.Timeout:
        print("ERROR: Server did not respond in time.")
        return False


def get_models() -> list[str]:
    """Fetch available models from the server."""
    try:
        resp = requests.get(f"{BASE_URL}/models", timeout=5)
        resp.raise_for_status()
        return resp.json().get("models", [])
    except Exception:
        return []


def get_sessions() -> list[dict]:
    """Fetch all past sessions from the server."""
    try:
        resp = requests.get(f"{BASE_URL}/sessions", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return []


# Commands

def cmd_help() -> None:
    """Print all available commands."""
    commands = [
        ("/sessions",   "List all past sessions"),
        ("/resume",     "Resume a previous session"),
        ("/model",      "Switch the active language model"),
        ("/session",    "Show the current session name and model"),
        ("/commands",   "Show this help message"),
        ("exit / quit", "Quit the client"),
    ]
    print(f"\n{CYAN}  Available commands:{RESET}")
    for cmd, desc in commands:
        print(f"  {BOLD}{cmd:<16}{RESET} {DIM}{desc}{RESET}")
    print()


def cmd_list_sessions() -> None:
    """Print all past sessions."""
    sessions = get_sessions()
    if not sessions:
        print(f"{DIM}  No past sessions found.{RESET}\n")
        return
    print(f"\n{CYAN}  Past sessions:{RESET}")
    for i, s in enumerate(sessions, 1):
        updated = s.get("updated_at", "")[:10]
        print(f"  {BOLD}{i}.{RESET} {s['title']}  {DIM}({updated}){RESET}")
    print()


def cmd_resume() -> tuple[str, str] | tuple[None, None]:
    """
    Let the user pick a past session to resume.
    Returns (session_id, title) or (None, None) if cancelled.
    """
    sessions = get_sessions()
    if not sessions:
        print(f"{DIM}  No past sessions to resume.{RESET}\n")
        return None, None

    print(f"\n{CYAN}  Select a session to resume:{RESET}")
    for i, s in enumerate(sessions, 1):
        updated = s.get("updated_at", "")[:10]
        print(f"  {BOLD}{i}.{RESET} {s['title']}  {DIM}({updated}){RESET}")
    print(f"  {DIM}0. Cancel{RESET}\n")

    try:
        choice = input("  Enter number: ").strip()
        idx = int(choice)
        if idx == 0:
            return None, None
        if 1 <= idx <= len(sessions):
            s = sessions[idx - 1]
            return s["session_id"], s["title"]
        print("  Invalid selection.\n")
        return None, None
    except (ValueError, KeyboardInterrupt):
        return None, None


def cmd_select_model(current_model: str) -> str:
    """
    Let the user pick a model from the available list.
    Returns the chosen model name, or the current model if cancelled.
    """
    models = get_models()
    if not models:
        print(f"{DIM}  No models found. Is Ollama running?{RESET}\n")
        return current_model

    print(f"\n{CYAN}  Available models:{RESET}")
    for i, m in enumerate(models, 1):
        marker = f" {CYAN}(active){RESET}" if m == current_model else ""
        print(f"  {BOLD}{i}.{RESET} {m}{marker}")
    print(f"  {DIM}0. Cancel{RESET}\n")

    try:
        choice = input("  Enter number: ").strip()
        idx = int(choice)
        if idx == 0:
            return current_model
        if 1 <= idx <= len(models):
            chosen = models[idx - 1]
            print(f"  Switched to {BOLD}{chosen}{RESET}\n")
            return chosen
        print("  Invalid selection.\n")
        return current_model
    except (ValueError, KeyboardInterrupt):
        return current_model


# Ask

def ask(question: str, session_id: str, model: str) -> None:
    """Send a question to the server and print the answer and sources."""
    try:
        resp = requests.post(
            f"{BASE_URL}/chat",
            json={"message": question, "session_id": session_id, "model": model},
            timeout=120,
        )
        resp.raise_for_status()
        data = resp.json()

        print(f"\nBot: {data['answer']}")

        sources = data.get("sources", [])
        if sources:
            unique_files = sorted({s["file"] for s in sources})
            print(f"\n{DIM}Sources: {', '.join(unique_files)}{RESET}")

        print(f"\n{BLUE}{'─' * 50}{RESET}\n")

    except requests.exceptions.Timeout:
        print("\nERROR: The request timed out. The model may still be loading.")
        print("       Try again in a few seconds.\n")
    except requests.exceptions.ConnectionError:
        print("\nERROR: Lost connection to the server.\n")
    except requests.exceptions.HTTPError as e:
        print(f"\nERROR: Server returned {e.response.status_code}.")
        try:
            detail = e.response.json().get("detail", "")
            if detail:
                print(f"       {detail}")
        except Exception:
            pass
        print()
    except (KeyError, ValueError):
        print("\nERROR: Unexpected response from server.\n")


# Main

def main() -> None:
    print(BANNER)
    print(f"{CYAN}  Type your question and press Enter. Type /commands for help.{RESET}")
    print(f"{BLUE}  {'─' * 48}{RESET}\n")

    if not check_server():
        sys.exit(1)

    # Default session and model
    session_id   = str(uuid.uuid4())
    session_name = "New session"
    model        = "llama3.2:3b"

    print(f"  {DIM}Session: {session_name}  |  Model: {model}{RESET}\n")

    while True:
        try:
            q = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye.")
            sys.exit(0)

        if not q:
            continue

        # built-in commands
        if q.lower() in {"exit", "quit"}:
            print("Goodbye.")
            sys.exit(0)

        if q.lower() == "/commands":
            cmd_help()
            continue

        if q.lower() == "/sessions":
            cmd_list_sessions()
            continue

        if q.lower() == "/resume":
            new_id, new_name = cmd_resume()
            if new_id:
                session_id   = new_id
                session_name = new_name
                print(f"  {DIM}Resumed: {session_name}{RESET}\n")
            continue

        if q.lower() == "/model":
            model = cmd_select_model(model)
            continue

        if q.lower() == "/session":
            print(f"\n  {DIM}Session: {session_name}  |  Model: {model}{RESET}\n")
            continue

        # regular question
        ask(q, session_id, model)


if __name__ == "__main__":
    main()