
from smartcard.System import readers
from smartcard.util import toHexString

# Select the smart card reader
r = readers()
if not r:
    print("No smart card readers found")
    exit()

reader = r[0]
connection = reader.createConnection()
connection.connect()

# Command to write data to the card (customize for your card's specification)
# Here, we assume you have a method to convert your private key to bytes
private_key = b'YOUR_PRIVATE_KEY_HERE'  # Replace with your actual private key

# APDU command to write data
# For example: 0xFF 0xD6 0x00 0x00 <data length> <data>
# The actual command structure will depend on your smart card specifications

data_length = len(private_key)
command = [0xFF, 0xD6, 0x00, 0x00, data_length] + list(private_key)

try:
    response, sw1, sw2 = connection.transmit(command)
    print("Response:", toHexString(response))
    print(f"SW1: {sw1}, SW2: {sw2}")
except Exception as e:
    print("Error during transmission:", e)

# Disconnect the reader
connection.disconnect()
