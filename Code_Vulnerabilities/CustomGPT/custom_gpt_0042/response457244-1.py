
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to smart card
def write_to_card(data):
    # List available card readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    reader = r[0]
    print(f"Using reader: {reader}")

    # Connect to the smart card
    connection = reader.createConnection()
    connection.connect()

    # Example APDU command to write data
    # This command structure may vary based on your card's specifications
    # Replace 'data' with appropriate APDU format based on card instruction
    APDU_WRITE = [0x00, 0xD0, 0x00, 0x00, len(data)] + data

    # Send the command to the smart card
    response, sw1, sw2 = connection.transmit(APDU_WRITE)

    # Check response status word (SW)
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully!")
    else:
        print(f"Error writing data: {toHexString(response)} SW1: {sw1} SW2: {sw2}")

# Example private key data to write (ensure it's in the correct format)
private_key_data = bytearray.fromhex('YOUR_PRIVATE_KEY_HEX_HERE')

# Write the private key to the smart card
write_to_card(private_key_data)
