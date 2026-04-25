
from smartcard.System import readers
from smartcard.util import toHexString, hexStringToBytes

# Select the first available smart card reader
reader_list = readers()
if not reader_list:
    print("No smart card readers found.")
    exit()

reader = reader_list[0]
connection = reader.createConnection()
connection.connect()

# Define the command APDU for writing data
# This is an example APDU command, adjust it based on your card's specification
# Example: Writing data to an ISO 7816 compliant card
data_to_write = "YOUR_DATA_HERE"  # Replace with your data
data_bytes = hexStringToBytes(data_to_write)

# Construct the APDU: Example: Write command
# INS should be adjusted according to your card's protocol
apdu = [0x00, 0xD0, 0x00, 0x00, len(data_bytes)] + list(data_bytes)

try:
    response, sw1, sw2 = connection.transmit(apdu)
    print("Response: ", toHexString(response))
    print("Status Word: ", sw1, sw2)
except Exception as e:
    print("Error during transmission: ", str(e))
finally:
    connection.disconnect()

