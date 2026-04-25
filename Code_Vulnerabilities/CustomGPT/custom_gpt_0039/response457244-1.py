
from smartcard.System import readers
from smartcard.util import toHexString

# Connect to the smart card reader
r = readers()
if not r:
    print("No smart card readers found.")
    exit()

reader = r[0]  # Choose the first available reader
connection = reader.createConnection()
connection.connect()

# Command to write data (ensure you have the right APDU command for your smart card)
# For example, 0x00 is the CLA, 0xE6 is the instruction to write
# The instruction and data will depend on your specific use case and card
def write_data(data):
    # Convert data to bytes
    data_bytes = data.encode('utf-8')

    # Frame the APDU command (e.g., writing data)
    apdu = [0x00, 0xE6, 0x00, 0x00, len(data_bytes)] + list(data_bytes)

    # Send the APDU
    response, sw1, sw2 = connection.transmit(apdu)

    # Check for success (SW1, SW2 codes)
    if sw1 == 0x90:
        print(f"Data written successfully: {toHexString(response)}")
    else:
        print(f"Error writing data: {sw1}, {sw2}")

# Example data to write (public key or private key)
example_data = "your-data-here"
write_data(example_data)

# Disconnect from card
connection.disconnect()
