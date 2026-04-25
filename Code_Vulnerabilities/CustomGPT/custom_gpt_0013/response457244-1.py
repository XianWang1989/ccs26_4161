
from smartcard.System import readers
from smartcard.util import toHexString

# Connect to the smart card
r = readers()
print("Available readers: ", r)
reader = r[0]  # Use the first reader
connection = reader.createConnection()
connection.connect()

# Command to write data to the card
# This example assumes a specific command structure
# You may need to adapt it to your card's specifications

# Example private key (should be in byte format)
private_key = bytes.fromhex('your_private_key_here')

# Command APDU to write data (example, modify as needed)
# INS byte for WRITE may vary based on your card
write_apdu = [0x00, 0xD0, 0x00, 0x00, len(private_key)] + list(private_key)

# Send the APDU command
response, sw1, sw2 = connection.transmit(write_apdu)

# Check the response
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully!")
else:
    print("Error writing data: ", toHexString(response), sw1, sw2)

# Disconnect from the card
connection.disconnect()
