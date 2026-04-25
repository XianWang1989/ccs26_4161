
from smartcard.System import readers
from smartcard.util import toHexString

# Find readers
r = readers()
print("Available readers: ", r)

# Choose the first available reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Define the APDU command for writing data (customize the command as needed)
# This is a generic command; you'll need to adapt it to your smart card's specifications.
# For example, to write data, you might use something like:
# CLA Instruction P1 P2 Lc Data Le
apdu = [0xFF, 0xD0, 0x00, 0x00, 0x10] + [0x01] * 16  # Adjust based on your card requirements

# Send the command
response, sw1, sw2 = connection.transmit(apdu)

# Print the response
print("Response: ", toHexString(response))
print("SW1: {}, SW2: {}".format(hex(sw1), hex(sw2)))

# Disconnect
connection.disconnect()
