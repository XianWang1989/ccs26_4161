
from smartcard.System import readers
from smartcard.util import toHexString, toBytes

# Connect to a smart card reader
def connect_to_reader():
    r = readers()
    if not r:
        raise Exception("No card readers found")
    return r[0].createConnection()

# Write data to the smart card
def write_to_card(data):
    connection = connect_to_reader()
    connection.connect()

    # Example command for writing data to a smart card (modify as needed)
    apdu_command = [0xFF, 0xD6, 0x00, 0x00, len(data)] + list(data)

    try:
        response, sw1, sw2 = connection.transmit(apdu_command)
        if sw1 == 0x90:  # SW1 indicates success
            print("Data written successfully!")
        else:
            print("Failed to write data:", toHexString(response), "Status Word:", sw1, sw2)
    except Exception as e:
        print("Error in communication:", str(e))

# Your private key as bytes (Replace with actual key)
private_key = b'YOUR_PRIVATE_KEY_BYTES'

if __name__ == "__main__":
    write_to_card(private_key)
