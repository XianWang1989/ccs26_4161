
from smartcard.System import readers
from smartcard.util import toHexString, toBytes

def connect_to_reader():
    r = readers()
    if not r:
        print("No smart card readers found.")
        return None
    print("Available readers: ", [str(reader) for reader in r])
    reader = r[0]  # Use the first available reader
    connection = reader.createConnection()
    connection.connect()
    return connection

def write_data_to_card(connection, data):
    # Example command to write data (APDU command)
    # This example assumes you're using a basic write command.
    # Modify the command according to your smart card specifications.

    # Note: APDUs vary greatly between types of cards and security requirements.
    # We're using basic ISO7816 command format in the example below.

    # Command format: [CLA INS P1 P2 Lc Data]
    # You may need to change CLA, INS, and parameters as per your smart card
    INS_WRITE = 0xD0  # Example instruction code for write (should be modified accordingly)
    P1 = 0x00         # Parameter 1 (may vary)
    P2 = 0x00         # Parameter 2 (may vary)

    # Convert data to bytes
    byte_data = toBytes(data)
    Lc = len(byte_data)  # Length of data
    command = [0x00, INS_WRITE, P1, P2, Lc] + byte_data  # Complete APDU command

    # Send command to the card
    try:
        data, sw1, sw2 = connection.transmit(command)
        print("Response Data: ", toHexString(data))
        print(f'Status Word: {sw1:X} {sw2:X}')  # Check SW codes for success or failure
    except Exception as e:
        print("Error during writing to card: ", e)

if __name__ == "__main__":
    connection = connect_to_reader()
    if connection:
        # Prepare the data you want to write to the card
        data = "Your data to write"  # Replace with the actual data you need
        write_data_to_card(connection, data.encode())
