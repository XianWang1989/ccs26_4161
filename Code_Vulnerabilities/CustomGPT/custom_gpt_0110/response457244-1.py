
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to the smart card
def write_data_to_card(data):
    # Get the list of available readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    # Use the first reader
    reader = r[0]
    print(f"Using reader: {reader}")

    # Connect to the reader
    connection = reader.createConnection()
    connection.connect()

    # Define APDU command for writing data (this might differ based on your card)
    # Example command to write a value (replace with your actual command and data)
    apdu_command = [0xFF, 0xD0, 0x00, 0x00, len(data)] + list(data)

    # Send the command to the card
    response, sw1, sw2 = connection.transmit(apdu_command)

    print(f"Response: {toHexString(response)} - Status Words: {sw1:02X} {sw2:02X}")

# Replace with the actual byte representation of your private key
private_key_data = bytes([0x00, 0x01, 0x02, 0x03])  # Example data
write_data_to_card(private_key_data)
