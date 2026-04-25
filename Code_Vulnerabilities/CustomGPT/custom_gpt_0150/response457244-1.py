
from smartcard.System import readers
from smartcard.util import toBytes

# Select the card reader
r = readers()
if not r:
    print("No card reader found.")
    exit()

# Connect to the first available reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Define the command to write data (example: writing data to the card application)
# Replace '0x00' and data with appropriate values for your card
apdu_command = [0x00, 0xDB, 0x00, 0x00, len(data)] + toBytes(data)  
data = "Your data here"

try:
    # Send the command to the card
    response, sw1, sw2 = connection.transmit(apdu_command)

    # Check the status words
    if sw1 == 0x90:
        print("Data written successfully:", response)
    else:
        print(f"Failed to write data. Status: {sw1:02X} {sw2:02X}")

except Exception as e:
    print("Error:", str(e))
