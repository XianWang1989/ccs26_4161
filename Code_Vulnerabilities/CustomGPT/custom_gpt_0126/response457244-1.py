
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to the smart card
def write_data_to_card(data):
    # Get the list of available readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    # Connect to the first available reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Command to write data (replace with actual APDU command for your smart card)
    # Example: Writing data to a specific memory location on the card
    WRITE_COMMAND = [0xFF, 0xD6, 0x00, 0x00, len(data)] + data

    # Send the command to the card
    response, sw1, sw2 = connection.transmit(WRITE_COMMAND)

    # Check the response status
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully.")
    else:
        print(f"Failed to write data. Status words: {sw1}, {sw2}")

# Example usage: writing the GPG key data
# Convert the key data to bytes (this should be your actual private key data)
key_data = bytearray(b'YOUR_PRIVATE_KEY_DATA_HERE')  # replace with actual data
write_data_to_card(key_data)
