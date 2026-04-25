
from smartcard.System import readers
from smartcard.util import toHexString
import gnupg

# Initialize GPG
gpg = gnupg.GPG()

# List available readers
r = readers()
print(f"Available readers: {r}")

# Select the first available reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Print card information
print("Card:", toHexString(connection.getData()))

# Example command to write data to the card (this is a dummy command)
# Replace 'COMMAND' with the actual command for your specific smart card
# For writing private keys or data, this should be according to the card's specification
command = [0x00, 0xE6, 0x00, 0x00, 0x10]  # Modify this as necessary
data = bytearray(b'Some data')  # Replace with actual data to write

# Write data to smart card
connection.transmit(command + data)

# Check response
response, sw1, sw2 = connection.transmit(command + data)
print(f"Response: {toHexString(response)}, SW1: {sw1}, SW2: {sw2}")
