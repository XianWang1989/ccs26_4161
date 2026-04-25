
from smartcard.System import readers
from smartcard.util import toHexString, toBytes

# Select the reader
r = readers()
if not r:
    print("No card readers found.")
    exit()

# Connect to the first reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Example command to write data to the card
# This command depends on the card's specific protocol
# Here is a placeholder for the APDU command
# (Check your card's documentation for specific writing instructions)
write_command = [0xFF, 0xD6, 0x00, 0x00, 0x04]  # Example command to write
data_to_write = b'Test'  # The data you want to write, as bytes

# Combine command with data
apdu = write_command + list(data_to_write)

try:
    # Send the command to the card
    response, sw1, sw2 = connection.transmit(apdu)
    print(f"Response: {toHexString(response)}")
    print(f"Status words: {sw1} {sw2}")
    if sw1 == 0x90:  # Check if the operation was successful
        print("Data written successfully.")
    else:
        print("Failed to write data.")
except Exception as e:
    print(f"An error occurred: {e}")
