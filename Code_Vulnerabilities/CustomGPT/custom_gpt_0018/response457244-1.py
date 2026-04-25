
from smartcard.System import readers
from smartcard.util import toHexString

# Establish the connection
def connect_to_card():
    r = readers()
    if len(r) < 1:
        print("No smart card readers found.")
        return None
    reader = r[0]
    print(f"Using reader: {reader}")
    connection = reader.createConnection()
    connection.connect()
    return connection

# Example to write data to the smart card
def write_to_card(connection, command_apdu):
    try:
        response, sw1, sw2 = connection.transmit(command_apdu)
        print(f"Response: {toHexString(response)} SW1: {sw1:02X} SW2: {sw2:02X}")
        if sw1 == 0x90:  # Success
            print("Data written successfully!")
        else:
            print("Error writing data.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
if __name__ == "__main__":
    connection = connect_to_card()
    if connection:
        # This APDU command format may vary; adjust according to your smart card's specifications
        # For example, to write data you might use: "00D0", followed by your data in APDU format
        data_to_write = b'\x01\x02\x03\x04'  # Example data
        command_apdu = [0x00, 0xD0, 0x00, 0x00, len(data_to_write)] + list(data_to_write)

        write_to_card(connection, command_apdu)
