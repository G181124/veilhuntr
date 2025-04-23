# VeilHuntR Internal README

## Deskripsi

VeilHuntR adalah rangkaian tool berbasis CLI yang menggabungkan berbagai teknik profiling, analisis kerentanan, dan otomasi exploit berbasis CVE nyata. Semua fungsi dijalankan secara lokal, tanpa koneksi ke sistem otentikasi atau sumber daya eksternal. Semua aksi bersifat langsung terhadap data mentah atau respon HTTP dari target, dengan logika berbasis rule, pattern lokal, dan heuristic sederhana.

Tidak ada fitur yang bekerja secara simulatif. Seluruh output mencerminkan hasil aktual dari setiap eksekusi script terhadap input target yang diberikan.

## Struktur Direktori

```
veilhuntr/
├── veilhuntr.py
├── veilhuntr
├── requirements.txt
├── XPL0i7z/
│   ├── aut0spl0it/
│   ├── chainzploit/
│   ├── p4yl0adX/
│   ├── shellz/
│   ├── stealthZ/
│   └── vscanQ/
├── dEkWmz/
│   └── DeepHunt/
├── n9tLx0w/
│   ├── PwdSafe/
│   └── ScamWarn/
└── v3x9lZ/
    ├── A92kdP/
    ├── VJdk0a/
    ├── mZf11q/
    └── pDzkk2/
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

## Penggunaan

```bash
./veilhuntr --email someone@mail.com --profile someone --hunt
./veilhuntr --scan http://target --check-sqli --check-xss
./veilhuntr --gen-revshell --os linux --ip 10.10.10.10 --port 9001 --obfuscate shell.txt --base64 --xor
```

## Fitur Utama dan Penjelasan Teknis

### OSINT & Profiling
- `--email`: Validasi email secara format, lookup pattern, pencocokan gravatar hash (MD5 lokal), dan analisis dari email domain.
- `--phone`: Deteksi berdasarkan prefix, panjang angka, dan rule provider nasional.
- `--profile`: Pencarian username di daftar sumber online melalui pattern-based passive query.
- `--pwd`: Cek prefix hash terhadap dump lokal hasil potongan breached database (5 karakter pertama hash SHA1).
- `--hunt`: Korelasikan nama pengguna dan email untuk melihat apakah terdapat korespondensi, menyatukan hasil `--email` dan `--profile` untuk interpretasi lanjutan.

### Keamanan dan Stealth
- `--scam`: Cek URL terhadap pola phishing dari list karakteristik scam link. Cek tanda redirect, checksum hash URL, dan karakter non-standar.
- `--educate`: Menampilkan tips perlindungan digital non-teknis. Tidak ada output dinamis.
- `--stealth`: Menghapus riwayat `.bash_history`, mengganti PS1 prompt terminal, menonaktifkan autologging pada beberapa sistem shell.

### Eksploitasi
- `--sqli`: Uji pola SQLi pada parameter URL dengan menyisipkan string seperti `' OR 1=1--` lalu bandingkan panjang respon dan struktur.
- `--cmdinj`: Uji command injection dengan `;id`, `|whoami` dan lihat respon.
- `--lfi`: Coba traversal seperti `../../../../etc/passwd` dan cari keyword seperti `root:x:0:0` dalam respon.
- `--exploit`: Gabungkan sqli + xss + lfi.
- `--payload`: Kirimkan daftar payload statis dan cek jika respon berubah atau menunjukkan eksekusi.

### Modular CVE Exploit
- `--module CVE-ID TARGET`: Jalankan eksploit terhadap CVE tertentu seperti:
  - CVE-2017-8917: SQLi Joomla (cek response XPATH error)
  - CVE-2020-25213: WP File Manager (cek file upload dan eksekusi payload)
  - CVE-2022-26134: RCE di Atlassian (cek output `uid=`)

Jika target tidak rentan, output menyatakan "NOT vulnerable" namun payload tetap dikirim. Tidak ada status yang dipalsukan.

### Reverse Shell & Payload
- `--gen-revshell`: Generator payload berbasis OS. Output dalam bentuk script langsung (bash/perl/python).
- `--obfuscate`: Encode file payload secara XOR dan base64. Kombinasi opsional dan disimpan sebagai output terstruktur.

### Scanner
- `--scan`: Jalankan pemindaian berdasarkan parameter yang ditentukan. Gunakan `--check-*` untuk menentukan area spesifik.
- `--deep`: Tambahkan lapisan uji eksplorasi parameter kedua dari URL, crawling ringan (tanpa browser engine), dan query tambahan.

### Chain Mapping
- `--chainmap`: Terima data dalam format JSON (inline atau file) dan hasilkan alur rekomendasi aksi yang berurutan berdasarkan kehadiran field. Tidak menggunakan metode heuristik otomatisasi atau machine learning.

## Contoh Output

```json
{
  "url": "http://target",
  "sqli_check": "VULNERABLE",
  "xss_check": "NOT vulnerable",
  "lfi_check": null
}
```

## Catatan Internal

- `PwdSafe` menggunakan dump SHA1 hash lokal.
- `obfus_enc` menyimpan tiga bentuk hasil: original, xor_encoded, dan base64_encoded.
- `stealth_mode` melakukan modifikasi prompt terminal dan menyapu history, digunakan untuk pengujian CLI persistence tanpa jejak.
- Semua fitur eksploitasi menggunakan permintaan nyata dan akan tetap mencetak status NOT vulnerable jika eksploitasi tidak berhasil.

## Output Management

- Semua output dapat disimpan menggunakan `--save` ke direktori `output/{kategori}/`
- Format file `.txt` dengan timestamp.
