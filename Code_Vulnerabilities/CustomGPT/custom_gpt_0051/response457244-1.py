
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to smart card
def write_data_to_card(data):
    # Select the reader
    r = readers()
    reader = r[0]  # Choose the first reader
    connection = reader.createConnection()
    connection.connect()

    # Prepare your command to write data
    # Command example: 0xFF is used for proprietary commands, adjust as necessary.
    command = [0xFF, 0xD0, 0x00, 0x00, len(data)] + list(data)

    # Send command to the card
    response, sw1, sw2 = connection.transmit(command)

    # Check the status word
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully.")
    else:
        print(f"Error writing data: {toHexString([sw1, sw2])}")

# Example usage
if __name__ == "__main__":
    private_key_data = bytes([0x01, 0x02, 0x03, 0x04])  # Example data
    write_data_to_card(private_key_data)
