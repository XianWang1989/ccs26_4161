
from smartcard.System import readers
from smartcard.util import toHexString

def write_data_to_card(data):
    # Get the list of readers
    try:
        r = readers()
        if not r:
            print("No smart card readers found.")
            return

        reader = r[0]
        print("Using reader: ", reader)

        connection = reader.createConnection()
        connection.connect()

        # Prepare APDU command to write data
        # Note: Modify based on your card specifications
        # P1 and P2 may differ depending on your card requirements.
        apdu = [0xD0, 0x00, 0x00, 0x00] + list(data)

        # Send the APDU command
        response, sw1, sw2 = connection.transmit(apdu)

        # Print response status
        print("Response: ", toHexString(response))
        print("SW1: ", sw1, "SW2: ", sw2)

    except Exception as e:
        print("An error occurred: ", str(e))

# Example: Convert your private key to bytes, e.g., like this
private_key_data = b'YourPrivateKeyDataHere'
write_data_to_card(private_key_data)
