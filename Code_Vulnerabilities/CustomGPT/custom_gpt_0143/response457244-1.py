
from smartcard.System import readers
from smartcard.util import toHexString

# Select the reader
r = readers()
print(f"Available readers: {r}")
if not r:
    raise Exception("No card readers found.")
reader = r[0]

# Connect to the card
connection = reader.createConnection()
connection.connect()

# Example: Write data (e.g., private key) to the card
# This command may vary depending on your card and APDU structure
APDU_WRITE_PRIVATE_KEY = [0xFF, 0xD6, 0x00, 0x00, 0x20]  # APDU for writing data
private_key_data = b'YourPrivateKeyDataHere'  # Replace with your actual data

# Add the private key data length
APDU_WRITE_PRIVATE_KEY.extend(private_key_data)
APDU_WRITE_PRIVATE_KEY.append(len(private_key_data))  # Add length byte

# Send the APDU command
response, sw1, sw2 = connection.transmit(APDU_WRITE_PRIVATE_KEY)

# Check the status word (SW) to verify success
if sw1 == 0x90 and sw2 == 0x00:
    print("Private key written successfully!")
else:
    print(f"Error writing key: SW1={sw1}, SW2={sw2}")

# Disconnect
connection.disconnect()
