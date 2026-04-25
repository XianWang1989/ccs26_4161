
from smartcard.System import readers
from smartcard.util import toHexString

# Select the reader
r = readers()
if not r:
    print("No smart card readers found.")
    exit()

# Connect to the reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Example APDU command to write data (customize according to your card's requirements)
APDU_WRITE = [0xFF, 0xD0, 0x00, 0x00, 0x10]  # Modify this for your specific command
data_to_write = bytes.fromhex('DEADBEEFDEADBEEFDEAD')  # Replace with your key data

# Sending data to the smart card
response, sw1, sw2 = connection.transmit(APDU_WRITE + list(data_to_write))

print("Response:", toHexString(response), "SW1:", sw1, "SW2:", sw2)

# Verify the response
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully.")
else:
    print("Error writing data:", hex(sw1), hex(sw2))
