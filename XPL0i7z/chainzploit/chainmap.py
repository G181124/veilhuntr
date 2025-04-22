import json

def generate_chainmap(data):
    chain = []

    if data.get("email"):
        chain.append("- Email diberikan sebagai input → Dapat digunakan untuk analisis breach & gravatar")
    
    if data.get("username"):
        chain.append("- Username terinput → Potensi penelusuran sosial media & profil online")
    
    if data.get("phone"):
        chain.append("- Nomor telepon dimasukkan → Bisa diperiksa untuk operator & kevalidan")

    if data.get("vulnerabilities"):
        vulns = data["vulnerabilities"]
        if vulns.get("sqli"):
            chain.append("- Flag SQLi ditandai dalam input → Eksploitasi SQL dapat dicoba")
        if vulns.get("lfi"):
            chain.append("- LFI terdeteksi → Akses file sensitif server")
        if vulns.get("cmdinj"):
            chain.append("- Flag Command Injection ditandai dalam input → Coba eksekusi perintah sistem")
    
    if not chain:
        chain.append("❔ Tidak ada jejak atau eksploitasi yang ditemukan.")

    return {
        "chainmap": chain,
        "recommendation": "🔁 Lanjutkan pengecekan manual atau uji eksploitasi tambahan jika perlu."
    }

if __name__ == "__main__":
    # Contoh uji coba lokal
    sample_data = {
        "email": "target@mail.com",
        "username": "targetuser",
        "phone": "085123456789",
        "vulnerabilities": {
            "sqli": True,
            "lfi": False,
            "cmdinj": True
        }
    }

    result = generate_chainmap(sample_data)
    print(json.dumps(result, indent=2, ensure_ascii=False))
