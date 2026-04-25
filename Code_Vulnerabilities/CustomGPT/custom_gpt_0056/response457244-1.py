
from smartcard.System import readers
from smartcard.util import toHexString

# Connect to the smart card reader
reader = readers()[0]  # Get the first available reader
connection = reader.createConnection()
connection.connect()

print("Connected to:", reader)

# Prepare your data as bytes (e.g., your private key)
data_to_write = b'\xDE\xAD\xBE\xEF'  # Replace with your actual data

# Define the APDU command to write data (example command)
# This needs to be modified based on your smart card's specification
APDU_WRITE = [0xFF, 0xD0, 0x00, 0x00, len(data_to_write)] + list(data_to_write)

# Send the command to the card
response, sw1, sw2 = connection.transmit(APDU_WRITE)

print("Response:", toHexString(response))
print("Status Word:", sw1, sw2)

# Check if the operation was successful
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully.")
else:
    print("Error writing data. SW1:", sw1, "SW2:", sw2)
