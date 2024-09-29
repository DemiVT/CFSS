# Emulating an NFC card (Using Python or pseudo code)
import nfc
import time

def read_nfc_card():
    print("Hold NFC card near reader...")
    with nfc.ContactlessFrontend('usb') as clf:
        tag = clf.connect(rdwr={'on-connect': lambda tag: False})
        print("Card Data:", tag)

def emulate_nfc_card(card_data):
    print("Emulating NFC card...")
    while True:
        time.sleep(5)
        print(f"Emulating: {card_data}")

if __name__ == "__main__":
    card_data = read_nfc_card()
    emulate_nfc_card(card_data)
