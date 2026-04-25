
from smartcard.System import readers
from smartcard.util import dump

# Select the reader
r = readers()
print("Available readers:", r)

# Connect to the first reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Define the command to write data (APDU command for writing)
# Here, you should replace the APDU command with the appropriate command for your smart card
# and the data you want to write
APDU_WRITE_DATA = [0xFF, 0xD0, 0x00, 0x00, 0x10]  # Example command
data_to_write = bytes("your_private_key_here", "utf-8")  # Your private key here

# Ensure that the command can accommodate the data length
APDU_WRITE_DATA.extend(data_to_write)

# Send the command to the smart card
response, sw1, sw2 = connection.transmit(APDU_WRITE_DATA)

# Check the response status: SW1 and SW2 byte should be 0x90 0x00 for success
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully!")
else:
    print("Error writing data:", hex(sw1), hex(sw2))

# Close the connection
connection.disconnect()
