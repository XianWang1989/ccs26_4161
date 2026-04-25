
from smartcard.System import readers
from smartcard.util import toBytes

# Choose the reader
r = readers()
if not r:
    print("No smart card readers found.")
    exit()

reader = r[0]
connection = reader.createConnection()
connection.connect()

# Command to write data to the smart card
# This is just an example; the command will depend on your card specifications
# '00D4' is a common command to write data, adjust according to your needs
data_to_write = "Your data here"
data_bytes = toBytes(data_to_write)

# Example APDU command to write data (this will vary for your specific card)
apdu = [0x00, 0xD0, 0x00, 0x00, len(data_bytes)] + list(data_bytes)

# Send the command to the card
response, sw1, sw2 = connection.transmit(apdu)

# Check for successful write (SW1 and SW2 codes)
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully.")
else:
    print(f"Failed to write data. SW1: {sw1}, SW2: {sw2}")
