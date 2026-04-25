
from smartcard.System import readers
from smartcard.util import toHexString

# Select the smart card reader
r = readers()
print("Available readers:", r)

if not r:
    print("No smart card readers found.")
    exit()

reader = r[0]
connection = reader.createConnection()
connection.connect()

# Example command to write to the card
# Replace with your own APDU command formatted for your smart card
# This example assumes you're using a specific command for writing data
# Consult your smart card's documentation for the correct command format
data_to_write = bytearray([0x00, 0xD0, 0x00, 0x00])  # APDU command structure may vary
data_to_write.extend(b'Your data here')  # Add the actual data you want to write

# Send command to the card
response, sw1, sw2 = connection.transmit(data_to_write)

# Check response
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully.")
else:
    print("Error writing data:", toHexString(response), sw1, sw2)
