
from smartcard.System import readers
from smartcard.util import toHexString

# Select the reader
r = readers()
if not r:
    print("No smart card readers found.")
    exit()

reader = r[0]
print(f"Using reader: {reader}")

# Connect to the card
connection = reader.createConnection()
connection.connect()

# Example command to write data (this depends on your card and requirements)
# Here, we will just demonstrate with a hypothetical command
# Replace with actual command based on your card's specification

# Pseudo command to write data
data_to_write = [0x00, 0xD0, 0x00, 0x00] + [0x04, 0x01, 0x02, 0x03, 0x04]  # Example data
response, sw1, sw2 = connection.transmit(data_to_write)

# Check the response
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully:")
    print(toHexString(response))
else:
    print(f"Error writing data: {sw1} {sw2}")
