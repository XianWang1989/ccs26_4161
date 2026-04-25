
from smartcard.System import readers
from smartcard.util import toBytes

# Select the smart card reader
r = readers()
if not r:
    print("No smart card readers found.")
    exit()

# Connect to the reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# APDU command to write data (example)
# Replace this with the appropriate command for your smart card
# This example assumes you're writing an ASCII string

# Example data to write (e.g., your GPG private key)
data_to_write = "YOUR_PRIVATE_KEY_HERE"
apdu_command = [0xFF, 0xD6, 0x00, 0x00] + list(toBytes(data_to_write))

# Send the command to the smart card
response, sw1, sw2 = connection.transmit(apdu_command)

# Check the response
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully.")
else:
    print(f"Failed to write data. Status words: {sw1:02X} {sw2:02X}")

# Disconnect
connection.disconnect()
