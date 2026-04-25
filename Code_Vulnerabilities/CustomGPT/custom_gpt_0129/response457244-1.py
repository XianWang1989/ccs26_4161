
from smartcard.System import readers
from smartcard.util import toBytes
from smartcard.Exceptions import *

def write_private_key_to_card(private_key):
    # Connect to the smart card reader
    r = readers()
    if not r:
        raise Exception("No smart card readers found.")

    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Prepare the command to write data to the card
    # This is a placeholder command; you need to customize the command
    command = [0xFF, 0xD6, 0x00, 0x00, len(private_key)]  # Example command format
    command.extend(private_key)  # Add your private key bytes here

    try:
        # Send the command to the card
        response, sw1, sw2 = connection.transmit(command)

        # Check the response status word
        if sw1 == 0x90 and sw2 == 0x00:
            print("Private key written to card successfully.")
        else:
            print(f"Failed to write to card. SW1: {sw1}, SW2: {sw2}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage: Convert a sample private key into bytes and write it to the card
sample_private_key = "YOUR_PRIVATE_KEY_IN_HEX_FORMAT"
private_key_bytes = bytes.fromhex(sample_private_key)
write_private_key_to_card(private_key_bytes)
