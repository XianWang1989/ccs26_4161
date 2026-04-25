
from smartcard.System import readers
from smartcard.util import toHexString

# Select the first available smart card reader
r = readers()
if not r:
    print("No smart card readers found.")
    exit()

reader = r[0]
print(f"Using reader: {reader}")

connection = reader.createConnection()
connection.connect()

# Replace these with your actual command to write data to the smart card
# Command structure depends on the smart card specifications
# Example: Write to a specific memory location (APDU command)
write_command = [0xFF, 0xD1, 0x00, 0x00, 0x20]  # Replace with actual command
data_to_write = [0x01, 0x02, 0x03, 0x04]  # Example data

# Combine command and data
apdu = write_command + data_to_write

# Send the APDU command to the card
try:
    response, sw1, sw2 = connection.transmit(apdu)
    print(f"Response: {toHexString(response)}")
    print(f"Status words: {sw1}, {sw2}")
except Exception as e:
    print(f"Error: {e}")

connection.disconnect()
