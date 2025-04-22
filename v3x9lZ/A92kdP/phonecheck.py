import argparse
import re
import json

OPERATOR_PREFIXES = {
    "Telkomsel": ["0811", "0812", "0813", "0821", "0822", "0852", "0853", "0823"],
    "Indosat": ["0814", "0815", "0816", "0855", "0856", "0857", "0858"],
    "XL": ["0817", "0818", "0819", "0859", "0877", "0878"],
    "Tri": ["0895", "0896", "0897", "0898", "0899"],
    "Smartfren": ["0881", "0882", "0883", "0884", "0885", "0886", "0887", "0888", "0889"],
    "By.U": ["0851"]  # Khususkan 0851 sebagai By.U (sub-brand Telkomsel)
}

def normalize(phone):
    phone = re.sub(r'[^0-9]', '', phone)
    if phone.startswith("62"):
        phone = "0" + phone[2:]
    return phone

def detect_operator(phone):
    if phone.startswith("0851"):
        return "Telkomsel / By.U"
    for operator, prefixes in OPERATOR_PREFIXES.items():
        if any(phone.startswith(p) for p in prefixes):
            return operator
    return "Tidak diketahui"

def check_number(phone):
    normalized = normalize(phone)
    result = {
        "original_input": phone,
        "normalized": normalized,
        "valid_format": len(normalized) >= 10 and normalized.startswith("08"),
        "provider": detect_operator(normalized)
    }
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--phone", required=True)
    args = parser.parse_args()
    
    info = check_number(args.phone)
    print(json.dumps(info, indent=2))
