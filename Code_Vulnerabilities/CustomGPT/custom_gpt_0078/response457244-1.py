
from smartcard.System import readers
from smartcard.util import toHexString

# Get the list of readers
r = readers()
print("Available readers:", r)

# Select the first reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Command to write data (APDU command format)
# Adjust the command as necessary for your specific smart card
# Example APDU: [Command Class, Instruction Code, Parameter 1, Parameter 2, Length of Data, Data...]
write_command = [0x00, 0xD0, 0x00, 0x00, 0x20]  # D0 is the write command
data_to_write = bytearray(b'your_private_key_here')  # Your private key (must be in bytes)
write_command += list(data_to_write)

# Send the command to the card
response, sw1, sw2 = connection.transmit(write_command)

# Check for success
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully!")
else:
    print("Error writing data: ", toHexString(response), sw1, sw2)
