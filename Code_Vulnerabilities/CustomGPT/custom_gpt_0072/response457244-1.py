
from smartcard.System import readers
from smartcard.util import toHexString

# Get the list of all smart card readers
r = readers()
if len(r) < 1:
    print("No smart card reader found.")
    exit()

# Connect to the first reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Example command to write data to the smart card
# Adapt the command according to your smart card's specifications
# This is a placeholder command that might not work for your specific card
# You need to find the correct APDU command for your smart card
apdu_command = [0x00, 0xD0, 0x00, 0x00, 0x20]  # Example (write command)
data_to_write = bytes.fromhex('your_hex_encoded_private_key_here')  # Replace with your actual key
apdu_command += list(data_to_write)

# Send the command to the smart card
response, sw1, sw2 = connection.transmit(apdu_command)

# Check response status words
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully!")
else:
    print(f"Failed to write data: {toHexString(response)} (SW: {sw1:02X} {sw2:02X})")
