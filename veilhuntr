#!/usr/bin/env python3
import argparse
import subprocess
import sys
import os
from datetime import datetime

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

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()

if __name__ == "__main__":
    main()
