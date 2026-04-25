
from smartcard.System import readers
from smartcard.util import toBytes

# Function to write data to smart card
def write_to_smart_card(data):
    # Get the list of available readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    # Connect to the first available reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Prepare the data to write (convert string to bytes)
    data_bytes = toBytes(data)

    # Command to write to the smart card (example command, adjust based on your card)
    WRITE_COMMAND = [0xFF, 0xE6, 0x00, 0x00] + data_bytes

    # Send the command to the card
    response, sw1, sw2 = connection.transmit(WRITE_COMMAND)

    # Check if the write was successful
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully.")
    else:
        print(f"Error writing data: SW1={sw1}, SW2={sw2}")

# Example usage
private_key_data = "YOUR_PRIVATE_KEY_HERE"
write_to_smart_card(private_key_data)
