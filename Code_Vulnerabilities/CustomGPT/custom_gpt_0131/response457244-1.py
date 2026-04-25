
from smartcard.System import readers
from smartcard.util import toBytes

# Function to write data to the card
def write_to_card(data):
    r = readers()
    if not r:
        print("No card readers found")
        return

    reader = r[0]  # Use the first reader found
    connection = reader.createConnection()
    connection.connect()

    # Convert your data to bytes
    data_bytes = toBytes(data)

    # Command to write to the card (example command)
    # This will depend on your card specifications
    command = [0xFF, 0xD6, 0x00, 0x00, len(data_bytes)] + list(data_bytes)

    try:
        response, sw1, sw2 = connection.transmit(command)
        if sw1 == 0x90:  # 0x90 indicates success
            print("Data written successfully")
        else:
            print(f"Error writing data: SW1: {sw1}, SW2: {sw2}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
private_key = "your_private_key_data"  # Replace with your actual private key data
write_to_card(private_key)
