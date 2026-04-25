
import sys
import smartcard.System
from smartcard.util import toHexString, toBytes

def write_to_card(data):
    readers = smartcard.System.readers()
    if not readers:
        print("No smart card readers found.")
        return

    reader = readers[0]
    print(f"Using reader: {reader}")

    connection = reader.createConnection()
    connection.connect()

    # Example APDU command to write data (modify according to your need)
    # For instance, writing data to a specific file on the card
    command = [0xFF, 0xD6, 0x00, 0x00, len(data)] + list(toBytes(data))

    try:
        response, sw1, sw2 = connection.transmit(command)
        print(f"Response: {toHexString(response)}")
        print(f"Status Word: {sw1:02X} {sw2:02X}")

        if sw1 == 0x90 and sw2 == 0x00:  # Success
            print("Data written successfully.")
        else:
            print("Error writing data to the card.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Replace 'your_data_here' with the actual data you want to write
    data_to_write = "your_data_here"
    write_to_card(data_to_write)
