
from smartcard.System import readers
from smartcard.util import toASCII, toBytes

# Connect to the smart card reader
r = readers()
print("Available readers: ", r)
reader = r[0]  # Select the first reader
connection = reader.createConnection()
connection.connect()

# Example data to write (your private key in bytes)
private_key = b"YOUR_PRIVATE_KEY_DATA"

# Define the command to write data to the card
# This command depends on the smart card specification you are using
# Example for writing data to a specific location (APDU command format)
apdu_command = [0xFF, 0xD0, 0x00, 0x00, len(private_key)] + list(private_key)

# Send the command to the card
response, sw1, sw2 = connection.transmit(apdu_command)

# Check the status words returned by the smart card
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully!")
else:
    print("Failed to write data, SW1: {}, SW2: {}".format(sw1, sw2))
