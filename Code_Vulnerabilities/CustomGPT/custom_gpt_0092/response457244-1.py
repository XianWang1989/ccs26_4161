
from smartcard.System import readers
from smartcard.util import toBytes

# Get the reader
r = readers()
if not r:
    print("No smart card readers found.")
    exit()

# Connect to the first reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Command to write data (example command)
# Replace with your specific command for your smart card
# Ensure to refer to the smart card's documentation for this command structure
command = [0xFF, 0xD6, 0x00, 0x00, 0x10]  # Example: WRITE_BINARY command
data_to_write = "YourPrivateKeyData".encode('utf-8')  # Your private key data

# Add data to the command
command += list(toBytes(data_to_write))

# Send command
try:
    response, sw1, sw2 = connection.transmit(command)
    print(f"Response: {response}, SW1: {sw1}, SW2: {sw2}")
except Exception as e:
    print(f"Error: {e}")

# Disconnect
connection.disconnect()
