
from smartcard.System import readers
from smartcard.util import toHexString

def main():
    # List available readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    print("Available readers: ")
    for reader in r:
        print(reader)

    # Connect to the first reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Sample data to write (e.g., private key)
    key_data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'  # Replace with actual key data

    # APDU command to write data to the card (this is just an example)
    # The command structure can vary based on the card type
    apdu_write = [0xFF, 0xD6, 0x00, 0x00, len(key_data)] + list(key_data)

    # Send the APDU command
    try:
        response, sw1, sw2 = connection.transmit(apdu_write)
        print(f"Response: {toHexString(response)}")
        print(f"Status words: {sw1:02X} {sw2:02X}")
    except Exception as e:
        print(f"Error during writing: {e}")

    connection.disconnect()

if __name__ == "__main__":
    main()
