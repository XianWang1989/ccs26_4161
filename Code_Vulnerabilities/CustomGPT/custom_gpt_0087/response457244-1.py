
import smartcard.System

def write_to_smart_card(data):
    # Find the available card readers
    readers = smartcard.System.readers()
    if not readers:
        print("No card readers found.")
        return

    reader = readers[0]  # Choose the first reader
    print(f"Using reader: {reader}")

    # Connect to the reader
    connection = reader.createConnection()
    connection.connect()

    # Example command to write data to the smart card
    # The following APDU command will differ based on your card's specifications
    # Here's a placeholder command: 0x00 (CLA), 0xD0 (INS), 0x00 (P1), 0x00 (P2), len(data), data
    apdu = [0x00, 0xD0, 0x00, 0x00, len(data)] + list(data.encode())

    try:
        response, sw1, sw2 = connection.transmit(apdu)
        print(f"Response: {response}, Status Word: {sw1:02X} {sw2:02X}")

        if sw1 == 0x90 and sw2 == 0x00:  # Check for success status
            print("Data written successfully.")
        else:
            print(f"Error writing data: {sw1:02X} {sw2:02X}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
data_to_write = "YourSensitiveData"
write_to_smart_card(data_to_write)
