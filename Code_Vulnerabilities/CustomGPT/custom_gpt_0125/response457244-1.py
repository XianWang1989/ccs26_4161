
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to the smart card
def write_to_card(data):
    # Get the available readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    print("Using reader:", r[0])
    connection = r[0].createConnection()
    connection.connect()

    # Here, you'll need the proper APDU command to write to the card
    # This is an example APDU command (you need to adapt this according to your card)
    apdu = [0xFF, 0xD6, 0x00, 0x00, len(data)] + list(data)
    response, sw1, sw2 = connection.transmit(apdu)

    print("Response:", toHexString(response))
    print("Status Words: {} {}".format(hex(sw1), hex(sw2)))

# Replace 'your_private_key' with the actual data you want to write.
your_private_key = bytearray(b'SamplePrivateKey123')
write_to_card(your_private_key)
