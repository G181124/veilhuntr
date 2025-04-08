#!/usr/bin/env python3
import argparse
import subprocess
import sys
import os
import json
from datetime import datetime

def run_module(path, args=None):
    command = ["python3", path]
    if args:
        command.extend(args)
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.stdout:
            print(f"\n=== Output dari {os.path.basename(path)} ===")
            try:
                output = json.loads(result.stdout)
                print(json.dumps(output, indent=2))
                return output
            except:
                print(result.stdout.strip())
                return result.stdout.strip()
    except Exception as e:
        print(f"❌ Gagal menjalankan {path}: {e}")
        return None

def save_output(data, prefix):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output_{prefix}_{now}.txt"
    with open(filename, "w") as f:
        if isinstance(data, str):
            f.write(data)
        else:
            f.write(json.dumps(data, indent=2))
    print(f"💾 Output disimpan di: {filename}")

def main():
    parser = argparse.ArgumentParser(description="VeilHuntR CLI Tool")
    parser.add_argument("--email", help="Investigasi email")
    parser.add_argument("--phone", help="Investigasi nomor telepon")
    parser.add_argument("--profile", help="Cek jejak online username")
    parser.add_argument("--leak", help="Cek data bocor (email/nomor/username)")
    parser.add_argument("--pwd", help="Cek password bocor")
    parser.add_argument("--scam", help="Deteksi link scam/phishing")
    parser.add_argument("--hunt", action="store_true", help="Korelasikan semua data")
    parser.add_argument("--stealth", action="store_true", help="Aktifkan stealth mode")
    parser.add_argument("--educate", action="store_true", help="Tampilkan tips perlindungan digital")
    parser.add_argument("--save", action="store_true", help="Simpan output ke file")

    args = parser.parse_args()
    all_output = []

    if args.email:
        print("📧 Investigasi Email:")
        all_output.append(run_module("v3x9lZ/mZf11q/emailcheck.py", ["--email", args.email]))
        all_output.append(run_module("v3x9lZ/mZf11q/breachlookup.py", ["--email", args.email]))
        all_output.append(run_module("v3x9lZ/mZf11q/passive_osint.py", ["--email", args.email]))

    if args.profile:
        print("\n👤 Jejak Profil:")
        all_output.append(run_module("v3x9lZ/2pDzkk/profiletrace.py", ["--user", args.profile]))

    if args.phone:
        print("\n📱 Cek Nomor Telepon:")
        all_output.append(run_module("v3x9lZ/A92kdP/phonecheck.py", ["--phone", args.phone]))

    if args.leak:
        print("\n🕵️ Leak Search:")
        all_output.append(run_module("v3x9lZ/VJdk0a/leaksearch.py", ["--query", args.leak]))

    if args.pwd:
        print("\n🔑 Cek Password Bocor:")
        all_output.append(run_module("9tLx0w/PwdSafe/pwdsafe.py", ["--pwd", args.pwd]))

    if args.scam:
        print("\n🚨 Scam/Phishing Detector:")
        all_output.append(run_module("9tLx0w/ScamWarn/scamwarn.py", ["--scam", args.scam]))

    if args.hunt:
        print("\n🔗 Korelasi Data:")
        hunt_args = []
        if args.email:
            hunt_args += ["--email", args.email]
        if args.phone:
            hunt_args += ["--phone", args.phone]
        if args.profile:
            hunt_args += ["--profile", args.profile]
        all_output.append(run_module("dEkWmz/DeepHunt/corehunt.py", hunt_args))

    if args.educate:
        tips = """
🛡️ Tips Perlindungan Digital:
- Gunakan password berbeda untuk tiap akun penting
- Aktifkan 2FA di akun email, sosial media, dan keuangan
- Jangan pakai tanggal lahir atau nama di password
- Selalu verifikasi link sebelum klik
- Gunakan password manager jika perlu
        """
        print(tips)
        all_output.append(tips)

    if args.save:
        save_output(all_output, "veilhuntr")

    if not any(vars(args).values()):
        parser.print_help()

if __name__ == "__main__":
    main()
