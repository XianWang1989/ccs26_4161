
from smartcard.System import readers
from smartcard.util import toBytes

# Select the reader
r = readers()
if not r:
    print("No smart card readers found.")
    exit()

reader = r[0]
print(f"Using Reader: {reader}")

# Connect to the smart card
connection = reader.createConnection()
connection.connect()

# Command to write data to the smart card (APDU commands may vary by card type)
# Example APDU command to write data (use correct length and parameters)
# Note: Replace <INS>, <P1>, <P2>, <data> with your specific command parameters
apdu_command = [0x00, 0xD0, 0x00, 0x00] + list(toBytes("<data>"))
response, sw1, sw2 = connection.transmit(apdu_command)

if sw1 == 0x90:  # 0x90 is success status for the command
    print("Data written successfully.")
else:
    print(f"Error writing data: SW1={sw1} SW2={sw2}")

# Close the connection
connection.disconnect()
