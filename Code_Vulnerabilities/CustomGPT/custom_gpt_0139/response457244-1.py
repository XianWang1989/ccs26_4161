
from smartcard.System import readers
from smartcard.util import toBytes, toHexString

# Function to write data to the smart card
def write_data_to_card(data):
    try:
        # Get the list of available readers
        reader_list = readers()
        if not reader_list:
            print("No smart card readers found.")
            return

        # Connect to the first available reader
        reader = reader_list[0]
        connection = reader.createConnection()
        connection.connect()

        # Here you would normally select the specific application on the card
        # This is often necessary for writing data.
        # APDU command to select application, replace with your application's AID
        # This is often an application identifier (AID) specific to the smart card
        select_command = [0x00, 0xA4, 0x04, 0x00]  # Adjust according to your needs
        connection.transmit(select_command)

        # Prepare the data to be written to the card
        # Example: write a GPG private key data
        write_command = [0x00, 0xD0, 0x00, 0x00, len(data)] + list(data)
        response, sw1, sw2 = connection.transmit(write_command)

        # Check the status word
        print(f"Response: {toHexString(response)}, SW: {sw1:02X} {sw2:02X}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example data: "Hello, Smart Card!"
data = b"Hello, Smart Card!"  # Replace with actual private key data
write_data_to_card(data)
