
from smartcard.System import readers
from smartcard.util import toBytes

# Define the private key (for demonstration, be careful with real keys)
private_key = "YOUR_PRIVATE_KEY"

def write_to_card(data):
    # Get the list of readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    # Select the first reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # APDU command to write data (this will vary based on your smart card's specifications)
    # Ensure your AEPC formulation matches the specification of your smart card
    WRITE_APDU = [0xFF, 0xD6, 0x00, 0x00, len(data)] + data

    # Convert data to bytes
    data_bytes = toBytes(data)

    try:
        # Send command to the card
        response, sw1, sw2 = connection.transmit(WRITE_APDU)
        print(f"Response: {response}, SW1: {sw1}, SW2: {sw2}")

        # Check if operation was successful
        if sw1 == 0x90 and sw2 == 0x00:
            print("Data written successfully.")
        else:
            print("Failed to write data to the card.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Write private key to smart card
write_to_card(private_key)
