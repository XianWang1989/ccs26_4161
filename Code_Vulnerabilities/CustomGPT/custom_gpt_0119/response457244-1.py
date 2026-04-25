
from smartcard.System import readers
from smartcard.util import toHexString

# Connect to the smart card reader
r = readers()
connection = r[0].createConnection()
connection.connect()

# Define the data to be written (replace with your actual data)
data_to_write = bytearray([0x00, 0xD0, 0x00, 0x00, 0x10])  # Replace with relevant APDU command and data
# Example APDU command to write data (status and values will depend on your card type)

try:
    # Send the command to the smart card
    response, sw1, sw2 = connection.transmit(data_to_write)

    # Check the response
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully!")
    else:
        print(f"Error: {toHexString(response)} - SW1: {sw1} SW2: {sw2}")

except Exception as e:
    print(f"An error occurred: {e}")
