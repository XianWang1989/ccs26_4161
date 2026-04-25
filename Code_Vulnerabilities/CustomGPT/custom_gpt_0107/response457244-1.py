
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to the smart card
def write_data_to_card(data):
    # Find all the card readers
    r = readers()
    if not r:
        print("No card readers found.")
        return

    # Use the first available reader
    reader = r[0]
    print(f"Using reader: {reader}")

    # Connect to the card
    connection = reader.createConnection()
    connection.connect()

    # Prepare the command to write data (example APDU command)
    # Change this according to your card's specifications
    command = [0xFF, 0xD6, 0x00, 0x00, len(data)] + list(data)

    # Send the command to the card
    response, sw1, sw2 = connection.transmit(command)

    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully.")
    else:
        print(f"Error writing data: SW1={sw1:02X}, SW2={sw2:02X}")

    # Disconnect the card
    connection.disconnect()

if __name__ == "__main__":
    # Example data to write (as bytes)
    data_to_write = bytes([0x01, 0x02, 0x03, 0x04])
    write_data_to_card(data_to_write)
