
import smartcard.System
from smartcard.util import toBytes

# Select the card reader
readers = smartcard.System.readers()
if not readers:
    raise Exception("No card readers found.")

reader = readers[0]
connection = reader.createConnection()
connection.connect()

# Write data to the smart card (example command)
# This command will vary based on your card's specifications
apdu = toBytes("00D0B00100")  # Example APDU command to write data
data_to_write = b"Your private key here"  # Replace with actual key data

# Sending APDU command to write data
response, sw1, sw2 = connection.transmit(apdu + data_to_write)

# Check response
if sw1 == 0x90 and sw2 == 0x00:
    print("Data written successfully.")
else:
    print(f"Error writing data: SW1={sw1:02X} SW2={sw2:02X}")
