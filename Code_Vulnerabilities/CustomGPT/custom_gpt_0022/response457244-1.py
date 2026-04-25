
from smartcard.System import readers
from smartcard.util import setSmartCard

# Function to write data to smart card
def write_to_card(data):
    # Get the list of available readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    # Use the first reader
    reader = r[0]
    print(f"Using reader: {reader}")

    # Connect to the smart card
    connection = reader.createConnection()
    connection.connect()

    # Command to write data (assuming the card expects a specific command structure)
    WRITE_COMMAND = [0xFF, 0xD6, 0x00, 0x00, len(data)] + data
    response, sw1, sw2 = connection.transmit(WRITE_COMMAND)

    if sw1 == 0x90:  # SW1 indicates success
        print("Data written successfully.")
    else:
        print(f"Error while writing data: SW1: {sw1}, SW2: {sw2}")

# Example data to write (convert to bytes)
data_to_write = bytearray(b"Your data here")
write_to_card(data_to_write)
