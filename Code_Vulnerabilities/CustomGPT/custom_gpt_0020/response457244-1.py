
import sys
from smartcard.System import readers
from smartcard.util import toHexString

# Function to send APDU command to the smart card
def send_apdu(command):
    # List available smart card readers
    r = readers()
    if not r:
        print("No card reader found.")
        sys.exit()

    # Select the first available reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Send APDU command to the smart card
    response, sw1, sw2 = connection.transmit(command)

    # Check for success (status word is 0x9000)
    if sw1 == 0x90 and sw2 == 0x00:
        print("Command successful.")
        print("Response:", toHexString(response))
    else:
        print(f"Command failed with status: {sw1:02X} {sw2:02X}")

# Example APDU command to write data to the card
# This example assumes a specific structure of the APDU command.
# Modify this according to your smart card's specifications.

# Define the command to write data (e.g., private key)
# The following is a fictional example: 
# 0x00 - CLA (Class)
# 0xE6 - INS (Instruction code to write data)
# 0x00 - P1 (Parameter 1)
# 0x01 - P2 (Parameter 2)
# 0x02 - Lc (Length of data)
# 0xA0 0B 0C 0D - Data to write (your actual private key)
apdu_command = [0x00, 0xE6, 0x00, 0x01, 0x02, 0xA0, 0x0B, 0x0C, 0x0D]

# Send the APDU command
send_apdu(apdu_command)
