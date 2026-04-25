
import sys
from smartcard.System import readers
from smartcard.Exceptions import CardConnectionException

# Define the data to write (e.g., GPG private key)
data_to_write = b'Your private key data in bytes'

def write_to_smart_card(data):
    try:
        # List available readers
        r = readers()
        if not r:
            print("No smart card readers found.")
            return

        # Select the first reader
        reader = r[0]
        print(f"Using reader: {reader}")

        # Connect to the smart card
        connection = reader.createConnection()
        connection.connect()

        # Example APDU command to write data to the card
        # Replace with the actual APDU command that your card expects
        apdu_command = [0xFF, 0xD6, 0x00, 0x00, len(data)] + list(data)

        # Send the APDU command to the smart card
        response, sw1, sw2 = connection.transmit(apdu_command)

        # Check the response
        if sw1 == 0x90 and sw2 == 0x00:
            print("Data written successfully.")
        else:
            print(f"Error writing data: SW1={sw1}, SW2={sw2}")

    except CardConnectionException:
        print("Failed to connect to the card.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.disconnect()

write_to_smart_card(data_to_write)
