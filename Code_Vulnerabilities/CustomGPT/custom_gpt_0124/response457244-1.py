
from smartcard.System import readers
from smartcard.util import toHexString

# Select the reader
r = readers()
if not r:
    print("No card readers found!")
    exit()

reader = r[0]
print(f"Using reader: {reader}")

# Connect to the card
connection = reader.createConnection()
connection.connect()

# Example APDU command to write data (you need to adjust based on your card's specs)
# Replace 'key_data' with your actual private key in bytes
key_data = b'YourPrivateKeyBytes'
command = [0xFF, 0xD0, 0x00, 0x00, len(key_data)] + list(key_data)
print(f"Sending command: {toHexString(command)}")

# Send the command to the card
response, sw1, sw2 = connection.transmit(command)

# Check the status word returned by the card
if sw1 == 0x90 and sw2 == 0x00:
    print("Key written successfully.")
else:
    print(f"Error writing key: SW1: {sw1}, SW2: {sw2}")

# Disconnect from the card
connection.disconnect()
