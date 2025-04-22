import base64

def xor_encrypt(text, key="k"):
    return "".join(chr(ord(c) ^ ord(key)) for c in text)

def encode_payload(file_path, use_base64=False, use_xor=False):
    result = {
        "original": "",
        "base64_encoded": None,
        "xor_encoded": None,
        "combined": None
    }

    try:
        with open(file_path, "r") as f:
            payload = f.read().strip()
            result["original"] = payload

            if use_base64:
                b64 = base64.b64encode(payload.encode()).decode()
                result["base64_encoded"] = b64

            if use_xor:
                xor = xor_encrypt(payload)
                result["xor_encoded"] = "".join(f"\\x{ord(c):02x}" for c in xor)

            if use_base64 and use_xor:
                combined = xor_encrypt(base64.b64encode(payload.encode()).decode())
                result["combined"] = "".join(f"\\x{ord(c):02x}" for c in combined)

    except Exception as e:
        result["error"] = str(e)

    return result
