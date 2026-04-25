
from smartcard.System import readers
from smartcard.util import toBytes

def write_data_to_card(data):
    # Connect to the first available reader
    r = readers()
    if not r:
        raise Exception("No smart card readers found.")

    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Example APDU command to write data (modify according to your card's specifications)
    # This is a generic command and may vary per card type
    WRITE_APDU = [0xFF, 0xD0, 0x00, 0x00, len(data)] + list(data)

    # Send the APDU command to the card
    response, sw1, sw2 = connection.transmit(WRITE_APDU)

    # Check for success (SW1, SW2 codes)
    if sw1 == 0x90 and sw2 == 0x00:
        print("Data written successfully.")
    else:
        print(f"Failed to write data: SW1={sw1}, SW2={sw2}")

# Replace with your actual private key data
private_key = "your_private_key_here"
private_key_bytes = toBytes(private_key.encode('utf-8'))

write_data_to_card(private_key_bytes)
