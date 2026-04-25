
from smartcard.System import readers
from smartcard.util import toBytes

def write_data_to_smart_card(data):
    # Get the list of available smart card readers
    r = readers()
    if not r:
        print("No smart card reader found.")
        return

    # Connect to the first available reader
    reader = r[0]
    print("Using reader:", reader)

    connection = reader.createConnection()
    connection.connect()

    # Example command to write data
    # Replace with the actual APDU command to write your data
    # APDU command format: [CLA, INS, P1, P2, Lc, Data, Le]
    command = [0xFF, 0xD0, 0x00, 0x00, len(data)] + list(data)

    try:
        # Send the APDU command to the card
        response, sw1, sw2 = connection.transmit(command)

        # Check the status words (SW)
        if sw1 == 0x90 and sw2 == 0x00:
            print("Data written successfully to the smart card.")
        else:
            print(f"Error writing data: SW1={sw1:02X}, SW2={sw2:02X}")

    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        connection.disconnect()

if __name__ == "__main__":
    # Example data to write (e.g., your private key)
    # This should be in byte format
    private_key = "your_private_key_here"  # Replace with your actual key data
    data_to_write = toBytes(private_key)

    write_data_to_smart_card(data_to_write)
