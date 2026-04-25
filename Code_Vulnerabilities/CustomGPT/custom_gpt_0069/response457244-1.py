
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to the smart card
def write_data_to_card(data):
    # Get the list of readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    # Using the first available reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    print(f"Connected to: {reader}")

    # Example APDU command to write data (this needs to be modified according to your card's protocol)
    # Below is a placeholder example:
    apdu = [0xFF, 0xD6, 0x00, 0x00, len(data)] + list(data)

    # Sending the command to the card
    response, sw1, sw2 = connection.transmit(apdu)

    # Check the response status
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully.")
    else:
        print(f"Error writing data: SW1: {sw1}, SW2: {sw2}")

# Data to write (example)
data_to_write = bytes("Your data here", 'utf-8')
write_data_to_card(data_to_write)
