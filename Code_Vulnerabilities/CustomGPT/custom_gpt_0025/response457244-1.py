
from smartcard.System import readers
from smartcard.exceptions import CardConnectionException

# Replace this with your data (e.g., private key in bytes)
private_key_data = b'This_is_your_private_key'

def main():
    try:
        # Get the available readers
        r = readers()
        if not r:
            print("No card readers found.")
            return

        # Connect to the first reader
        reader = r[0]
        connection = reader.createConnection()
        connection.connect()

        # Define APDU command for writing data
        # This example uses a generic command; adjust based on your card's specification
        write_apdu = [0xFF, 0xD6, 0x00, 0x00, len(private_key_data)] + list(private_key_data)

        # Send the APDU command to the card
        response, sw1, sw2 = connection.transmit(write_apdu)

        # Check for a successful write
        if sw1 == 0x90 and sw2 == 0x00:
            print("Data written successfully.")
        else:
            print("Failed to write data. SW1: {}, SW2: {}".format(sw1, sw2))

    except CardConnectionException as e:
        print("Error connecting to card: {}".format(e))
    except Exception as e:
        print("An error occurred: {}".format(e))

if __name__ == "__main__":
    main()
