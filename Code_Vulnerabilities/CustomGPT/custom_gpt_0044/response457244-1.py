
from smartcard.System import readers
from smartcard.util import toBytes

def write_to_smart_card(data):
    # Get the list of available readers
    r = readers()
    if not r:
        print("No smart card readers found!")
        return

    # Select the first available reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Command to write data to the smart card
    # This is an example; modify based on your card specifications
    write_command = [0xFF, 0xE2, 0x00, 0x00, len(data)] + data

    # Send command to the card
    response, sw1, sw2 = connection.transmit(write_command)

    # Check for success (SW1 SW2 should be 0x90 0x00 for success)
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully!")
    else:
        print(f"Failed to write data. SW1: {sw1}, SW2: {sw2}")

if __name__ == "__main__":
    # Convert your private key here
    private_key = "your_private_key_here"
    data_to_write = toBytes(private_key)

    # Write to the smart card
    write_to_smart_card(data_to_write)
