
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to the smart card
def write_to_card(data):
    # Get available readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Define your APDU command for writing
    # Here, 'XX' should be replaced with the actual command to write data
    apdu_command = [0xFF, 0xD6, 0x00, 0x00, len(data)] + list(data)

    # Send the APDU command
    response, sw1, sw2 = connection.transmit(apdu_command)

    print(f"Response: {toHexString(response)}")
    print(f"Status Words: {sw1:02X} {sw2:02X}")

# Example data (your private key in bytes)
private_key_data = b'\x30\x82\x01\x0a\x02\x01\x00\x02\x01\x01...'  # Replace with your actual key
write_to_card(private_key_data)
