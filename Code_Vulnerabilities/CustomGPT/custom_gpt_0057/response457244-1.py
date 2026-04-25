
from smartcard.System import readers
from smartcard.util import toBytes

def write_private_key_to_card(private_key):
    r = readers()
    if not r:
        print("No card readers found.")
        return

    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    key_data = toBytes(private_key)
    apdu = [0x00, 0xE2, 0x00, 0x00, len(key_data)] + list(key_data)  # Example APDU to write
    response, sw1, sw2 = connection.transmit(apdu)

    if sw1 == 0x90 and sw2 == 0x00:
        print("Private key written successfully.")
    else:
        print("Failed to write key, SW1: {}, SW2: {}".format(sw1, sw2))

# Replace with your actual private key.
private_key = "your-private-key-in-hex-or-appropriate-format"
write_private_key_to_card(private_key)
