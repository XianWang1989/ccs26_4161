
from smartcard.System import readers
from smartcard.util import toHexString, toBytes

# Connect to the smart card reader
r = readers()
reader = r[0]  # Select the first reader
connection = reader.createConnection()
connection.connect()

# APDU command to write data (example command, customize as needed)
# Assuming you have the appropriate command structure for your card
command = [0x00, 0xD0, 0x00, 0x00, 0x0A]  # Example command (write data)
data_to_write = "My data".encode()  # Convert your data to bytes
command.extend(data_to_write)  # Append your data to the command

# Send the command to the card
response, sw1, sw2 = connection.transmit(command)

# Check the response status
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully.")
else:
    print("Error writing data: {} {}".format(hex(sw1), hex(sw2)))
