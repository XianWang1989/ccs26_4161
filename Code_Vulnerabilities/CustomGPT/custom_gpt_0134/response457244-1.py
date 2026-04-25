
from smartcard.System import readers
from smartcard.util import toBytes

def main():
    # Find available readers
    r = readers()
    if len(r) < 1:
        print("No smart card readers found.")
        return

    # Connect to the first available reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Your private key as bytes (e.g., use your actual private key)
    private_key_hex = "your_private_key_in_hex"
    private_key_bytes = toBytes(private_key_hex)

    # APDU command to write data to the smart card
    # This is a generic example. Modify this based on your card specifications.
    WRITE_COMMAND = [0xFF, 0xD0, 0x00, 0x00, len(private_key_bytes)] + list(private_key_bytes)

    # Send command to write private key
    response, sw1, sw2 = connection.transmit(WRITE_COMMAND)

    # Check response status
    if sw1 == 0x90 and sw2 == 0x00:
        print("Private key written successfully.")
    else:
        print(f"Failed to write private key. Status words: {sw1:02X} {sw2:02X}")

if __name__ == "__main__":
    main()
