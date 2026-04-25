
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to the card
def write_data_to_card(card, data):
    try:
        # Create a command to write data
        command = [0xFF, 0xD0, 0x00, 0x00, len(data)] + data
        response, sw1, sw2 = card.transmit(command)

        if sw1 == 0x90:  # Check for success
            print("Data written successfully!")
            print("Response:", toHexString(response))
        else:
            print(f"Error writing data: SW1={sw1:02X}, SW2={sw2:02X}")

    except Exception as e:
        print("An error occurred:", e)

# Main function
def main():
    # List available smart card readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    reader = r[0]  # Select the first reader
    connection = reader.createConnection()
    connection.connect()  # Connect to the reader

    # Prepare the data to be written (example as bytes)
    private_key_data = bytearray.fromhex("your_private_key_in_hex_here")

    # Write the data to the smart card
    write_data_to_card(connection, private_key_data)

if __name__ == "__main__":
    main()
