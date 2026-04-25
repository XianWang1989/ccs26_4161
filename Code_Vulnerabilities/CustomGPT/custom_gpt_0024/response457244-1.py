
from smartcard.System import readers
from smartcard.util import toHexString

# Select the card reader
rdr = readers()[0]  # assuming you have at least one reader
connection = rdr.createConnection()
connection.connect()

# Define the APDU command for writing data
# Note: Update the command according to your smart card's documentation
apdu_write = [0xFF, 0xD6, 0x00, 0x00, 0x20]  # example command
data_to_write = bytearray(b'YourPrivateKeyDataHere')  # replace with your key data

# Send command
try:
    response = connection.transmit(apdu_write + data_to_write)
    print("Response: ", toHexString(response))
except Exception as e:
    print("Error: ", str(e))
