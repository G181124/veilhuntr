import socket

def start_listener(port):
    try:
        s = socket.socket()
        s.bind(("0.0.0.0", int(port)))
        s.listen(1)
        print(f"🎧 Listening on port {port}...")

        conn, addr = s.accept()
        print(f"⚡ Connection from {addr[0]}")

        while True:
            cmd = input("$ ")
            if cmd.strip().lower() in ["exit", "quit"]:
                break
            conn.send(cmd.encode() + b"\n")
            data = conn.recv(4096)
            print(data.decode(errors='ignore'))

        conn.close()
    except Exception as e:
        print(f"❌ Listener error: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", required=True)
    args = parser.parse_args()

    start_listener(args.port)
