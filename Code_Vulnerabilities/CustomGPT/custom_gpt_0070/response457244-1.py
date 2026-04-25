
from smartcard.System import readers
from smartcard.util import toBytes

# Select the reader
r = readers()
if not r:
    print("No smart card reader found.")
    exit()
reader = r[0]
print(f"Using reader: {reader}")

# Connect to the smart card
connection = reader.createConnection()
connection.connect()

# Define the command to write to the smart card
# (This is a generic example; your specific command will depend on the card specifications)
# APDU command structure: [CLA INS P1 P2 Lc Data Le]
# Example command to write data to card
data = "your_private_key_here"  # Replace with your actual private key
apdu_command = [0xFF, 0xD6, 0x00, 0x00, len(data)] + list(toBytes(data))

# Send the command to the card
# Response should be checked according to your smart card's specifications
response, sw1, sw2 = connection.transmit(apdu_command)

# Check the status word (SW1 SW2)
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully.")
else:
    print(f"Error writing data: SW1={sw1}, SW2={sw2}")

# Disconnect the card
connection.disconnect()

