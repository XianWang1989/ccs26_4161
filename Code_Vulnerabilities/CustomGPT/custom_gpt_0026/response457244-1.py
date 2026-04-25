
from smartcard.System import readers
from smartcard.util import toHexString

# Get the list of available smart card readers
r = readers()
if not r:
    raise Exception("No smart card readers found.")

# Select the first reader
reader = r[0]
print(f"Using reader: {reader}")

# Connect to the smart card
connection = reader.createConnection()
connection.connect()

# Example APDU command to write data
# Note: You need to replace 'XX' with appropriate values for your card
# For example, to write a private key:
apdu_write_private_key = [0xFF, 0xD0, 0x00, 0x00, 0x20]  # Command for writing data
data_to_write = bytearray([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 
                           0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10])  # Replace this with actual key data

# Send the write command
response, sw1, sw2 = connection.transmit(apdu_write_private_key + data_to_write)

# Check the response status word
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully.")
else:
    print(f"Error writing data: {toHexString(response)}")

# Always remember to disconnect when done
connection.disconnect()
