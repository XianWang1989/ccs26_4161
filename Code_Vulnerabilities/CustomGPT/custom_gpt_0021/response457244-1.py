
from smartcard.System import readers
from smartcard.util import toHexString

# List available readers
r = readers()
print("Available readers:", [str(reader) for reader in r])

# Connect to the reader
if not r:
    print("No card readers found.")
    exit()

reader = r[0]
connection = reader.createConnection()
connection.connect()

# Example APDU command to write data to the card
# This command syntax will vary based on your smart card's specifications
# Here, we use a hypothetical command for writing a private key

# Replace 'YOUR_PRIVATE_KEY_DATA' with the actual data you want to write
private_key_data = bytes.fromhex('YOUR_PRIVATE_KEY_DATA')

# APDU command: [CLA, INS, P1, P2, Lc, data]
apdu_command = [0x00, 0xE6, 0x00, 0x00, len(private_key_data)] + list(private_key_data)

# Send the command to the smart card
response, sw1, sw2 = connection.transmit(apdu_command)

# Check the response
print("Response:", toHexString(response))
print("Status words:", sw1, sw2)

# Clean up
connection.disconnect()
