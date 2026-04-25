
from smartcard.System import readers
from smartcard.util import toBytes

# List available readers
r = readers()
if not r:
    print("No card readers found")
    exit()

# Select the first available reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Define command to write data to the card
# (You need to replace 'your_data' with actual data and modify the APDU command accordingly)
data = 'your_data'
apdu_command = [0xD0, 0x00, 0x00, 0x00, len(data)] + list(toBytes(data))

try:
    # Send the command to the card
    response, sw1, sw2 = connection.transmit(apdu_command)
    print("Response:", response, "SW1:", sw1, "SW2:", sw2)

    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully!")
    else:
        print("Error writing data. SW1, SW2: ", sw1, sw2)
except Exception as e:
    print("An error occurred:", e)
