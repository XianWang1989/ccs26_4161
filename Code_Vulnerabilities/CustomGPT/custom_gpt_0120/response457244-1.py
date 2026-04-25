
from smartcard.System import readers
from smartcard.util import toBytes

# Function to write data to smart card
def write_to_smart_card(data):
    # Get the list of readers (smart card readers)
    r = readers()
    if not r:
        print("No smart card reader found.")
        return

    # Select the first available reader
    reader = r[0]
    print(f"Using reader: {reader}")

    # Connect to the smart card
    connection = reader.createConnection()
    connection.connect()

    # APDU command to select an application (example)
    select_applet = [0x00, 0xA4, 0x04, 0x00, 0x0E]  # Adjust as per your card's specs
    connection.transmit(select_applet)

    # APDU command to write data (example)
    write_command = [0x00, 0xD0, 0x00, 0x00] + list(toBytes(data))  # Adjust offsets as needed
    response, sw1, sw2 = connection.transmit(write_command)

    # Check response
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully!")
    else:
        print(f"Error writing data: SW1={sw1:02X}, SW2={sw2:02X}")

# Example usage
data_to_write = "Your private key data here"  # Replace with actual key data
write_to_smart_card(data_to_write)
