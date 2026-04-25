
from smartcard.System import readers
from smartcard.util import toBytes

# Function to write data to the smart card
def write_to_card(data):
    # Connect to the reader
    r = readers()
    reader = r[0]  # Select the first reader
    connection = reader.createConnection()
    connection.connect()

    # APDU command to write data (this command may vary depending on your smart card)
    # Here, we will use a placeholder command
    # Adjust the command based on your smart card's requirements
    write_command = [0xFF, 0xD0, 0x00, 0x00, len(data)] + list(data)

    # Send the write command
    response, sw1, sw2 = connection.transmit(write_command)

    # Check for success (SW1 is 0x90 for success in most cases)
    if sw1 == 0x90:
        print("Write Successful")
    else:
        print("Write Failed with status words:", sw1, sw2)

# Data you want to write (convert your private key to bytes)
private_key = b'YourPrivateKeyData'
write_to_card(private_key)
