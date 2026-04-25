
from smartcard.System import readers
from smartcard.util import toHexString

def write_to_smart_card(data):
    # List of available readers
    r = readers()
    if not r:
        print("No Smart Card readers found.")
        return

    # Select the reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Assuming the private key needs to be written to a specific APDU command
    # Modify this command according to your card's specifications
    WRITE_APDU = [0xFF, 0xD6, 0x00, 0x00, len(data)] + list(data)

    # Send the command to write data
    response, sw1, sw2 = connection.transmit(WRITE_APDU)

    # Check the response
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully:", toHexString(response))
    else:
        print("Error writing data. SW1: {}, SW2: {}".format(hex(sw1), hex(sw2)))

# Example usage
private_key = b'\x01\x02\x03\x04'  # Replace with your actual private key as bytes
write_to_smart_card(private_key)
