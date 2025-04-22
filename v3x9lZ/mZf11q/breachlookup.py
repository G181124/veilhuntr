import requests

def breach_info(email, api_key):
    headers = {
        "hibp-api-key": api_key,
        "user-agent": "VeilHuntR-Checker"
    }
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            return {
                "email": email,
                "breached": True,
                "breaches": response.json(),
                "note": "Email ditemukan dalam basis data pelanggaran nyata (HIBP)."
            }
        elif response.status_code == 404:
            return {
                "email": email,
                "breached": False,
                "breaches": [],
                "note": "Email tidak ditemukan dalam basis data breach publik (HIBP)."
            }
        else:
            return {
                "email": email,
                "breached": None,
                "breaches": [],
                "note": f"Gagal mengakses HIBP API (status code: {response.status_code})"
            }

    except Exception as e:
        return {
            "email": email,
            "breached": None,
            "breaches": [],
            "note": f"Terjadi kesalahan saat koneksi ke HIBP: {str(e)}"
        }
