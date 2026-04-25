
from smartcard.System import readers
from smartcard.util import toBytes

def write_to_smart_card(data):
    # List available readers
    r = readers()

    if not r:
        print("No smart card readers found.")
        return

    reader = r[0]  # Select the first reader
    connection = reader.createConnection()
    connection.connect()

    # Example APDU command to write data (CL, INS, P1, P2, Lc, data)
    # You need to modify this based on your smart card specifications
    # This is a sample WRITE command
    command = [0xFF, 0xD6, 0x00, 0x00, len(data)] + data

    try:
        response, sw1, sw2 = connection.transmit(command)
        print("Response:", response)
        print("SW1:", hex(sw1), "SW2:", hex(sw2))
    except Exception as e:
        print("Error communicating with card:", e)

if __name__ == "__main__":
    # Replace with your private key data
    private_key_hex = "0123456789ABCDEF"
    private_key_bytes = toBytes(private_key_hex)

    write_to_smart_card(private_key_bytes)
