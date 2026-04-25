
from smartcard.System import readers
from smartcard.util import toHexString

# Initialize PC/SC reader
r = readers()
print("Available readers:", r)

# Select your smart card reader
if not r:
    print("No smart card readers available.")
    exit()

reader = r[0]
connection = reader.createConnection()
connection.connect()

# Example data to be written (use your actual private key data)
data_to_write = bytearray("Your private key data here", 'utf-8')

# APDU command for writing data (replace with actual command as needed)
# This is a placeholder. Consult your smart card documentation for the correct command.
command = [0xFF, 0xD6, 0x00, 0x00, len(data_to_write)] + list(data_to_write)

# Send APDU command to the card
response, sw1, sw2 = connection.transmit(command)

print("Response:", toHexString(response))
print("Status Word:", sw1, sw2)

if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully.")
else:
    print("Failed to write data, status word:", sw1, sw2)
