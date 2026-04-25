
from smartcard.System import readers
from smartcard.util import toHexString

# Initialize the reader
r = readers()
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Command to write a private key to the card
# Replace with appropriate command based on your smart card specification
# This is a placeholder command; you'll need to adapt it to your card's requirements.
command = [0xFF, 0xD6, 0x00, 0x00, 0x20]  # Example command with 0x20 bytes of data to write
private_key = bytes.fromhex('your_private_key_in_hex')

# Combine command and data to send to the card
data_to_send = command + list(private_key)

# Send the command to the card
response, sw1, sw2 = connection.transmit(data_to_send)

# Check the status word to see if the operation was successful
if sw1 == 0x90 and sw2 == 0x00:
    print("Private key written successfully.")
else:
    print(f"Error writing key: {toHexString(response)} (SW1: {sw1}, SW2: {sw2})")
