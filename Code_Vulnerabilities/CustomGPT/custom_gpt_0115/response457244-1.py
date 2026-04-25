
from smartcard.System import readers
from smartcard.util import toHexString, toBytes

def main():
    # List all available readers
    r = readers()
    print("Available readers:")
    for reader in r:
        print(reader)

    # Connect to the first reader
    connection = r[0].createConnection()
    connection.connect()

    # Define your APDU command for writing data (modify as needed)
    # Example: Writing some dummy data (replace with your key data)
    data_to_write = b'\x00\x00\x00\x00'  # Replace with actual data
    command = [0xFF, 0xD6, 0x00, 0x00, len(data_to_write)] + list(data_to_write)

    # Send the command
    response, sw1, sw2 = connection.transmit(command)

    # Check response
    if sw1 == 0x90:  # Success
        print("Data written successfully.")
    else:
        print(f"Failed to write data. SW1: {sw1}, SW2: {sw2}")

if __name__ == "__main__":
    main()
