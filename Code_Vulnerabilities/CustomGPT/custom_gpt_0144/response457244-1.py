from smartcard.System import readers
from smartcard.util import toHexString

# Define the APDU command for selecting an application or file on the card
# This is an example; the actual command depends on your card's specification
SELECT = [0x00, 0xA4, 0x04, 0x00, 0x0A, 0xA0, 0x00, 0x00, 0x00, 0x62,
          0x03, 0x01, 0x0C, 0x06, 0x01]

# Define the APDU command for writing data to the card
# This is an example; the actual command depends on your card's specification
WRITE = [0x00, 0xD0, 0x00, 0x00, 0x10] + [0x01, 0x02, 0x03, 0x04,
                                          0x05, 0x06, 0x07, 0x08,
                                          0x09, 0x0A, 0x0B, 0x0C,
                                          0x0D, 0x0E, 0x0F, 0x10]

# Get the list of available readers
reader_list = readers()
print(f"Available readers: {reader_list}")

if not reader_list:
    raise Exception("No smart card readers found.")

# Use the first reader
reader = reader_list[0]
connection = reader.createConnection()
connection.connect()

# Send the SELECT command
data, sw1, sw2 = connection.transmit(SELECT)
print(f"Response: {toHexString(data)}, Status words: {sw1:02X} {sw2:02X}")

if sw1 == 0x90 and sw2 == 0x00:
    # Send the WRITE command
    data, sw1, sw2 = connection.transmit(WRITE)
    print(f"Response: {toHexString(data)}, Status words: {sw1:02X} {sw2:02X}")

    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully.")
    else:
        print("Failed to write data.")
else:
    print("Failed to select application or file.")
