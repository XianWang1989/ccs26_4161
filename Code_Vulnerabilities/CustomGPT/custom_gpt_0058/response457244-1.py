
from smartcard.System import readers
from smartcard.util import toBytes

# List available smart card readers
r = readers()
if not r:
    print("No smart card readers found.")
    exit()

# Connect to the first reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Prepare the data you want to write (e.g., your private key in bytes)
private_key_data = "YOUR_PRIVATE_KEY".encode("utf-8")  # Replace with your actual key data
data_to_write = toBytes(private_key_data)

# Define APDU command to write data (this is a general example)
# You may need to adjust the CLA, INS, P1, P2, and LE depending on your smart card specifics
WRITE_APDU = [0xFF, 0xD6, 0x00, 0x00, len(data_to_write)] + list(data_to_write)

# Send the command to the card
response, sw1, sw2 = connection.transmit(WRITE_APDU)

# Check status word for success
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully to the smart card.")
else:
    print(f"Failed to write data to card. SW1: {sw1}, SW2: {sw2}")
