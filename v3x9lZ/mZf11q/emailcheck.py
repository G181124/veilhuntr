import re
import dns.resolver
import socket

DISPOSABLE_DOMAINS = [
    "mailinator.com", "10minutemail.com", "tempmail.com", "guerrillamail.com",
    "trashmail.com", "yopmail.com", "getnada.com", "emailondeck.com"
]

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def is_valid_email(email):
    return EMAIL_REGEX.match(email) is not None


def get_mx_records(domain):
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        return sorted([str(r.exchange).rstrip('.') for r in answers])
    except Exception:
        return []


def is_disposable(domain):
    return domain.lower() in DISPOSABLE_DOMAINS


def email_info(email):
    result = {
        "email": email,
        "valid_format": False,
        "domain": None,
        "mx_records": [],
        "is_disposable": False
    }

    if not is_valid_email(email):
        return result

    result["valid_format"] = True
    domain = email.split("@")[-1]
    result["domain"] = domain
    result["is_disposable"] = is_disposable(domain)
    result["mx_records"] = get_mx_records(domain)

    return result


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Email Validator & MX Checker")
    parser.add_argument("--email", required=True, help="Target email to check")
    args = parser.parse_args()

    info = email_info(args.email)
    print(json.dumps(info, indent=2))
