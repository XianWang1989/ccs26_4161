
from smartcard.System import readers
from smartcard.util import toBytes

def write_data_to_smart_card(data):
    # Get the list of readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    reader = r[0]
    print("Using reader:", reader)

    connection = reader.createConnection()
    connection.connect()

    # Example command to write data
    # This depends on your specific smart card's APDU command structure
    command = [0x00, 0xD0, 0x00, 0x00] + list(toBytes(data))  # WRITE command

    # Send the command to the card
    response, sw1, sw2 = connection.transmit(command)

    # Check the status word (SW1 SW2) for success
    if sw1 == 0x90:  # Success
        print("Data written successfully.")
    else:
        print(f"Error writing data: SW1={sw1}, SW2={sw2}")

# Example usage
private_key_data = "YourPrivateKeyHere"
write_data_to_smart_card(private_key_data)
