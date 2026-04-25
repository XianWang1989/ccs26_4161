
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to the smart card
def write_data_to_card(data):
    # Get the list of all available readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    # Use the first reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Example: APDU Command to write data (this is an example)
    # Replace with actual APDU command according to your smart card specifications
    write_command = [0xFF, 0xD6, 0x00, 0x00, len(data)] + list(data)
    print("Sending command:", toHexString(write_command))

    try:
        # Send the command to smart card
        response, sw1, sw2 = connection.transmit(write_command)
        print("Response:", toHexString(response))
        print("Status Word SW1:", sw1)
        print("Status Word SW2:", sw2)

        if sw1 == 0x90 and sw2 == 0x00:
            print("Data written successfully.")
        else:
            print("Error writing data. SW1/SW2 not OK.")

    except Exception as e:
        print("An error occurred:", e)

# Example data to write (convert your private key to byte array if required)
private_key_data = b'\x01\x02\x03\x04\x05\x06\x07\x08'  # Example byte data
write_data_to_card(private_key_data)
