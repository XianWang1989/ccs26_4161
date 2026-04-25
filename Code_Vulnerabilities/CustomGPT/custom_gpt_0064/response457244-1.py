
from smartcard.System import readers
from smartcard.Exceptions import CardConnectionException

def main():
    # List readers
    r = readers()
    print("Available readers:", r)

    # Connect to the first available reader
    reader = r[0]
    connection = reader.createConnection()

    try:
        connection.connect()
        print("Connected to:", reader)

        # Sample APDU command to write data
        # Replace 'YOUR_PRIVATE_KEY_DATA' with your actual private key data
        private_key_data = bytes.fromhex('YOUR_PRIVATE_KEY_DATA')

        # APDU command to write to a specific memory location
        # This is an example; check your card's specifications for the correct command
        write_command = [0xFF, 0xD6, 0x00, 0x00, len(private_key_data)] + list(private_key_data)

        # Send the APDU command
        response_data, sw1, sw2 = connection.transmit(write_command)

        # Check if write was successful (typically check SW1 and SW2)
        if sw1 == 0x90 and sw2 == 0x00:
            print("Data written successfully!")
        else:
            print("Error writing data:", sw1, sw2)

    except CardConnectionException as e:
        print("Card connection error:", e)
    finally:
        connection.disconnect()

if __name__ == "__main__":
    main()
