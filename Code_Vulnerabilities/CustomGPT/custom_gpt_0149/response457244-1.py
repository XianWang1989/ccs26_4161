
from smartcard.System import readers
from smartcard.util import toBytes

def write_to_smart_card(data):
    # Find the smart card readers
    r = readers()
    if not r:
        print("No card readers found.")
        return

    reader = r[0]  # Select the first reader
    connection = reader.createConnection()
    connection.connect()

    # Convert the data to bytes
    data_bytes = toBytes(data)

    # Define your APDU command for writing (example command, adjust as needed)
    # Example APDU command to write data to the card
    command = [0xFF, 0xD6, 0x00, 0x00, len(data_bytes)] + list(data_bytes)

    # Send the APDU command
    response, sw1, sw2 = connection.transmit(command)

    if sw1 == 0x90:
        print("Data written successfully.")
    else:
        print("Error writing data: SW1 = {}, SW2 = {}".format(sw1, sw2))

# Example usage
data_to_write = "Your specific data here"
write_to_smart_card(data_to_write)
