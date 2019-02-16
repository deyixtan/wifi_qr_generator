
import argparse
import pyqrcode

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WIFI QR Code Generator")
    parser.add_argument("ssid")
    parser.add_argument("security", choices=["WEP", "WPA"])
    parser.add_argument("password")

    args = parser.parse_args()

    qr_text_raw = f"WIFI:S:{args.ssid};T:{args.security};P:{args.password};;"
    qr_code = pyqrcode.create(qr_text_raw)
    qr_code.png(f"{args.ssid}.png")
