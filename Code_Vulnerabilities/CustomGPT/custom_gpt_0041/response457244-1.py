
from smartcard.System import readers
from smartcard.util import toBytes

# Find available readers
r = readers()
print(f"Available readers: {r}")

# Select the first reader
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Define the data to write (example data)
data = "Your data here"
data_bytes = toBytes(data)

# Example APDU command to write data
# Replace 'xx' with the actual value for your smart card
# This format is just illustrative; refer to your card documentation for specifics
apdu_write = [0xFF, 0xD0, 0x00, 0x00, len(data_bytes)] + list(data_bytes)

# Send the APDU command
try:
    response, sw1, sw2 = connection.transmit(apdu_write)
    print("Response:", response)
    print("SW1:", sw1, "SW2:", sw2)
except Exception as e:
    print(f"Error: {e}")

# Close the connection
connection.disconnect()
