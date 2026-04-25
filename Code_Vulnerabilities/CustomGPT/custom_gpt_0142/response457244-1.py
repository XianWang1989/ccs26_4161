
from smartcard.System import readers
from smartcard.util import toHexString, toBytes

# Define the command to write data (customize this according to your card's specification)
# This is just a sample command. You will need to change it based on the card's requirements.
# For example, if you are writing a GPG private key or any other data.
APDU_WRITE_DATA = [0xFF, 0xD0, 0x00, 0x00, 0x10]  # Example: Write command with dummy parameters
data_to_write = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10'  # Sample data

# Add data as payload
APDU_WRITE_DATA += list(data_to_write)

# List available readers
r = readers()
if not r:
    print("No smart card readers found.")
    exit()

# Select the first available reader
reader = r[0]
print(f"Using reader: {reader}")

try:
    # Connect to the card
    connection = reader.createConnection()
    connection.connect()

    # Write data to card
    response, sw1, sw2 = connection.transmit(APDU_WRITE_DATA)

    # Check status word for success
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully.")
    else:
        print(f"Failed to write data. Status Word: {sw1:02X} {sw2:02X}")

except Exception as e:
    print(f"An error occurred: {e}")

