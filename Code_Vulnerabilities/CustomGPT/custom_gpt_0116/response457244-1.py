
from smartcard.System import readers

# Function to write data to the smart card
def write_to_smart_card(data):
    try:
        # Get the list of readers
        r = readers()
        if not r:
            print("No smart card readers found.")
            return

        # Connect to the first reader
        reader = r[0]
        connection = reader.createConnection()
        connection.connect()

        # Define the APDU command to write data (example format)
        # Adjust the APDU based on your card's requirements
        apdu = [0xFF, 0xD6, 0x00, 0x00, len(data)] + list(data)

        # Send the APDU command to write data
        response, sw1, sw2 = connection.transmit(apdu)

        # Check the status word for success
        if sw1 == 0x90:
            print("Data written successfully.")
        else:
            print(f"Error writing data. SW1: {sw1}, SW2: {sw2}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
private_key = b'YOUR_PRIVATE_KEY_DATA'  # Replace with actual private key bytes
write_to_smart_card(private_key)
