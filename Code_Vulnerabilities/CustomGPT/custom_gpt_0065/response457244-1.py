
from smartcard.System import readers
from smartcard.util import toBytes

def write_to_card(data):
    # Get a list of readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    reader = r[0]  # use the first reader
    connection = reader.createConnection()
    connection.connect()

    # Example command to write data
    # You'll need to modify this command based on your card's specifications
    apdu_command = [0xFF, 0xD0, 0x00, 0x00, len(data)] + list(toBytes(data))

    # Send the command to the card
    response, sw1, sw2 = connection.transmit(apdu_command)

    print(f"Response: {response}, Status Words: {sw1:02X} {sw2:02X}")

if __name__ == "__main__":
    data_to_write = "Your Data Here"  # Replace with your data
    write_to_card(data_to_write)
