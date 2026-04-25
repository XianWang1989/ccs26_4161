
from smartcard.System import readers
from smartcard.util import toHexString, toBytes

# Function to write data to the smart card
def write_data_to_smart_card(data):
    # Get the available smart card readers
    reader_list = readers()
    if not reader_list:
        print("No smart card readers found.")
        return

    reader = reader_list[0]  # Use the first reader
    connection = reader.createConnection()
    connection.connect()

    # Example command to write data (this will depend on your card's specifications)
    # Command to select application (replace with actual values)
    select_command = [0x00, 0xA4, 0x04, 0x00, 0x0B]  # Example APDU command
    connection.transmit(select_command)

    # Convert data to bytes and prepare to send
    data_bytes = toBytes(data)

    # Command to write data (replace with actual values)
    write_command = [0xFF, 0xD0, 0x00, 0x00, len(data_bytes)] + list(data_bytes)
    response, sw1, sw2 = connection.transmit(write_command)

    # Check for errors
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully.")
    else:
        print(f"Error writing data: SW1={sw1}, SW2={sw2}")

# Example usage
data_to_write = "Hello Smart Card"
write_data_to_smart_card(data_to_write)
