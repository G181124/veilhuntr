import requests

platforms = [
    "https://www.tiktok.com/@{}",
    "https://github.com/{}",
    "https://keybase.io/{}",
    "https://steamcommunity.com/id/{}",
    "https://instagram.com/{}",
    "https://pinterest.com/{}"
]

def trace_username(username):
    result = []
    headers = {"User-Agent": "Mozilla/5.0"}

    for url in platforms:
        full_url = url.format(username)
        try:
            response = requests.get(full_url, headers=headers, timeout=5)
            if response.status_code == 200:
                result.append({"platform": url.split("//")[1].split("/")[0], "url": full_url})
        except:
            continue

    return result
