
from smartcard.System import readers
from smartcard.util import toHexString

# Function to write data to smart card
def write_data_to_smartcard(data, apdu_cmd):
    # Get the list of readers
    r = readers()
    if not r:
        print("No smart card readers found.")
        return

    reader = r[0]
    print("Using reader:", reader)

    # Connect to the reader
    connection = reader.createConnection()
    connection.connect()

    # Write data to the smart card using the provided APDU command
    response, sw1, sw2 = connection.transmit(apdu_cmd)

    # Print the result
    print("Response: ", toHexString(response))
    print("Status Words: ", sw1, sw2)

# Example of the private key data you want to write to the smart card
private_key_data = b'YOUR_PRIVATE_KEY_DATA'  # Replace with your actual private key data

# Example APDU command to write data (this will vary based on your smart card and the method used)
# Here we are assuming you're writing to a specific memory location.
# This command is just an example, you may need to customize it based on your card specs.
apdu_write = [0xFF, 0xD6, 0x00, 0x00, len(private_key_data)] + list(private_key_data)

# Write data to the smart card
write_data_to_smartcard(private_key_data, apdu_write)
