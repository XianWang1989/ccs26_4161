
from smartcard.System import readers
from smartcard.util import toBytes, toHexString

# Select the reader
r = readers()
print("Available readers:", r)
reader = r[0]  # Choose the first reader

# Connect to the card
connection = reader.createConnection()
connection.connect()

# Command to select the application on the card (if needed)
SELECT_COMMAND = [0x00, 0xA4, 0x04, 0x00]  # Example command
response, sw1, sw2 = connection.transmit(SELECT_COMMAND)
print("Select response:", toHexString(response), "SW1:", sw1, "SW2:", sw2)

# Prepare the private key data to be written
private_key_data = toBytes("YOUR_PRIVATE_KEY_DATA_HERE")  # Use the actual key data
WRITE_COMMAND = [0x00, 0xD0, 0x00, 0x00, len(private_key_data)] + list(private_key_data)

# Send the command to write data to the card
response, sw1, sw2 = connection.transmit(WRITE_COMMAND)
print("Write response:", toHexString(response), "SW1:", sw1, "SW2:", sw2)

# Ensure the operation was successful (check SW1 and SW2)
if sw1 == 0x90 and sw2 == 0x00:
    print("Successfully wrote data to the smart card.")
else:
    print("Failed to write data:", sw1, sw2)

# Disconnect
connection.disconnect()
