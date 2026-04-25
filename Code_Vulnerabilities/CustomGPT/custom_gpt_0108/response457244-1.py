
from smartcard.System import readers
from smartcard.util import toHexString

# Initialize the smart card reader
r = readers()
print("Available readers:", r)

# Open the first reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Command to write data to a smart card
# Example command: this depends on the card's specifications
# This is just a placeholder command; you need to refer to your card's documentation for the correct one.
write_command = [0xFF, 0xD6, 0x00, 0x00, 0x10]  # Example command (Modify accordingly)

# Data to write (example data)
data_to_write = bytearray(b'Some data to write')

# Ensure the length matches the command's expected length
if len(data_to_write) > 10:
    raise ValueError("Data length exceeds 10 bytes")

# Append data to write command
write_command += data_to_write

# Send the command to the card
response, sw1, sw2 = connection.transmit(write_command)

# Print the response
if sw1 == 0x90:  # Successful write
    print("Data successfully written to the card.")
else:
    print(f"Error: {toHexString(response)} {sw1:02x} {sw2:02x}")

connection.disconnect()
