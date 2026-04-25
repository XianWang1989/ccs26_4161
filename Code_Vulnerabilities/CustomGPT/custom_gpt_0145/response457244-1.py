
from smartcard.System import readers
from smartcard.util import toHexString

def write_private_key_to_smart_card(private_key):
    # Select the smart card reader
    r = readers()
    if not r:
        print("No reader available")
        return

    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # You may need to select the GPG application on the card first, if necessary.
    # This command will vary based on your card application, an example command:
    # connection.transmit([0x00, 0xA4, 0x04, 0x00, len(key_data)] + key_data)

    # Example of writing data
    # Here `key_data` should be the byte array of your private key
    key_data = private_key.encode()  # Convert the private key string to bytes
    command = [0xFF, 0xD6, 0x00, 0x00, len(key_data)] + list(key_data)

    # Transmit the command to write the private key
    response, sw1, sw2 = connection.transmit(command)

    if sw1 == 0x90 and sw2 == 0x00:
        print("Private key successfully written to the smart card.")
    else:
        print(f"Failed to write private key. SW1: {sw1}, SW2: {sw2}")

# Usage example
private_key = "your_private_key_here"
write_private_key_to_smart_card(private_key)
