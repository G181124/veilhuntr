# VeilHuntR

VeilHuntR adalah tool berbasis CLI yang bisa digunakan langsung lewat terminal untuk mengumpulkan informasi dan menguji target dari berbagai sisi. Cocok dipakai dalam berbagai tahap eksplorasi, pengecekan celah, dan simulasi eksekusi payload.

## Fitur Utama

- Cek informasi dari email, username, atau nomor telepon
- Cari tahu apakah password pernah bocor
- Uji celah umum seperti SQLi, LFI, dan command injection
- Jalankan eksploitasi otomatis ke URL target
- Tes payload seperti XSS dan path traversal
- Obfuscate payload dengan base64 atau XOR
- Buat reverse shell yang bisa langsung dipakai
- Scan URL untuk mendeteksi potensi celah
- Susun urutan langkah eksploitasi dengan chainmap
- Jalankan exploit berbasis CVE yang tersedia langsung dari tool

## Contoh Penggunaan

```bash
# Telusuri profil online berdasarkan username
./veilhuntr --profile johndoe

# Cek apakah password bocor
./veilhuntr --pwd "hunter2"

# Scan SQL injection
./veilhuntr --sqli "http://target.com/page.php?id=1"

# Eksekusi otomatis exploit terhadap target
./veilhuntr --exploit "http://testphp.vulnweb.com/listproducts.php?cat=1"

# Obfuscasi payload
./veilhuntr --obfuscate shellcode.txt --xor --base64

# Buat reverse shell
./veilhuntr --gen-revshell --os linux --ip 192.168.1.10 --port 4444
```

## Instalasi

```bash
git clone https://github.com/G181124/veilhuntr
cd veilhuntr
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
chmod +x veilhuntr
```
