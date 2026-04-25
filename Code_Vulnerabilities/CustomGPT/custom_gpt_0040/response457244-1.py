
from smartcard.System import readers
from smartcard.util import toHexString

# Select the reader
r = readers()
print("Available readers: ", r)
if len(r) == 0:
    print("No readers available")
    exit()

reader = r[0]
connection = reader.createConnection()
connection.connect()

# Example APDU command to write data
APDU_WRITE = [0xFF, 0xD6, 0x00, 0x00, 0x20]  # Example: write command (modify as needed)
data_to_write = b'your_data_here'             # Data to write (ensure it's max 20 bytes)

# Ensure you send the correct length
if len(data_to_write) > 20:
    raise ValueError("Data exceeds maximum length (20 bytes)")

# Construct APDU with data
full_apdu = APDU_WRITE + list(data_to_write)

# Send command
response, sw1, sw2 = connection.transmit(full_apdu)

# Check status word for success
if sw1 == 0x90:  # 0x90 indicates success
    print("Data written successfully")
else:
    print(f"Error writing data: SW1={sw1}, SW2={sw2}")

# Clean up
connection.disconnect()
