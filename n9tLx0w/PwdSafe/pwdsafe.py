import hashlib
import requests

def check_password(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return {"error": "Gagal mengakses API HIBP"}
        hashes = response.text.splitlines()
        for line in hashes:
            h_suffix, count = line.split(":")
            if h_suffix == suffix:
                return {
                    "password": password,
                    "breached": True,
                    "breach_count": int(count),
                    "hash_prefix": prefix,
                    "note": "Password ditemukan dalam data breach asli (HIBP)"
                }
        return {
            "password": password,
            "breached": False,
            "hash_prefix": prefix,
            "note": "Password aman, tidak ditemukan di database breach HIBP"
        }
    except Exception as e:
        return {"error": str(e)}
