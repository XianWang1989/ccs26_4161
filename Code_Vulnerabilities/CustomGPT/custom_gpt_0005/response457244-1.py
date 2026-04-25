
import smartcard
from smartcard.System import readers

# Select the reader
try:
    r = readers()
    reader = r[0]  # Assuming the first reader is the ACR38U-I1
    connection = reader.createConnection()
    connection.connect()

    # Command to write data (Example command)
    # This is a generalized example. Please replace it with your specific data and command structure.
    command = [0xFF, 0xD6, 0x00, 0x00, 0x0A]  # APDU Command to write data
    data_to_write = bytearray("YourDataHere".encode('utf-8'))

    # Send the command to write data
    response, sw1, sw2 = connection.transmit(command + list(data_to_write))

    # Check the response status word
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully!")
    else:
        print(f"Error writing data: SW1={sw1}, SW2={sw2}")

except Exception as e:
    print(f"An error occurred: {e}")
