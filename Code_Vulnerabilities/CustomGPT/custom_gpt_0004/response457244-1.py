
from smartcard.System import readers
from smartcard.util import toHexString

# List the available readers
r = readers()
print("Available Readers:")
for reader in r:
    print(reader)

# Select the first reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Example command to write data (this will vary based on your card)
# Replace with actual command and data specific to your smart card
write_command = [0x00, 0xD0, 0x00, 0x00, 0x04]  # APDU command (modify as needed)
data_to_write = [0xDE, 0xAD, 0xBE, 0xEF]          # Data to write

# Prepare the full command including data
command = write_command + data_to_write

# Send command to the card
response, sw1, sw2 = connection.transmit(command)

# Print response
print("Response:", toHexString(response))
print("Status Words:", sw1, sw2)

# Close connection
connection.disconnect()
