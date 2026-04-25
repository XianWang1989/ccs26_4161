
from smartcard.System import readers
from smartcard.util import toHexString

# Replace this with your data
private_key_data = bytearray([0x01, 0x02, 0x03, 0x04, 0x05])  # Example private key data
applet_select_command = [0x00, 0xA4, 0x04, 0x00]  # Example command to select applet
write_command = [0x00, 0xD0, 0x00, 0x00, len(private_key_data)] + list(private_key_data)  # Example write command

# Get the smart card reader
r = readers()
if not r:
    print("No card readers found")
    exit()

# Connect to the first reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Select the applet
response = connection.transmit(applet_select_command)
print("Select Applet Response:", toHexString(response[0]))

# Write the private key data to the card
response = connection.transmit(write_command)
print("Write Response:", toHexString(response[0]))

# Disconnect from the card
connection.disconnect()
