
from smartcard.System import readers
from smartcard.util import toHexString, toBytes

def write_to_smart_card(key_data):
    # Get the list of available readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    print("Card connected:", connection)

    # Command to select the appropriate application on the smart card
    SELECT_APDU = [0x00, 0xA4, 0x04, 0x00, len(key_data)] + list(key_data)
    response, sw1, sw2 = connection.transmit(SELECT_APDU)

    if (sw1, sw2) != (0x90, 0x00):
        print("Select command failed:", toHexString(response), sw1, sw2)
        return

    # Command to write data to the card - replace "DATA_AREA" with actual data area
    WRITE_APDU = [0x00, 0xD0, 0x00, 0x00, len(key_data)] + list(key_data)
    response, sw1, sw2 = connection.transmit(WRITE_APDU)

    if (sw1, sw2) == (0x90, 0x00):
        print("Data written successfully.")
    else:
        print("Write command failed:", toHexString(response), sw1, sw2)

    connection.disconnect()

# Example usage
private_key = "YOUR_PRIVATE_KEY_DATA_HERE"
write_to_smart_card(toBytes(private_key))
