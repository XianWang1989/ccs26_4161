
from smartcard.System import readers
from smartcard.util import toHexString

def write_to_card(data):
    # Get the list of available readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    # Use the first available reader
    reader = r[0]
    print(f"Using reader: {reader}")

    # Connect to the smart card
    connection = reader.createConnection()
    connection.connect()

    # Data to write (proper formatting may be needed, e.g., APDU command)
    command = [0xFF, 0xD0, 0x00, 0x00, len(data)] + data

    # Send APDU command
    response, sw1, sw2 = connection.transmit(command)

    # Check for success (SW1 and SW2 status words)
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully.")
    else:
        print(f"Failed to write data: SW1={sw1}, SW2={sw2}")

    # Disconnect
    connection.disconnect()

# Example data to write (e.g., private key, in bytes)
private_key_data = [0xDE, 0xAD, 0xBE, 0xEF]  # Replace with actual key bytes
write_to_card(private_key_data)
