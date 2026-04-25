
from smartcard.System import readers
from smartcard.util import toBytes

# Initialize the reader
r = readers()
if not r:
    print("No card readers found.")
    exit()

reader = r[0]
connection = reader.createConnection()
connection.connect()

# Example: Writing a private key to the smart card
# This is typically done using APDU commands

# Replace with your actual APDU command for writing the private key
# For demonstration, we use a made-up command
apdu_write_private_key = [0xFF, 0xD0, 0x00, 0x00, 0x20]  # Command for writing
private_key_data = "YOUR_PRIVATE_KEY_DATA_HERE".encode('utf-8')  # Replace with actual key data
data_to_write = toBytes(private_key_data)

# Send the command to the card
try:
    response, sw1, sw2 = connection.transmit(apdu_write_private_key + list(data_to_write))
    print("Response:", response)
    print("SW1:", sw1, "SW2:", sw2)

    # Check if writing was successful
    if sw1 == 0x90 and sw2 == 0x00:
        print("Private key written successfully.")
    else:
        print("Error writing to card: SW1 SW2 =", sw1, sw2)

except Exception as e:
    print("Error:", e)
finally:
    connection.disconnect()
