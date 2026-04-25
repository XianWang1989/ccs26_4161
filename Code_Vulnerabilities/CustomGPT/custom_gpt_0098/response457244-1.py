
from smartcard.System import readers
from smartcard.util import toBytes

# Function to write data to smart card
def write_to_smartcard(data):
    # List available readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    # Connect to the first available reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Command to write to the card (example APDU command)
    # Adjust the APDU command to match your card's specifications
    command = [0xFF, 0xD6, 0x00, 0x00, len(data)]  # Write command
    command += toBytes(data)

    # Sending command to the card
    response, sw1, sw2 = connection.transmit(command)

    # Check the response status
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully.")
    else:
        print(f"Failed to write data: SW1={sw1}, SW2={sw2}")

# Example usage
private_key = "your_private_key_here"  # Replace with your actual key
write_to_smartcard(private_key)
