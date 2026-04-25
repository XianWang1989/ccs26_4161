
from smartcard.System import readers
from smartcard.util import toHexString

# Get the available readers
r = readers()
print("Available readers:", r)

# Connect to the first reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Command APDU to select an application
# This APDU command may vary based on the card you are using
select_applet = [0x00, 0xA4, 0x04, 0x00]  # Replace with your select command
response, sw1, sw2 = connection.transmit(select_applet)
if sw1 == 0x90 and sw2 == 0x00:
    print("Applet selected successfully.")
else:
    print("Failed to select applet:", toHexString(response))

# Now, write data to the card
# Replace with the appropriate APDU command for writing your data
data_to_write = [0x00, 0xD0, 0x00, 0x00] + [0x01, 0x02, 0x03, 0x04]  # Example data
response, sw1, sw2 = connection.transmit(data_to_write)

if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully:", toHexString(data_to_write))
else:
    print("Failed to write data:", toHexString(response))

# Disconnect from the reader
connection.disconnect()
