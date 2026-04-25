
from smartcard.System import readers
from smartcard.util import toHexString, toBytes

# Define your private key and the AID (Application Identifier) you want to use
private_key = "your_private_key_in_hex_format"  # Replace with your actual key
aid = "A0 00 00 00 00 01"  # Example AID, adjust accordingly

# Convert the private key from hex to bytes
data_to_write = toBytes(private_key.replace(" ", ""))

def main():
    # Get the list of readers
    r = readers()
    if not r:
        print("No card readers found.")
        return

    # Choose the first reader
    reader = r[0]
    print(f"Using reader: {reader}")

    # Connect to the card
    connection = reader.createConnection()
    connection.connect()

    # Selecting the Application (optional)
    select_applet_cmd = [0x00, 0xA4, 0x04, 0x00] + list(map(int, aid.split()))
    connection.transmit(select_applet_cmd)

    # Write data to the card (example using APDU command for writing)
    write_cmd = [0x00, 0xD0, 0x00, 0x00, len(data_to_write)] + list(data_to_write)
    response, sw1, sw2 = connection.transmit(write_cmd)

    # Check the status words for success
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully.")
    else:
        print(f"Error writing data: SW1={sw1}, SW2={sw2}")

if __name__ == "__main__":
    main()
