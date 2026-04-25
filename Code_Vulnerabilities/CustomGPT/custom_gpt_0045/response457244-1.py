
from smartcard.System import readers
from smartcard.util import setT0, setT1

# Function to write data to the smart card
def write_data_to_card(data):
    try:
        # List available readers
        r = readers()
        if not r:
            print("No smart card readers found.")
            return

        # Connect to the first found reader
        reader = r[0]
        connection = reader.createConnection()
        connection.connect()

        # APDU Command to write data (Example: Write to a specific memory location)
        # This is a generic APDU command; you might need to adjust it for your card
        # Here, we use a simple command write to an example address
        # Command format: [Status Command, P1, P2, data length, data]
        # You’ll need to adapt these values accordingly based on your card’s documentation.
        apdu = [0xFF, 0xD6, 0x00, 0x00, len(data)] + data
        response, sw1, sw2 = connection.transmit(apdu)

        # Check the response
        if sw1 == 0x90:
            print("Data written successfully.")
        else:
            print(f"Failed to write data. Status words: {sw1:02X} {sw2:02X}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
data_to_write = [0xDE, 0xAD, 0xBE, 0xEF]  # Example data (as bytes)
write_data_to_card(data_to_write)
