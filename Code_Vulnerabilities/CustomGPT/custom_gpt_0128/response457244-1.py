
from smartcard.System import readers
from smartcard.util import toBytes, toHexString

# Initialize the reader
r = readers()
if not r:
    print("No smart card readers found.")
    exit()

# Connect to the first available reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Example data to write (private key as bytes)
private_key = "YOUR_PRIVATE_KEY".encode('utf-8')  # Replace this with your actual private key

# Define a command to write data to the smart card
# This example uses a hypothetical APDU command format (check your card's specification)
WRITE_APDU = [0xFF, 0xD0, 0x00, 0x00, len(private_key)]  # Modify as per your card's command structure
command = WRITE_APDU + list(private_key)

# Send the command to the smart card
response, sw1, sw2 = connection.transmit(command)

# Check the response
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully.")
else:
    print(f"Error writing data: {toHexString(response)} (SW1: {sw1}, SW2: {sw2})")

# Disconnect the card
connection.disconnect()
