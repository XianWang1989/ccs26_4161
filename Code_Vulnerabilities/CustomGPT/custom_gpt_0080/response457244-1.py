
from smartcard.System import readers
from smartcard.util import toBytes

# Connect to the smart card reader
def connect_to_card():
    r = readers()
    if not r:
        print("No smart card readers found.")
        return None
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()
    return connection

# Write data to the smart card
def write_to_card(connection, data):
    # Sample APDU command - adjust based on your card's documentation
    # This command structure is for illustrative purposes; check your card's specs.
    write_command = [0xFF, 0xD6, 0x00, 0x00, len(data)] + list(data)

    # Send the command
    response, sw1, sw2 = connection.transmit(write_command)
    if sw1 == 0x90:  # Success
        print("Data written successfully.")
    else:
        print("Error writing data: SW1=0x{:02X}, SW2=0x{:02X}".format(sw1, sw2))

# Main execution
if __name__ == "__main__":
    connection = connect_to_card()
    if connection:
        private_key = "your_private_key_here"  # Replace with your actual key data
        write_to_card(connection, toBytes(private_key))
