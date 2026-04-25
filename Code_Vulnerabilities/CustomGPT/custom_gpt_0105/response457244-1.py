
from smartcard.System import readers
from smartcard.util import toBytes, toHexString

# Define your private key (example)
private_key = "your_private_key_here"

# Select the reader
r = readers()
if not r:
    print("No smart card readers found")
    exit()

reader = r[0]
print(f"Using: {reader}")

# Connect to the card
connection = reader.createConnection()
connection.connect()

# Send APDU command to write the private key
# Example APDU structure: [CLA, INS, P1, P2, Lc, data]
apdu = [
    0xFF,  # CLA (ISO command class)
    0xE2,  # INS (Instruction code for 'WRITE' - this code may vary)
    0x00,  # P1 (Parameter 1)
    0x00,  # P2 (Parameter 2)
    len(private_key)  # Lc (Length of the data)
] + list(toBytes(private_key))

# Send command to the card
response, sw1, sw2 = connection.transmit(apdu)

# Check response status
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully to the card")
else:
    print(f"Error writing data: {toHexString(response)}")
