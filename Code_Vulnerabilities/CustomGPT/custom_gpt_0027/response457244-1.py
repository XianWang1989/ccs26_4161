
from smartcard.System import readers
from smartcard.util import setTlv, getTlv, toHexString

def write_to_card(data):
    try:
        # Initialize reader
        r = readers()
        if not r:
            print("No card reader found.")
            return

        reader = r[0]  # You can select a different reader if needed
        connection = reader.createConnection()
        connection.connect()

        # Example data to write (this should be formatted as per your card's requirements)
        data = bytes(data, 'utf-8')

        # Command to write data (this is hypothetical; consult your card's documentation)
        write_command = [0xFF, 0xD0, 0x00, 0x00, len(data)] + list(data)

        # Send command to card
        response, sw1, sw2 = connection.transmit(write_command)
        print(f"Response: {toHexString(response)}, Status Word: {sw1:02X} {sw2:02X}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'your_private_key_here' with the actual data to be written
    write_to_card('your_private_key_here')
