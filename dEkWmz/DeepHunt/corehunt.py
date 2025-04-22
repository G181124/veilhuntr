import json
from v3x9lZ.mZf11q import emailcheck, passive_osint
from v3x9lZ.pDzkk2 import profiletrace

def deep_hunt(email=None, username=None):
    result = {
        "email_analysis": {},
        "gravatar_data": {},
        "username_trace": []
    }

    if email:
        result["email_analysis"] = emailcheck.email_info(email)
        result["gravatar_data"] = passive_osint.get_passive_data(email)

    if username:
        result["username_trace"] = profiletrace.trace_username(username)

    return result
