
from smartcard.System import readers
from smartcard.util import toBytes, toHexString

def main():
    # List available smart card readers
    r = readers()
    print("Available readers:", r)

    if not r:
        print("No readers found.")
        return

    # Connect to the first reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()
    print(f"Connected to reader: {reader}")

    # Example data to write (replace with your actual data)
    # Note: Ensure that your data is formatted according to the smart card specifications.
    data_to_write = "YOUR_PRIVATE_KEY_OR_DATA"
    data_bytes = toBytes(data_to_write)

    # Define APDU commands
    # This is a simple example; the commands need to correspond to your specific smart card implementation.
    WRITE_COMMAND = [0xFF, 0xD6, 0x00, 0x00, len(data_bytes)] + list(data_bytes)

    # Write data to the smart card
    try:
        response, sw1, sw2 = connection.transmit(WRITE_COMMAND)
        print(f"Response: {toHexString(response)} (SW1: {sw1}; SW2: {sw2})")

        # Check the status word (SW)
        if sw1 == 0x90 and sw2 == 0x00:
            print("Data written successfully!")
        else:
            print("Failed to write data, status:", (sw1, sw2))

    except Exception as e:
        print("Error during write process:", str(e))


if __name__ == "__main__":
    main()
