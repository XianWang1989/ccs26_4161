
import sys
import time
from smartcard.System import readers
from smartcard.CardType import InteractiveCardType
from smartcard.Exceptions import CardConnectionException

def write_data_to_smart_card(data):
    # List all available smart card readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    # Select the first reader
    reader = r[0]
    print(f"Using reader: {reader}")

    try:
        # Connect to the smart card
        connection = reader.createConnection()
        connection.connect()

        # Prepare APDU command to write data (example command, modify as needed)
        # Here we're assuming a basic write command, typically it would be more complex
        apdu_command = [0xFF, 0xD0, 0x00, 0x00, len(data)] + list(data)
        print(f"Sending APDU: {apdu_command}")

        # Send the command to the smart card
        response, sw1, sw2 = connection.transmit(apdu_command)

        print(f"Response: {response}, SW1: {sw1}, SW2: {sw2}")

    except CardConnectionException as e:
        print(f"Card connection error: {e}")
    finally:
        # Disconnect the card
        connection.disconnect()

if __name__ == "__main__":
    # Example data to write, adjust as necessary
    data_to_write = bytearray("Your data here", 'utf-8')
    write_data_to_smart_card(data_to_write)
