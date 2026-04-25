
# Importing the required library
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to smart card
def write_data_to_smart_card(data):
    # Connect to the card reader
    reader = readers()[0]  # Selecting the first reader
    connection = reader.createConnection()
    connection.connect()

    # APDU command structure to write data (example)
    # 0xFF is the CLA byte, which specifies the command class
    # 0xD0 is the INS byte, which specifies the command for writing
    # 0x00 is P1 and P2, parameters for command execution
    # Data is the info you want to write
    WRITE_COMMAND = [0xFF, 0xD0, 0x00, 0x00] + list(data)

    # Send the command to the smart card
    response, sw1, sw2 = connection.transmit(WRITE_COMMAND)

    # Check the response
    if sw1 == 0x90:
        print("Data written successfully: ", toHexString(response))
    else:
        print("Error writing data, SW1: {}, SW2: {}".format(hex(sw1), hex(sw2)))

# Example usage
private_key = [0x01, 0x02, 0x03, 0x04]  # Replace with the actual bytes of your private key
write_data_to_smart_card(private_key)
