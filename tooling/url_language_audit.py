"""
URL language audit — for bilingual (EN/ES) marketing sites.

Crawls a site, then flags URLs whose SLUG language does not match their
CONTENT language (the classic i18n debt: English slugs serving Spanish pages).
Outputs a CSV with a proposed localized slug for each mismatch.

Anonymized portfolio version: pass the target domain via --domain.
No client data or hard-coded URLs are included.

Usage:
    python url_language_audit.py --domain https://www.example.com --es-prefix /es

Dependencies:
    pip install requests beautifulsoup4
"""
import argparse
import csv
import time
from collections import deque
from urllib.parse import urljoin, urlparse, unquote

import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; GEOAuditBot/1.0)"}

# --- Language signals -------------------------------------------------------
SPANISH_TOKENS = {
    "mejorar", "mejores", "mejor", "visibilidad", "ia", "monitorizar",
    "investigacion", "analisis", "sentimiento", "marca", "marcas",
    "soluciones", "agencias", "que", "confian", "en", "de", "para", "con",
    "plataformas", "comparativa", "guia", "busqueda", "como", "herramientas",
}
ENGLISH_TOKENS = {
    "best", "alternatives", "tracking", "tracker", "tool", "tools", "checker",
    "how", "to", "improve", "brand", "visibility", "customer", "stories",
    "compare", "vs", "knowledge", "base", "answer", "ranking", "citation",
    "citations", "content", "sentiment", "share", "voice", "source", "trust",
    "signals", "search", "engine", "generative", "for", "the", "and", "of",
    "your", "optimization", "score", "rate", "coverage", "design", "mentions",
}
ACCENTS = set("áéíóúñ¿¡ü")
ES_STOP = {"de", "la", "el", "los", "las", "en", "para", "con", "que", "como",
           "una", "un", "y", "tu", "por", "más", "qué", "cómo", "guía"}
EN_STOP = {"the", "of", "for", "how", "to", "your", "and", "with", "what",
           "best", "from", "guide"}


def slug_language(path, es_prefix):
    p = unquote(path)
    if p.startswith(es_prefix):
        p = p[len(es_prefix):]
    tokens = [t.lower() for t in p.replace("/", "-").split("-") if t]
    es = sum(1 for t in tokens if t in SPANISH_TOKENS)
    en = sum(1 for t in tokens if t in ENGLISH_TOKENS)
    if es > en:
        return "ES"
    if en > es:
        return "EN"
    return "NEUTRO" if (es == 0 and en == 0) else "MIXTO"


def content_language(title, desc):
    text = f"{title} {desc}".lower()
    if any(c in ACCENTS for c in text):
        return "ES"
    words = set(text.replace("|", " ").split())
    es, en = len(words & ES_STOP), len(words & EN_STOP)
    if es > en:
        return "ES"
    if en > es:
        return "EN"
    return "ES" if es else "?"


def crawl(domain, es_prefix, delay=0.4, max_pages=2000):
    host = urlparse(domain).netloc
    seeds = [domain.rstrip("/") + "/", domain.rstrip("/") + es_prefix]

    def norm(u):
        pp = urlparse(u)
        return domain.rstrip("/") + (pp.path.rstrip("/") or "/")

    visited, queue = {}, deque(norm(s) for s in seeds)
    while queue and len(visited) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue
        try:
            r = requests.get(url, headers=HEADERS, timeout=15)
        except Exception:
            visited[url] = {"status": "ERR", "title": "", "desc": ""}
            continue
        title = desc = ""
        if "text/html" in r.headers.get("content-type", ""):
            soup = BeautifulSoup(r.text, "html.parser")
            if soup.title:
                title = soup.title.get_text(strip=True)
            h1 = soup.find("h1")
            desc = h1.get_text(strip=True) if h1 else ""
            for a in soup.find_all("a", href=True):
                nxt = norm(urljoin(url, a["href"].split("#")[0]))
                if urlparse(nxt).netloc == host and nxt not in visited:
                    queue.append(nxt)
        visited[url] = {"status": r.status_code, "title": title, "desc": desc}
        print(f"[{r.status_code}] {url}  ({len(visited)} done, {len(queue)} queued)")
        time.sleep(delay)
    return visited


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", required=True, help="e.g. https://www.example.com")
    ap.add_argument("--es-prefix", default="/es")
    ap.add_argument("--out", default="url_language_audit.csv")
    args = ap.parse_args()

    pages = crawl(args.domain, args.es_prefix)

    rows = []
    for url, meta in sorted(pages.items()):
        if args.es_prefix not in urlparse(url).path:
            continue  # focus on the localized tree
        slug_lang = slug_language(urlparse(url).path, args.es_prefix)
        cont_lang = content_language(meta["title"], meta["desc"])
        flag = "SI" if (slug_lang == "EN" and cont_lang == "ES") else ""
        rows.append({
            "url": url,
            "slug_language": slug_lang,
            "content_language": cont_lang,
            "needs_localization": flag,
            "status": meta["status"],
            "title": meta["title"],
        })

    rows.sort(key=lambda r: (0 if r["needs_localization"] == "SI" else 1, r["url"]))
    with open(args.out, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    flagged = sum(1 for r in rows if r["needs_localization"] == "SI")
    print(f"\nDone. {len(rows)} localized URLs · {flagged} need slug localization → {args.out}")


if __name__ == "__main__":
    main()
