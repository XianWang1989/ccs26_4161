
from smartcard.System import readers
from smartcard.util import toHexString, toBytes

# Choose the reader
rdr = readers()[0]  # selecting the first available reader
connection = rdr.createConnection()
connection.connect()

# Command to write data to the smart card
# Note: This is a hypothetical command. 
# The actual command may depend on the smart card specifications.
# Let's say your private key is a bytes object that you intend to write
private_key = b'YOUR_PRIVATE_KEY_DATA'  # Replace with your actual private key data

# Define the APDU command for writing data
# This takes the form: [CLA, INS, P1, P2, L, data]
# You will have to modify the CLA (Class), INS (Instruction), and P1, P2 parameters according to your card spec
CLA = 0xFF  # Class byte
INS = 0xD6  # Instruction byte
P1 = 0x00   # Parameter 1
P2 = 0x00   # Parameter 2
L = len(private_key)  # Length of the data
data_to_write = private_key

# Build APDU command
apdu = [CLA, INS, P1, P2, L] + list(data_to_write)

# Transmit command to card
response, sw1, sw2 = connection.transmit(apdu)

# Check the status word
if (sw1, sw2) == (0x90, 0x00):  # 0x9000 indicates success
    print("Data written successfully to smart card.")
else:
    print("Failed to write data. Status words: {}, {}".format(hex(sw1), hex(sw2)))

# Disconnect the connection
connection.disconnect()
