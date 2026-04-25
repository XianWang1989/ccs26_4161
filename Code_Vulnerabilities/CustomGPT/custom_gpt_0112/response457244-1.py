
from smartcard.System import readers
from smartcard.util import toBytes

# Connect to the smart card reader
r = readers()
print("Available readers:", r)

if not r:
    print("No readers available.")
    exit()

reader = r[0]  # Select the first reader
connection = reader.createConnection()
connection.connect()

# Data to write (your private key)
private_key = "YOUR_PRIVATE_KEY_HERE"
data_to_write = toBytes(private_key)  # Convert string to bytes

# Example command to write data; modify according to your card's specific command
# This command is just an example; refer to your card documentation for correct APDU commands.
command = [0xFF, 0xE2, 0x00, 0x00, len(data_to_write)] + data_to_write

try:
    # Send command to write data to the card
    response, sw1, sw2 = connection.transmit(command)
    print("Response:", response)
    print("Status words:", sw1, sw2)

    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully.")
    else:
        print("Failed to write data. Status words:", sw1, sw2)

except Exception as e:
    print("An error occurred:", str(e))
