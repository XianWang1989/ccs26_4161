
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to the smart card
def write_to_card(data):
    # Get the list of available readers
    available_readers = readers()
    if len(available_readers) == 0:
        print("No smart card readers found.")
        return

    # Using the first available reader
    reader = available_readers[0]
    connection = reader.createConnection()
    connection.connect()

    # Prepare the APDU command to write data
    # Assuming your smart card uses a simple WRITE command
    # You might need to adjust based on your card's specifications
    apdu_command = [0xFF, 0xD6, 0x00, 0x00, len(data)]
    command = apdu_command + list(data)

    # Send the command to the card
    response, sw1, sw2 = connection.transmit(command)

    # Verify the response
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully!")
    else:
        print(f"Error writing data: SW1={sw1}, SW2={sw2}")

if __name__ == "__main__":
    private_key_data = b'your_private_key_here'  # Replace with your actual private key
    write_to_card(private_key_data)
