import requests

def check_url(url):
    result = {
        "url": url,
        "is_suspicious": False,
        "reasons": [],
        "status_code": None
    }

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        result["status_code"] = response.status_code

        # Heuristik sederhana
        if response.status_code in [403, 404, 500]:
            result["is_suspicious"] = True
            result["reasons"].append("Status code mencurigakan")

        if any(domain in url.lower() for domain in ["freegift", "login-now", "bonus", "claim", "bit.ly", "rb.gy", "tinyurl.com"]):
            result["is_suspicious"] = True
            result["reasons"].append("URL mengandung pola umum scam/phishing")

        if "Set-Cookie" in response.headers and "secure" not in response.headers.get("Set-Cookie", "").lower():
            result["is_suspicious"] = True
            result["reasons"].append("Cookie tidak aman")

    except requests.exceptions.RequestException as e:
        result["is_suspicious"] = True
        result["reasons"].append(f"Gagal diakses: {str(e)}")

    return result

# Untuk pengujian mandiri
if __name__ == "__main__":
    import argparse
    import json
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    args = parser.parse_args()
    print(json.dumps(check_url(args.url), indent=2))
