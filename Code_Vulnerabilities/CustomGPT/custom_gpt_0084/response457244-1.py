
from smartcard.System import readers
from smartcard.util import toBytes

def main():
    # List available readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    reader = r[0]
    print(f"Using reader: {reader}")

    connection = reader.createConnection()
    connection.connect()

    # APDU command to write data (example command)
    write_data_apdu = [0xFF, 0xE6, 0x00, 0x00] + list(toBytes('Your Data Here')) + [0x00]

    try:
        # Send the command to the card
        response, sw1, sw2 = connection.transmit(write_data_apdu)

        # Check the response status
        if sw1 == 0x90 and sw2 == 0x00:
            print("Data written successfully.")
        else:
            print(f"Error writing data: SW1={sw1}, SW2={sw2}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
