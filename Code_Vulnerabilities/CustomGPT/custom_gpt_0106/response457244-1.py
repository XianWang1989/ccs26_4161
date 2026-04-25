
from smartcard.System import readers
from smartcard.util import toHexString

# Select the reader
r = readers()
print("Available readers:", r)

if not r:
    print("No smart card readers found.")
    exit()

reader = r[0]
connection = reader.createConnection()
connection.connect()

# Prepare your data
# Replace this with the format required by your card
private_key_data = bytes.fromhex('YOUR_PRIVATE_KEY_HEX')

# Command APDU to write data (modify this as per your card specs)
# This is typically 'WRITE' or similar command, check your card documentation
# Example: [0xFF, 0xD0, 0x00, 0x00, len(private_key_data)]
apdu_command = [0xFF, 0xD0, 0x00, 0x00, len(private_key_data)] + list(private_key_data)

# Send the command to the card
response, sw1, sw2 = connection.transmit(apdu_command)

if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully:", toHexString(response))
else:
    print("Error writing data. SW1: {}, SW2: {}".format(hex(sw1), hex(sw2)))

# Disconnect the reader
connection.disconnect()
