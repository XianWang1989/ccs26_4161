
from smartcard.System import readers
from smartcard.util import toHexString, toBytes

def write_to_smart_card(data):
    # Find available readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    reader = r[0]  # Use the first available reader
    connection = reader.createConnection()
    connection.connect()

    # The APDU command to write the data to the smart card
    # Example: 0x00 (CLA), 0xD0 (INS), 0x00 (P1), 0x00 (P2), length of data
    apdu_command = [0x00, 0xD0, 0x00, 0x00, len(data)] + list(data)

    # Send the APDU command to the card
    response, sw1, sw2 = connection.transmit(apdu_command)

    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully.")
    else:
        print("Failed to write data. SW1: {}, SW2: {}".format(sw1, sw2))

    # Disconnect from the card
    connection.disconnect()

# Sample data to write (you should replace this with the actual data)
sample_data = b'This is a test.'
write_to_smart_card(sample_data)
