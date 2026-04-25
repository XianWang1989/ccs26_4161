
from smartcard.System import readers
from smartcard.exceptions import CardConnectionException

def write_data_to_card(data):
    # Get the list of available readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    # Select the first reader
    reader = r[0]
    print(f"Using reader: {reader}")

    try:
        # Connect to the reader
        connection = reader.createConnection()
        connection.connect()

        # Prepare the APDU command to write data (this may vary based on the card)
        apdu_command = [0xFF, 0xD6, 0x00, 0x00, len(data)] + list(data.encode('utf-8'))

        # Send the command to the card
        response, sw1, sw2 = connection.transmit(apdu_command)

        # Check for success (SW1, SW2 should indicate success status)
        if sw1 == 0x90:
            print("Data written successfully!")
        else:
            print(f"Error writing data: SW1={sw1}, SW2={sw2}")

    except CardConnectionException as e:
        print("Card connection failed:", str(e))
    finally:
        connection.disconnect()

# Example data to write
data = "Your private key or relevant data"
write_data_to_card(data)
