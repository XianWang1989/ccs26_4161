
from smartcard.System import readers
from smartcard.util import toBytes

def write_data_to_smart_card(data):
    # Get the list of readers
    r = readers()

    if not r:
        print("No smart card readers found.")
        return

    # Connect to the first reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Example command to write data (APDU command)
    # Adjust according to your smart card specifications
    # Assuming you want to write data to a specific location on the card
    # Replace '00' and 'b0' with the appropriate values as per the smart card's protocol
    command = [0x00, 0xD0, 0x00, 0x00, len(data)] + list(toBytes(data))

    try:
        # Send the command to the card
        response, sw1, sw2 = connection.transmit(command)

        # Process response
        if sw1 == 0x90:  # SW1/SW2 value for success
            print(f"Data written successfully. Response: {response}")
        else:
            print(f"Failed to write data. SW1: {sw1}, SW2: {sw2}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Data to write to the smart card
data_to_write = "Your data here"  # Replace with your actual data
write_data_to_smart_card(data_to_write)
