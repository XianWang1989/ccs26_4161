
from smartcard.System import readers
from smartcard.util import toHexString

# Initialize the reader
r = readers()
print("Available readers:", r)

# Connect to the first reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Select the appropriate application on the smart card
# (this is usually an APDU command that depends on your card specifications)
SELECT_APDU = [0x00, 0xA4, 0x04, 0x00, len(YOUR_AID), *YOUR_AID]
connection.transmit(SELECT_APDU)

# Prepare your data to write (e.g., your private key)
data_to_write = YOUR_USER_PRIVATE_KEY.encode('utf-8')  # Ensure it's in bytes
WRITE_COMMAND = [0x00, 0xD0, 0x00, 0x00, len(data_to_write)] + list(data_to_write)

# Send the write command
response, sw1, sw2 = connection.transmit(WRITE_COMMAND)

# Check the status word
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully!")
else:
    print("Failed to write data, SW1:", hex(sw1), "SW2:", hex(sw2))

# Disconnect
connection.disconnect()
