
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to the smart card
def write_to_card(data):
    # Get the list of readers
    r = readers()
    if len(r) < 1:
        print("No smart card readers found.")
        return

    # Connect to the first reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Send command to write data
    # Convert the data to bytes (replace with your command structure)
    command = [0xFF, 0xD6, 0x00, 0x00, len(data)] + list(data)

    # Send the command
    data, sw1, sw2 = connection.transmit(command)

    # Check response status
    if sw1 == 0x90:
        print("Data written successfully:", toHexString(data))
    else:
        print("Error writing data, status word:", sw1, sw2)

# Example usage
private_key = b'YourPrivateKeyData'  # Replace with your actual private key data
write_to_card(private_key)
