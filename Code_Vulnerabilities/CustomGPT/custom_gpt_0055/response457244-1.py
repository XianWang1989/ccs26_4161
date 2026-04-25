
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to the smart card
def write_to_card(data):
    # List available readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    # Use the first available reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # APDU command to write data
    # Note: Replace with the correct APDU command according to your smart card specs
    apdu_write = [0x00, 0xE6, 0x00, 0x00, len(data)] + data
    response, sw1, sw2 = connection.transmit(apdu_write)

    print(f"Response: {toHexString(response)}")
    print(f"Status Words: {sw1:02X} {sw2:02X}")

# Example private key (format it according to your requirements)
private_key = b'\x30\x82\x01...'

# Write the private key to the smart card
write_to_card(private_key)
