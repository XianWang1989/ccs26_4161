
from smartcard.System import readers
from smartcard.util import toHexString

# Discover available readers
r = readers()
if not r:
    print("No smart card readers found.")
    exit()

reader = r[0]  # Select the first reader
connection = reader.createConnection()
connection.connect()

# Command to write data (this example assumes a specific structure)
# Use appropriate APDU commands based on your smart card specifications
data_to_write = bytes("YourPrivateKeyData", "utf-8")
apdu_write = [0xFF, 0xD0, 0x00, 0x00, len(data_to_write)] + list(data_to_write)

# Communicate with the card
response, sw1, sw2 = connection.transmit(apdu_write)

print(f"Response: {toHexString(response)}")
print(f"Status Word: SW1: {sw1}, SW2: {sw2}")

# Check status word for success
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully.")
else:
    print("Error writing data.")
