
from smartcard.System import readers
from smartcard.util import toHexString

# Select the smart card reader
r = readers()
if not r:
    print("No readers found")
    exit()

reader = r[0]
connection = reader.createConnection()
connection.connect()

# APDU command to write data to the card
# This example assumes that the smart card supports writing with a basic command
# Replace with the appropriate command based on your card's specification

# Example: Writing data (your private key) to the card
# APDU format: [CLA INS P1 P2 LEN data]
# Modify these parameters according to your specific requirements
data_to_write = b'YourPrivateKeyHere'  # Replace with your actual private key

# Example APDU command to write data
cla = 0x00  # Class
ins = 0xE2  # Instruction (This varies by card)
p1 = 0x00   # Parameter 1
p2 = 0x00   # Parameter 2
lc = len(data_to_write)  # Length of data to write

apdu = [cla, ins, p1, p2, lc] + list(data_to_write)

# Send command to the card
response, sw1, sw2 = connection.transmit(apdu)

# Check for success (SW1 SW2 should be 0x90, 0x00 for success)
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully!")
else:
    print(f"Error writing data: SW1={sw1:02x}, SW2={sw2:02x}")
