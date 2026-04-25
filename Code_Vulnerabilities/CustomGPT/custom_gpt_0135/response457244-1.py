
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to the smart card
def write_to_card(data):
    try:
        # Get the list of available readers
        r = readers()
        if not r:
            print("No smart card readers found.")
            return

        reader = r[0]
        connection = reader.createConnection()
        connection.connect()

        # APDU command for writing (example command)
        # Replace with appropriate command for writing private key
        apdu = [0xFF, 0xD6, 0x00, 0x00, len(data)]  # Write data command
        apdu += list(data)

        # Send the command to the card
        response, sw1, sw2 = connection.transmit(apdu)
        print(f"Response: {toHexString(response)}")
        print(f"Status words: {sw1:02X} {sw2:02X}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
private_key = b'YOUR_PRIVATE_KEY_HERE'  # Private key to write, in bytes
write_to_card(private_key)
