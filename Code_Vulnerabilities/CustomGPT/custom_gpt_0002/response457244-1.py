
from smartcard.System import readers
from smartcard.util import toBytes

# Select the first available reader
r = readers().get(0)
connection = r.createConnection()
connection.connect()

# Example command to write data to the card
# Command APDU to write data (this is a placeholder, modify according to your card's spec)
data_to_write = "Your data here"
apdu_command = [0xFF, 0xD6, 0x00, 0x00, len(data_to_write)] + list(toBytes(data_to_write))

# Send command to the card
response, sw1, sw2 = connection.transmit(apdu_command)

# Check response status
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully!")
else:
    print("Failed to write data; status word:", sw1, sw2)
