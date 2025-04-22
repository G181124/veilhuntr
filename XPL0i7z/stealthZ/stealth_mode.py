import random

PROXIES = [
    "http://104.248.63.17:30588",
    "http://103.216.82.18:6667",
    "http://51.158.68.133:8811",
]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
]

def activate_stealth():
    proxy = random.choice(PROXIES)
    user_agent = random.choice(USER_AGENTS)

    print("\n\033[1;35m[STEALTH MODE ENABLED]\033[0m")
    print(f"\033[1;34m[*] Proxy in use: {proxy}")
    print(f"[*] Spoofed User-Agent: {user_agent}\033[0m")
