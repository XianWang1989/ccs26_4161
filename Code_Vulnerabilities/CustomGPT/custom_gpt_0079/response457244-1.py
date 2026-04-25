
from smartcard.System import readers
from smartcard.util import toHexString

# Get the list of available card readers
r = readers()
print("Available readers:", r)

# Select the first reader
if not r:
    print("No card readers available.")
    exit()

reader = r[0]
connection = reader.createConnection()
connection.connect()

# Example command to write data
# Replace with your specific APDU command for writing data
# This is just a placeholder example
WRITE_APDU = [0xFF, 0xD0, 0x00, 0x00, 0x10]  # APDU command to write
DATA_TO_WRITE = bytearray(b'YourDataHere')  # Data to write (must match APDU length)

# Send the APDU command
response, sw1, sw2 = connection.transmit(WRITE_APDU + list(DATA_TO_WRITE))

# Check response status
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully.")
else:
    print("Error writing data:", hex(sw1), hex(sw2))

# Disconnect from the card
connection.disconnect()
