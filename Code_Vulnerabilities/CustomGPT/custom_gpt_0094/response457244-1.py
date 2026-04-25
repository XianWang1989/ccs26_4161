
from smartcard.System import readers
from smartcard.util import toBytes

# Initialize the reader
r = readers()
print(f"Available readers: {r}")
reader = r[0]  # Select the first reader

# Connect to the smart card
connection = reader.createConnection()
connection.connect()

# Define the APDU command for writing to the card
# This example assumes a simple write operation
# Modify the command based on your smart card's specification.
write_command = [0xFF, 0xD0, 0x00, 0x00, 0x20]  # Example command
private_key = "YOUR_PRIVATE_KEY"  # Replace with your private key
data_to_write = toBytes(private_key)  # Convert string to bytes

# Send the write command
response, sw1, sw2 = connection.transmit(write_command + data_to_write)

# Check for successful write
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully.")
else:
    print(f"Failed to write data. Status Word: {sw1:02X} {sw2:02X}")

# Disconnect the connection
connection.disconnect()
