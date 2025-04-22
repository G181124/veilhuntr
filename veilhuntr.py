import argparse
import os
import json
import datetime
from v3x9lZ.mZf11q import emailcheck, passive_osint
from v3x9lZ.A92kdP import phonecheck
from v3x9lZ.pDzkk2 import profiletrace
from dEkWmz.DeepHunt import corehunt
from n9tLx0w.PwdSafe import pwdsafe
from n9tLx0w.ScamWarn import scamwarn
from XPL0i7z.stealthZ import stealth_mode
from XPL0i7z.aut0spl0it import auto_sqli, auto_cmdinj, auto_lfi, auto_exploit, auto_payload
from XPL0i7z.p4yl0adX import obfus_enc, revershell_gen
from XPL0i7z.vscanQ import scanalyzer
from XPL0i7z.chainzploit import chainmap

def print_banner():
    banner = "\033[1;36m" + r"""
 __     __   _ _ _   _             _   ____  
 \ \   / /__(_) | | | |_   _ _ __ | |_|  _ \ 
  \ \ / / _ \ | | |_| | | | | '_ \| __| |_) |
   \ V /  __/ | |  _  | |_| | | | | |_|  _ < 
    \_/ \___|_|_|_| |_|\__,_|_| |_|\__|_| \_\
""" + "\033[0m" + "\n\033[1;32m[ VEILHUNTR - OSINT & EXPLOITATION FRAMEWORK ]\n               [ Created By RL ]\033[0m\n"
    print(banner)

class CustomHelpParser(argparse.ArgumentParser):
    def print_help(self, *args, **kwargs):
        print_banner()
        super().print_help(*args, **kwargs)

def save_output(folder, filename, content):
    os.makedirs(f"output/{folder}", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = f"output/{folder}/{filename}_{timestamp}.txt"
    with open(filepath, "w") as f:
        f.write(content)
    print(f"\n\033[1;33m[+] Output disimpan di: {filepath}\033[0m")

def main():
    parser = CustomHelpParser(description="VeilHuntR CLI Tool")
    parser.add_argument("--email", help="Analisis email target")
    parser.add_argument("--phone", help="Cek informasi nomor telepon")
    parser.add_argument("--profile", help="Telusuri jejak online dari username")
    parser.add_argument("--pwd", help="Cek apakah password bocor")
    parser.add_argument("--scam", help="Deteksi kemungkinan link scam/phishing")
    parser.add_argument("--hunt", action="store_true", help="Korelasi email dan username")
    parser.add_argument("--stealth", action="store_true", help="Aktifkan stealth mode")
    parser.add_argument("--educate", action="store_true", help="Tampilkan tips perlindungan digital")
    parser.add_argument("--sqli", help="Uji kerentanan SQL Injection pada URL target")
    parser.add_argument("--cmdinj", help="Uji command injection pada target URL")
    parser.add_argument("--lfi", help="Uji Local File Inclusion (LFI) pada target URL")
    parser.add_argument("--exploit", help="Jalankan eksploitasi otomatis terhadap URL target")
    parser.add_argument("--payload", help="Uji payload otomatis terhadap URL target")
    parser.add_argument("--obfuscate", metavar="FILE", help="Obfuscate payload dari file")
    parser.add_argument("--xor", action="store_true", help="Aktifkan encoding XOR (digunakan dengan --obfuscate)")
    parser.add_argument("--base64", action="store_true", help="Aktifkan encoding base64 (digunakan dengan --obfuscate)")
    parser.add_argument("--scan", metavar="URL", help="Pindai target untuk celah umum (SQLi, XSS, LFI)")
    parser.add_argument("--check-sqli", action="store_true", help="Sertakan scan SQLi pada --scan")
    parser.add_argument("--check-xss", action="store_true", help="Sertakan scan XSS pada --scan")
    parser.add_argument("--check-lfi", action="store_true", help="Sertakan scan LFI pada --scan")
    parser.add_argument("--gen-revshell", action="store_true", help="Hasilkan reverse shell")
    parser.add_argument("--os", help="Sistem operasi target (linux/windows)", choices=["linux", "windows"])
    parser.add_argument("--deep", action="store_true", help="Aktifkan mode pemindaian mendalam saat menggunakan --scan")
    parser.add_argument("--chainmap", metavar="DATA", help="Susun urutan aksi berdasarkan data hasil OSINT dan eksploitasi (format JSON/file path)")
    parser.add_argument("--ip", help="IP listener untuk reverse shell")
    parser.add_argument("--port", help="Port listener untuk reverse shell")
    parser.add_argument("--save", action="store_true", help="Simpan output ke file")
    args = parser.parse_args()

    banner = "\033[1;36m" + r"""
 __     __   _ _ _   _             _   ____  
 \ \   / /__(_) | | | |_   _ _ __ | |_|  _ \ 
  \ \ / / _ \ | | |_| | | | | '_ \| __| |_) |
   \ V /  __/ | |  _  | |_| | | | | |_|  _ < 
    \_/ \___|_|_|_| |_|\__,_|_| |_|\__|_| \_\
""" + "\033[0m" + "\n\033[1;32m[ VEILHUNTR - OSINT & EXPLOITATION FRAMEWORK ]\n               [ Created By RL ]\033[0m\n"
    print(banner)

    if args.stealth:
        stealth_mode.activate_stealth()
        
    if args.email:
        print("\033[1;34m[EMAIL ANALYSIS]\033[0m\n")
        output = ""
        output += "=== Hasil dari emailcheck.py ===\n"
        output += json.dumps(emailcheck.email_info(args.email), indent=2) + "\n\n"
        output += "=== Hasil dari passive_osint.py ===\n"
        output += json.dumps(passive_osint.get_passive_data(args.email), indent=2)
        print(output)
        if args.save:
            save_output("email", "output_email", output)


    if args.phone:
        print("\n\033[1;34m[PHONE INFO CHECK]\033[0m")
        output = json.dumps(phonecheck.check_number(args.phone), indent=2)
        print(output)
        if args.save:
            save_output("phone", "output_phone", output)

    if args.profile:
        print("\n\033[1;34m[USERNAME TRACE]\033[0m")
        result = profiletrace.trace_username(args.profile)
        output = json.dumps(result, indent=2)
        print(output)
        if args.save:
            save_output("profile", "output_profile", output)

    if args.pwd:
        print("\n\033[1;34m[PASSWORD LEAK CHECK]\033[0m")
        result = pwdsafe.check_password(args.pwd)
        output = json.dumps(result, indent=2)
        print(output)
        if args.save:
            save_output("pwd", "output_pwd", output)

    if args.scam:
        print("\n\033[1;34m[SCAM / PHISHING LINK CHECK]\033[0m")
        result = scamwarn.check_url(args.scam)
        output = json.dumps(result, indent=2)
        print(output)
        if args.save:
            save_output("scam", "output_scam", output)

    if args.hunt and args.email and args.profile:
        print("\n\033[1;34m[DATA CORRELATION - DEEPHUNT]\033[0m\n")
        result = corehunt.deep_hunt(email=args.email, username=args.profile)
        output = json.dumps(result, indent=2)
        print(output)
        if args.save:
            save_output("hunt", "output_hunt", output)

    if args.sqli:
        print("\n\033[1;34m[SQL INJECTION SCAN]\033[0m")
        result = auto_sqli.scan_sql(args.sqli)
        output = json.dumps(result, indent=2)
        print(output)
        if args.save:
            save_output("sqli", "output_sqli", output)

    if args.cmdinj:
        print("\n\033[1;34m[COMMAND INJECTION SCAN]\033[0m")
        result = auto_cmdinj.scan_cmdinj(args.cmdinj)
        output = json.dumps(result, indent=2)
        print(output)
        if args.save:
            save_output("cmdinj", "output_cmdinj", output)

    if args.lfi:
        print("\n\033[1;34m[LOCAL FILE INCLUSION (LFI) SCAN]\033[0m")
        result = auto_lfi.scan_lfi(args.lfi)
        output = json.dumps(result, indent=2)
        print(output)
        if args.save:
            save_output("lfi", "output_lfi", output)

    if args.exploit:
        print("\n\033[1;34m[AUTO EXPLOIT SCAN]\033[0m")
        result = auto_exploit.scan_exploit(args.exploit)
        output = json.dumps(result, indent=2)
        print(output)
        if args.save:
            save_output("exploit", "output_exploit", output)

    if args.payload:
        print("\n\033[1;34m[AUTO PAYLOAD TEST]\033[0m")
        result = auto_payload.test_payload(args.payload)
        output = json.dumps(result, indent=2)
        print(output)
        if args.save:
            save_output("payload", "output_payload", output)

    if args.obfuscate:
        print("\n\033[1;34m[PAYLOAD OBFUSCATION]\033[0m")
        result = obfus_enc.encode_payload(args.obfuscate, use_base64=args.base64, use_xor=args.xor)
        output = json.dumps(result, indent=2)
        print(output)
        if args.save:
            save_output("obfuscate", "encoded_payload", output)

    if args.scan:
        print("\n\033[1;34m[VULNERABILITY SCANNER]\033[0m")
        result = scanalyzer.run_scan(args.scan, sqli=args.check_sqli, xss=args.check_xss, lfi=args.check_lfi)
        output = json.dumps(result, indent=2)
        print(output)
        if args.save:
            save_output("scan", "vuln_scan", output)

    if args.gen_revshell and args.os and args.ip and args.port:
        print("\n\033[1;34m[REVERSE SHELL GENERATOR]\033[0m")
        result = revershell_gen.generate_reverse_shell(args.os, args.ip, args.port, obfuscate=args.obfuscate)
        output = json.dumps(result, indent=2)
        print(output)
        if args.save:
            save_output("shellz", "revshell", output)
    
    if args.chainmap:
        print("\n\033[1;34m[CHAINMAP EXPLOIT LOGIC]\033[0m")
        try:
            if os.path.isfile(args.chainmap):
                with open(args.chainmap, "r") as f:
                    data = json.load(f)
            else:
                data = json.loads(args.chainmap)
            result = chainmap.generate_chainmap(data)
            output = json.dumps(result, indent=2, ensure_ascii=False)
            print(output)
            if args.save:
                save_output("chainmap", "exploit_chainmap", output)
        except Exception as e:
            print(f"❌ Gagal memproses chainmap: {e}")


    if args.educate:
        print("\n\033[1;34m[DIGITAL SECURITY TIPS]\033[0m")
        tips = [
            "- Gunakan password berbeda untuk tiap akun penting",
            "- Aktifkan 2FA di akun email, sosial media, dan keuangan",
            "- Jangan pakai tanggal lahir atau nama di password",
            "- Selalu verifikasi link sebelum klik",
            "- Gunakan password manager jika perlu",
        ]
        for tip in tips:
            print(tip)
        if args.save:
            save_output("educate", "tips", "\n".join(tips))

if __name__ == "__main__":
    main()
