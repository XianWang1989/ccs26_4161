
from smartcard.System import readers
from smartcard.util import toHexString

# Choose the reader
r = readers()
if not r:
    print("No smart card reader found.")
else:
    reader = r[0]
    print(f"Using reader: {reader}")

# Connect to the smart card
connection = reader.createConnection()
connection.connect()

# Example APDU command to write data (e.g., personal data or public key)
# This APDU command format depends on your specific smart card and the data structure you want to write.
# Replace the example command with the actual data and command suitable for your smart card.

# The following is an example command, change it according to your smart card's specification
apdu_command = [0xFF, 0xD6, 0x00, 0x00, 0x10]  # This is a generic write command
data_to_write = [0x01, 0x02, 0x03, 0x04]  # Example data, replace it with your actual data
apdu_command += data_to_write  # Append data to the command

# Send the command to the card
response, sw1, sw2 = connection.transmit(apdu_command)

# Output the response
print(f"Response: {response}, SW1: {sw1}, SW2: {sw2}")

# Always remember to disconnect
connection.disconnect()
