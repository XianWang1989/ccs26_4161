
from smartcard.System import readers
from smartcard.Exceptions import CardConnectionException

# Define your APDU command for writing data (this is an example)
# You need to modify it according to your card's specification
def create_write_apdu(data):
    # APDU command structure: [CLA, INS, P1, P2, dataLength, data...]
    data_length = len(data)
    return [0x00, 0xE6, 0x00, 0x00, data_length] + list(data)

def main():
    try:
        # Get the list of readers
        r = readers()
        if not r:
            print("No smart card readers found.")
            return

        # Choose the first reader
        reader = r[0]
        print(f"Using reader: {reader}")

        # Connect to the card
        connection = reader.createConnection()
        connection.connect()

        # Data to write (example byte data)
        data_to_write = b'YourPrivateKeyData'
        apdu = create_write_apdu(data_to_write)

        # Send the APDU command to the card
        response, sw1, sw2 = connection.transmit(apdu)
        print(f"Response: {response}, Status Word: {sw1:02X} {sw2:02X}")

        if (sw1, sw2) == (0x90, 0x00):
            print("Data written successfully!")
        else:
            print("Failed to write data.")

    except CardConnectionException as e:
        print(f"Card connection error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
