
from smartcard.System import readers
from smartcard.util import toHexString

# Connect to the smart card reader
r = readers()
print("Available readers:", r)

if not r:
    print("No smart card readers found.")
    exit()

reader = r[0]
connection = reader.createConnection()
connection.connect()

# Example APDU command to write data to the smart card
# Replace <YOUR_APDU_COMMAND> with the actual command for your smart card
# This is an example command, it must be valid for your particular smart card use case
APDU_COMMAND = [0xFF, 0xD0, 0x00, 0x00, 0x20]  # Replace with your command
data_to_write = bytes.fromhex('<YOUR_DATA_HEX_STRING>')  # Data you want to write

# Combine APDU command with data length and data
apdu = APDU_COMMAND + [len(data_to_write)] + list(data_to_write)

# Send the APDU command to the smart card
try:
    response, sw1, sw2 = connection.transmit(apdu)
    print("Response:", toHexString(response))
    print("SW1:", sw1, "SW2:", sw2)  # Status words
except Exception as e:
    print(f"Error while communicating with the card: {e}")
