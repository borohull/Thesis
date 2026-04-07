#!/usr/bin/env python3
"""
crawler.py — Recursive web crawler for the ELTE IK RAG pipeline.

Crawls:
  - https://inf.elte.hu/  recursively (full domain)
  - 20 whitelisted page subtrees on www.elte.hu  (stay within each path prefix)

Usage:
    python crawler.py              # resumable crawl
    python crawler.py --reset      # wipe data/raw/ + data/processed/, then crawl
"""

import argparse
import re
import shutil
import time
from collections import deque
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse, unquote

import httpx
from bs4 import BeautifulSoup

# ── Directories ───────────────────────────────────────────────────────────────
ROOT_DIR = Path(__file__).parent
RAW_DIR  = ROOT_DIR / "data" / "raw"
PROC_DIR = ROOT_DIR / "data" / "processed"
PDF_DIR  = RAW_DIR / "linked_pdfs"

# ── Crawl configuration ───────────────────────────────────────────────────────
DELAY          = 0.5   # seconds between requests
REQUEST_TIMEOUT = 20.0  # seconds

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; ELTEThesisCrawler/1.0)",
    "Accept-Language": "en-US,en;q=0.9,hu;q=0.8",
}

# ── Seeds ─────────────────────────────────────────────────────────────────────
INF_SEEDS = ["https://inf.elte.hu/"]
INF_HOSTS = {"inf.elte.hu", "www.inf.elte.hu"}

ELTE_SEEDS = [
    "https://www.elte.hu/en/quaestura-office",
    "https://www.elte.hu/en/grant-for-EIT-Digital-master-students",
    "https://www.elte.hu/en/funding-for-students-from-the-usa",
    "https://www.elte.hu/en/current-students/christian-young-people",
    "https://www.elte.hu/en/students-at-risk",
    "https://www.elte.hu/en/current-students/diaspora",
    "https://www.elte.hu/en/current-students/stipendium-hungaricum",
    "https://www.elte.hu/en/visa-coordinator-contact",
    "https://www.elte.hu/en/for-non-eea-citizens-with-eu-residence-permits",
    "https://www.elte.hu/en/extension-of-residence-permit",
    "https://www.elte.hu/en/passive-student-status",
    "https://www.elte.hu/en/mentor",
    "https://www.elte.hu/en/arrange-housing",
    "https://www.elte.hu/en/student-finances",
    "https://www.elte.hu/en/about-hungary",
    "https://www.elte.hu/en/about-budapest",
    "https://www.elte.hu/en/in-case-of-emergency",
    "https://www.elte.hu/en/health-insurance",
    "https://www.elte.hu/en/neptun-administration-of-progress",
    "https://www.elte.hu/en/student-card",
]

# Whitelisted path prefixes derived from each elte.hu seed
ELTE_PREFIXES = [urlparse(s).path for s in ELTE_SEEDS]


# ── URL utilities ─────────────────────────────────────────────────────────────

def normalize_url(url: str) -> str:
    """Lowercase scheme+host, strip fragment and query, normalize trailing slash."""
    p = urlparse(url)
    path = p.path.rstrip("/") or "/"
    return urlunparse((p.scheme.lower(), p.netloc.lower(), path, "", "", ""))


def dedup_key(url: str) -> str:
    """Like normalize_url but also collapses www.inf.elte.hu → inf.elte.hu."""
    normed = normalize_url(url)
    p = urlparse(normed)
    host = p.netloc.replace("www.inf.elte.hu", "inf.elte.hu")
    return urlunparse((p.scheme, host, p.path, "", "", ""))


def is_allowed(url: str) -> bool:
    """Return True if url is within the crawl scope."""
    p = urlparse(url)
    if p.scheme not in ("http", "https"):
        return False
    host = p.netloc.lower().removeprefix("www.")
    if host == "inf.elte.hu":
        return True
    if host == "elte.hu":
        path = p.path
        return any(
            path == prefix or path.startswith(prefix + "/")
            for prefix in ELTE_PREFIXES
        )
    return False


def url_to_filename(url: str) -> str:
    """
    Map a URL to a flat .html filename under RAW_DIR.

    inf.elte.hu/en/students        →  en_students.html
    inf.elte.hu/                   →  index.html
    www.elte.hu/en/quaestura-office→  elte_en_quaestura-office.html
    """
    p = urlparse(url)
    host_bare = p.netloc.lower().removeprefix("www.")
    path = p.path.strip("/")

    if not path:
        path = "index"

    # Replace path separators and non-safe chars with underscores
    safe = re.sub(r"[^\w\-]", "_", path.replace("/", "_"))
    # Collapse multiple underscores
    safe = re.sub(r"_+", "_", safe).strip("_")

    if host_bare == "inf.elte.hu":
        return f"{safe}.html"
    else:
        return f"elte_{safe}.html"


def pdf_url_to_filename(url: str) -> str:
    """Extract and URL-decode the PDF filename from a URL."""
    name = unquote(Path(urlparse(url).path).name)
    if not name.lower().endswith(".pdf"):
        name += ".pdf"
    return name


# ── Fetch helpers ─────────────────────────────────────────────────────────────

def fetch_html(client: httpx.Client, url: str, dest: Path) -> tuple[str | None, str | None]:
    """
    Fetch a URL and save its HTML to dest.

    Returns (html_text, final_url_after_redirects) on success, (None, None) on skip/fail.
    Does NOT sleep — caller is responsible for DELAY.
    """
    try:
        resp = client.get(url, follow_redirects=True)
        resp.raise_for_status()
    except Exception as e:
        print(f"  [FAIL] {url}  ({e})")
        return None, None

    ctype = resp.headers.get("content-type", "")
    if "text/html" not in ctype:
        print(f"  [SKIP-TYPE] {url}  ({ctype.split(';')[0].strip()})")
        return None, None

    dest.write_bytes(resp.content)
    final_url = str(resp.url)
    print(f"  [SAVE] {url}  →  {dest.name}")
    return resp.text, final_url


def fetch_pdf(client: httpx.Client, url: str) -> None:
    """Download a PDF to PDF_DIR, skip if already exists."""
    dest = PDF_DIR / pdf_url_to_filename(url)
    if dest.exists():
        print(f"  [PDF-SKIP] {dest.name}")
        return
    try:
        resp = client.get(url, follow_redirects=True)
        resp.raise_for_status()
        dest.write_bytes(resp.content)
        print(f"  [PDF-SAVE] {url}  →  {dest.name}")
    except Exception as e:
        print(f"  [PDF-FAIL] {url}  ({e})")


# ── Link extraction ───────────────────────────────────────────────────────────

def extract_links(html: str, base_url: str) -> list[str]:
    """Return all absolute href links found in html, normalized."""
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if not href or href.startswith(("mailto:", "tel:", "javascript:")):
            continue
        abs_url = normalize_url(urljoin(base_url, href))
        links.append(abs_url)
    return links


# ── Main crawl loop ───────────────────────────────────────────────────────────

def crawl(client: httpx.Client) -> None:
    """BFS crawl of all seeds. Single loop handles both inf.elte.hu and elte.hu."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PDF_DIR.mkdir(parents=True, exist_ok=True)

    visited: set[str] = set()
    queue: deque[str] = deque(INF_SEEDS + ELTE_SEEDS)

    saved = skipped = failed = pdfs = 0

    while queue:
        url = queue.popleft()
        key = dedup_key(url)
        if key in visited:
            continue
        visited.add(key)

        dest = RAW_DIR / url_to_filename(url)

        if dest.exists():
            print(f"  [SKIP] {url}")
            skipped += 1
            # Parse the existing file to find links we may not have enqueued yet
            try:
                html = dest.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
        else:
            time.sleep(DELAY)
            html, final_url = fetch_html(client, url, dest)
            if html is None:
                if not dest.exists():
                    failed += 1
                    continue
                # File was skipped for content-type — don't follow links
                continue
            saved += 1
            # Redirect scope check: if we were redirected outside allowed domains, don't follow
            if final_url and not is_allowed(normalize_url(final_url)):
                continue

        # Enqueue discovered links
        for link in extract_links(html, url):
            link_key = dedup_key(link)
            if link_key in visited:
                continue
            if link.lower().endswith(".pdf") and is_allowed(link):
                time.sleep(DELAY)
                fetch_pdf(client, link)
                pdfs += 1
            elif is_allowed(link):
                queue.append(link)

    print(
        f"\nCrawl complete — saved: {saved}, skipped: {skipped}, "
        f"failed: {failed}, PDFs: {pdfs}"
    )


# ── Reset ─────────────────────────────────────────────────────────────────────

def reset_data() -> None:
    """Wipe data/raw/ and data/processed/ entirely."""
    for d in (RAW_DIR, PROC_DIR):
        if d.exists():
            shutil.rmtree(d)
            print(f"[RESET] Deleted {d}")
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROC_DIR.mkdir(parents=True, exist_ok=True)
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    print("[RESET] Directories recreated.")


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Crawl ELTE IK and whitelisted ELTE pages for the RAG pipeline."
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Wipe data/raw/ and data/processed/ before crawling.",
    )
    args = parser.parse_args()

    if args.reset:
        reset_data()

    with httpx.Client(headers=HEADERS, timeout=REQUEST_TIMEOUT) as client:
        crawl(client)


if __name__ == "__main__":
    main()
