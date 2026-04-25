
from smartcard.System import readers
from smartcard.util import toHexString

# Connect to the smart card reader
r = readers()
connection = r[0].createConnection()
connection.connect()

# Define APDU command to write data (replace with correct command for your card)
command = [0xFF, 0xD6, 0x00, 0x00, 0x02]  # Example command to write data
data_to_write = [0x12, 0x34]  # Example data (your GPG private key in a format that your card accepts)

# Combine command with data
full_command = command + data_to_write

# Send command to card and receive response
response, sw1, sw2 = connection.transmit(full_command)

print("Response:", toHexString(response))
print("Status words:", sw1, sw2)
