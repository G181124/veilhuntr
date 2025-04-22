import argparse
import json
import urllib.parse
import requests
from bs4 import BeautifulSoup

def search_engine_query(engine_name, base_url, query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    url = base_url + urllib.parse.quote(query)
    try:
        res = requests.get(url, headers=headers, timeout=8)
        soup = BeautifulSoup(res.text, "html.parser")

        links = []
        for a in soup.find_all("a", href=True):
            href = a['href']
            # Hapus link non-informasi seperti gambar, script, icon
            if any(ext in href for ext in [".css", ".js", ".svg", ".ico", ".png", ".jpg"]):
                continue
            # Tanpa filter query
            links.append(href)

        return {
            "engine": engine_name,
            "result_count": len(links),
            "urls": links[:10]  # Batasi 10 saja
        }
    except Exception as e:
        return {
            "engine": engine_name,
            "error": str(e)
        }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True, help="Email atau keyword untuk pencarian bocoran")
    args = parser.parse_args()
    query = args.query

    results = []

    results.append(search_engine_query(
        "Google",
        "https://www.google.com/search?q=",
        query
    ))

    results.append(search_engine_query(
        "Bing",
        "https://www.bing.com/search?q=",
        query
    ))

    results.append(search_engine_query(
        "Yandex",
        "https://yandex.com/search/?text=",
        query
    ))

    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
