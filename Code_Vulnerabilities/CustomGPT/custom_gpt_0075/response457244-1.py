
import smartcard
from smartcard.System import readers

def write_private_key_to_smart_card(private_key_hex):
    # Initialize the reader
    r = readers()
    if not r:
        raise RuntimeError("No smart card readers found.")

    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Command to write data to smart card (this varies based on card specifications)
    # Example: this command may write data to a specific key index
    write_command = [0xFF, 0xD6, 0x00, 0x00, len(private_key_hex) // 2] + [int(private_key_hex[i:i+2], 16) for i in range(0, len(private_key_hex), 2)]

    try:
        response, sw1, sw2 = connection.transmit(write_command)
        if sw1 == 0x90:
            print("Private key written successfully.")
        else:
            print(f"Failed to write: SW1={sw1}, SW2={sw2}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
private_key = "0123456789ABCDEF0123456789ABCDEF"  # Replace with actual key
write_private_key_to_smart_card(private_key)
