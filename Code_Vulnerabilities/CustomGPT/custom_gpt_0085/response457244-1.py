
from smartcard.System import readers
from smartcard.util import toBytes

# Replace this with your actual card data
private_key_data = "your_private_key_here"

def main():
    # List available readers
    r = readers()
    if not r:
        print("No readers available")
        return

    # Connect to the first available reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # APDU command to write data (example command, modify according to your smart card)
    # This example assumes a Write command; you need to adapt it to your card's spec.
    apdu_command = [0xFF, 0xD6, 0x00, 0x00, len(private_key_data)]  # Write command
    data_to_write = toBytes(private_key_data)

    # Combine the command and data to write the final command
    command = apdu_command + data_to_write

    # Send the command to the card
    response, sw1, sw2 = connection.transmit(command)

    # Check if the write was successful
    if sw1 == 0x90:  # SW1 = 0x90 indicates success
        print("Data written successfully!")
    else:
        print(f"Failed to write data. SW1: {sw1}, SW2: {sw2}")

if __name__ == "__main__":
    main()
