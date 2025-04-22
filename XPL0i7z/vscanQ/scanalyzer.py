import requests

def run_scan(url, sqli=False, xss=False, lfi=False):
    results = {
        "url": url,
        "sqli_check": None,
        "xss_check": None,
        "lfi_check": None
    }

    if sqli:
        test_url = url + "'"
        try:
            r = requests.get(test_url, timeout=5)
            if "sql" in r.text.lower() or "syntax" in r.text.lower():
                results["sqli_check"] = "VULNERABLE"
            else:
                results["sqli_check"] = "Not Vulnerable"
        except:
            results["sqli_check"] = "Error"

    if xss:
        test_url = url + "<script>alert(1)</script>"
        try:
            r = requests.get(test_url, timeout=5)
            if "<script>alert(1)</script>" in r.text:
                results["xss_check"] = "VULNERABLE"
            else:
                results["xss_check"] = "Not Vulnerable"
        except:
            results["xss_check"] = "Error"

    if lfi:
        test_url = url + "../../../../etc/passwd"
        try:
            r = requests.get(test_url, timeout=5)
            if "root:x:" in r.text:
                results["lfi_check"] = "VULNERABLE"
            else:
                results["lfi_check"] = "Not Vulnerable"
        except:
            results["lfi_check"] = "Error"

    return results
