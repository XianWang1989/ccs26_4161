
from smartcard.System import readers
from smartcard.util import toHexString

# Initialize the reader
r = readers()
if not r:
    print("No card readers available")
    exit()

reader = r[0]
connection = reader.createConnection()
connection.connect()

# Replace with your APDU command to select the application on your smart card
select_apdu = [0x00, 0xA4, 0x04, 0x00, 0x0E]  # Example APDU command
response, sw1, sw2 = connection.transmit(select_apdu)

if sw1 == 0x90:
    print("Application selected successfully")
else:
    print("Failed to select application:", toHexString(response))

# Prepare the APDU command to write data (this is an example, modify as needed)
write_apdu = [0x00, 0xD0, 0x00, 0x00, 0x0A]  # WRITE command
data_to_write = bytearray(b'YourData')  # Data to write, must match length in APDU
response, sw1, sw2 = connection.transmit(write_apdu + list(data_to_write))

if sw1 == 0x90:
    print("Data written successfully")
else:
    print("Failed to write data:", toHexString(response))

# Remember to close the connection
connection.disconnect()
