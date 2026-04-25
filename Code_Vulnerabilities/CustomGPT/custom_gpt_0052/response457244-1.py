
from smartcard.System import readers
from smartcard.util import toHexString

# Function to connect to the smart card
def connect_to_card():
    # Get the list of available card readers
    r = readers()
    if len(r) < 1:
        print("No card readers found")
        return None

    # Connect to the first available reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    return connection

# Function to write data to the smart card
def write_to_card(connection, data):
    # Command to write data (example)
    # Adjust the command according to your card's specification
    command = [0xFF, 0xD0, 0x00, 0x00, len(data)] + data
    response, sw1, sw2 = connection.transmit(command)

    # Check response status
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully:", toHexString(data))
    else:
        print(f"Failed to write data: SW1={sw1:02X}, SW2={sw2:02X}")

# Example private key to write
private_key = bytes.fromhex("YOUR_PRIVATE_KEY_IN_HEX")

# Main logic
if __name__ == "__main__":
    conn = connect_to_card()
    if conn:
        write_to_card(conn, private_key)
        conn.disconnect()
