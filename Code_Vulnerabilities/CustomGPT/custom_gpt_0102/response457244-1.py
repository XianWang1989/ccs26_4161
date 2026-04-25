
from smartcard.System import readers
from smartcard.util import toBytes

# Find available smart card readers
r = readers()
print("Available readers:", r)

# Select the first reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Example command to write data (APDU command)
# This example assumes the smart card is ready to receive the command.
# Update the APDU command with the correct values for your smart card.
apdu_write = [0xFF, 0xD6, 0x00, 0x00, 0x04]  # change according to your needs
data_to_write = toBytes("Data")  # Convert string to bytes

# Ensure the data length fits
if len(data_to_write) > 4:
    raise ValueError("Data too long, max length is 4 bytes")

# Combine APDU command with data
apdu_command = apdu_write + list(data_to_write)

# Send APDU command
response, sw1, sw2 = connection.transmit(apdu_command)

# Check the status word
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully:", response)
else:
    print("Error writing data, status words:", sw1, sw2)

# Disconnect the reader
connection.disconnect()
