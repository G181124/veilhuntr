import argparse
import requests

common_paths = [
    ".env", "admin", "phpinfo.php", "backup.zip", "db.sql", ".git", ".htaccess",
    "config.php", "config.json", "web.config", "readme.md", "setup.php"
]

def scan_common_vuln_paths(base_url):
    found = []
    for path in common_paths:
        url = base_url.rstrip("/") + "/" + path
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                found.append({"path": path, "url": url, "status": 200})
        except:
            continue
    return {
        "url": base_url,
        "vulnerable_paths_found": found
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    args = parser.parse_args()
    result = scan_common_vuln_paths(args.url)
    print(result)
