
from smartcard.System import readers
from smartcard.util import toHexString

def write_data_to_smart_card(data):
    # Select the reader
    r = readers()
    if len(r) < 1:
        print("No card reader found.")
        return

    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    # Convert data to byte array
    data_bytes = data.encode('utf-8')

    # Example APDU command to write data (this may vary based on your card specifications)
    # Assuming we are using a WRITE command, please adjust as necessary
    apdu_command = [0xFF, 0xD6, 0x00, 0x00, len(data_bytes)] + list(data_bytes)

    try:
        # Send the APDU command to the card
        response, sw1, sw2 = connection.transmit(apdu_command)

        # Check the response status word
        if sw1 == 0x90 and sw2 == 0x00:
            print("Data written successfully! Response:", toHexString(response))
        else:
            print("Error writing data. SW1 SW2:", sw1, sw2)
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        connection.disconnect()

# Example private key (This must be a valid representation for your card)
private_key = "-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY_DATA\n-----END PRIVATE KEY-----"
write_data_to_smart_card(private_key)
