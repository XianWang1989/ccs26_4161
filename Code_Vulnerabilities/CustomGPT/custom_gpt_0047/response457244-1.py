
from smartcard.System import readers
from smartcard.util import toHexString

# Function to connect to the smart card
def connect_to_card():
    r = readers()
    if len(r) < 1:
        print("No smart card readers found.")
        return None
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()
    print(f"Connected to {reader.getName()}")
    return connection

# Function to write data to the smart card
def write_data(connection, data):
    # APDU command to write data (modify for your card's expected command)
    WRITE_APDU = [0xFF, 0xD0, 0x00, 0x00, len(data)] + list(data)
    print(f"Sending APDU: {toHexString(WRITE_APDU)}")
    response, sw1, sw2 = connection.transmit(WRITE_APDU)

    # Check status words for success
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully")
    else:
        print(f"Error: SW1: {sw1}, SW2: {sw2}")

def main():
    connection = connect_to_card()
    if connection:
        # Example private key data: ensure to convert it to bytes
        private_key_data = bytes.fromhex("1234567890ABCDEF")  # Replace with your actual key in hex
        write_data(connection, private_key_data)

if __name__ == "__main__":
    main()
