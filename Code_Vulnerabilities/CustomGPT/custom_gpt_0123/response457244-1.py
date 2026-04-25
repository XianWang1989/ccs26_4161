
from smartcard.System import readers
from smartcard.util import toBytes

# Define the data to write
data_to_write = "Your digital signature data"
data_bytes = toBytes(data_to_write)

# List available readers
r = readers()
print("Available readers:", r)

# Connect to the first reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Define the APDU command to write data (example command)
# This will vary depending on your smart card specifications
# For illustration, below is a generic command:
# Command format: [CLA, INS, P1, P2, Lc, data, Le]
cla = 0xFF  # Class byte
ins = 0xE2  # Instruction byte for WRITE
p1 = 0x00   # Parameter 1
p2 = 0x00   # Parameter 2
lc = len(data_bytes)
apdu = [cla, ins, p1, p2, lc] + list(data_bytes)

# Send the APDU command to the card
response, sw1, sw2 = connection.transmit(apdu)

# Check the response status
if sw1 == 0x90 and sw2 == 0x00:  # Status word indicating success
    print("Data written successfully:", response)
else:
    print("Failed to write data. Status words:", sw1, sw2)

connection.disconnect()
