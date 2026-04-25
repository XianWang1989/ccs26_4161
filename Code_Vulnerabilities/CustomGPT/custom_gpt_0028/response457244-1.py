
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to the smart card
def write_to_card(data):
    # Find the reader
    r = readers()
    if not r:
        print("No card reader found.")
        return

    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # APDU command to write data
    # This is just an example; you might need to adjust it based on your card's specification.
    apdu_write = [0xFF, 0xD6, 0x00, 0x00, len(data)] + list(data.encode('utf-8'))

    # Send the command to the card
    response, sw1, sw2 = connection.transmit(apdu_write)

    if sw1 == 0x90:  # 0x90 indicates success
        print("Data written successfully:", toHexString(response))
    else:
        print("Error writing data:", sw1, sw2)

if __name__ == "__main__":
    # Example data to write
    data_to_write = "Your data here"
    write_to_card(data_to_write)
