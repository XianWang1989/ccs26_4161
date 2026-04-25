
from smartcard.System import readers
from smartcard.Util import toBytes

# Select the reader
r = readers()
if len(r) < 1:
    print("No readers found.")
    exit()

reader = r[0]
connection = reader.createConnection()
connection.connect()

# Command to write data to the smart card
# The command depends on the smart card and its commands. Below is a generic example.
# Replace '0x00', '0xE6', '0x00', '0x00' with the corresponding bytes for your card.
data_to_write = "your_private_key_here"  # Replace with your actual key
data_bytes = toBytes(data_to_write)

# Example APDU command to write data: "00 E6 00 00 <data>"
apdu_command = [0x00, 0xE6, 0x00, 0x00] + list(data_bytes)

try:
    response, sw1, sw2 = connection.transmit(apdu_command)
    print(f"Response: {response}, SW1: {sw1}, SW2: {sw2}")
except Exception as e:
    print(f"An error occurred: {e}")

connection.disconnect()
