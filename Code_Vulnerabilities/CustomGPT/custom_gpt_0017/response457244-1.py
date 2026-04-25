
from smartcard.System import readers
from smartcard.util import toHexString

# Connect to the smart card reader
r = readers()
if not r:
    raise Exception("No smart card reader found.")

reader = r[0]
connection = reader.createConnection()
connection.connect()

# Example data to write (e.g., your private key)
# Ensure the data length is appropriate for the card
private_key_data = b'YourPrivateKeyData'

# Assuming you have a specific command to write data; this varies by card
# Here, I'm using a placeholder command
# You will need to check your card's documentation for the correct APDU command
command = [0xFF, 0xD6, 0x00, 0x00, len(private_key_data)] + list(private_key_data)

# Send command to the card
response, sw1, sw2 = connection.transmit(command)

# Check the status word
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully:", toHexString(private_key_data))
else:
    print("Failed to write data. SW1:", sw1, "SW2:", sw2)
