
from smartcard.System import readers
from smartcard.util import toHexString

def write_private_key(card, private_key):
    # Example command to select a file on the smart card
    # Adjust the command based on your smart card's specification
    select_cmd = [0x00, 0xA4, 0x04, 0x00]  # SELECT FILE command

    # Send the command to the card
    response, sw1, sw2 = card.transmit(select_cmd)
    if sw1 != 0x90:
        raise Exception(f'Error selecting file: {toHexString(response)}')

    # Prepare the command to write the private key
    write_cmd = [0x00, 0xD0, 0x00, 0x00] + list(private_key)

    # Transmit the write command
    response, sw1, sw2 = card.transmit(write_cmd)
    if sw1 != 0x90:
        raise Exception(f'Error writing key: {toHexString(response)}')

    print('Private key written successfully')

def main():
    # Get the list of available readers
    r = readers()
    if not r:
        print("No card readers found")
        return

    # Connect to the first reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Your private key as bytes (example), adjust this
    private_key = bytearray.fromhex("YOUR_PRIVATE_KEY_IN_HEX")

    write_private_key(connection, private_key)

if __name__ == '__main__':
    main()
