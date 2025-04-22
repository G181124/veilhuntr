import hashlib

def get_passive_data(email):
    hash_email = hashlib.md5(email.strip().lower().encode()).hexdigest()
    gravatar_url = f"https://www.gravatar.com/avatar/{hash_email}"
    
    return {
        "email": email,
        "gravatar_url": gravatar_url,
        "note": "Jika URL mengembalikan gambar, kemungkinan gravatar aktif."
    }

# CLI test mode
if __name__ == "__main__":
    import argparse, json
    parser = argparse.ArgumentParser(description="Passive OSINT Gravatar Checker")
    parser.add_argument("--email", required=True, help="Email untuk cek gravatar")
    args = parser.parse_args()
    print(json.dumps(get_passive_data(args.email), indent=2))
