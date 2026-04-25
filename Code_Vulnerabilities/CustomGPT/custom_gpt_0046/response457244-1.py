
from smartcard.System import readers
from smartcard.util import toBytes

# Initialize the reader
r = readers()
reader = r[0]  # Select the first reader

connection = reader.createConnection()
connection.connect()

# Define the command to write data to the card
# The following command is just an example; actual commands depend on your card and protocol used.
write_command = [0xFF, 0xD0, 0x00, 0x00, 0x20]  # APDU command to write data (modified as needed)

# Your private key data as bytes (ensure proper formatting)
private_key_data = b'YOUR_PRIVATE_KEY_HERE'  # Replace with your actual private key

# Send multiple commands if the data exceeds APDU size
for i in range(0, len(private_key_data), 255):
    chunk = private_key_data[i:i + 255]
    command = write_command + list(chunk)
    response, sw1, sw2 = connection.transmit(command)

    if sw1 == 0x90:  # Check for success status word
        print(f'Successfully wrote chunk: {chunk.hex()}')
    else:
        print(f'Failed to write chunk: {chunk.hex()} with SW1: {sw1} SW2: {sw2}')

connection.disconnect()
