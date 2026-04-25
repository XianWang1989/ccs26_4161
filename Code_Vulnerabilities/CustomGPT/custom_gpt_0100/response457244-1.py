
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to the smart card
def write_to_card(data):
    # Get the list of available card readers
    available_readers = readers()
    if not available_readers:
        print("No card readers found.")
        return

    # Select the first available reader
    reader = available_readers[0]
    print("Using reader:", reader)

    connection = reader.createConnection()
    connection.connect()

    print("Connected to card.")

    # APDU command to write data (modify according to your card's specifications)
    write_cmd = [0x00, 0xD0, 0x00, 0x00, len(data)] + list(data)

    # Send command to the card
    response, sw1, sw2 = connection.transmit(write_cmd)

    # Check status words for success
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully:", toHexString(data))
    else:
        print("Error writing data. SW1:", sw1, "SW2:", sw2)

    connection.disconnect()

# Example usage
if __name__ == "__main__":
    # Replace this with the data you want to write (as bytes)
    data_to_write = bytes.fromhex('DEADBEEF')
    write_to_card(data_to_write)
