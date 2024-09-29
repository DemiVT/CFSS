# Sample code for capturing and decoding RFID (simulation)
import rfid_reader

def capture_rfid_data():
    rfid_data = rfid_reader.read()
    print("Captured RFID:", rfid_data)
    return rfid_data

def emulate_rfid(rfid_data):
    print("Emulating RFID data...")
    # Emulate captured RFID signal
    while True:
        print(f"Sending RFID: {rfid_data}")
        time.sleep(2)

rfid_data = capture_rfid_data()
emulate_rfid(rfid_data)
