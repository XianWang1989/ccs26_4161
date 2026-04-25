
from smartcard.System import readers
from smartcard.util import toHexString

def write_data_to_card(data):
    # List available smart card readers
    r = readers()
    if not r:
        print("No card readers found.")
        return

    reader = r[0]  # Select the first reader
    connection = reader.createConnection()
    connection.connect()  # Connect to the smart card

    # Define the APDU command to write data (example)
    WRITE_APDU = [0xFF, 0xD0, 0x00, 0x00, len(data)] + list(data)

    # Send APDU command to the smart card
    response, sw1, sw2 = connection.transmit(WRITE_APDU)

    print(f"Response: {toHexString(response)}")
    print(f"Status Word: {sw1:02X} {sw2:02X}")

# Example usage
private_key_data = b'\x00\x01\x02\x03\x04\x05...'  # Replace with your actual private key bytes
write_data_to_card(private_key_data)
