
from smartcard.System import readers
from smartcard.util import toBytes

# Connect to the first available reader
r = readers()
if not r:
    print("No smart card readers found.")
    exit()

reader = r[0]
connection = reader.createConnection()
connection.connect()

# Command to write data to the smart card (example)
# You need to replace the APDU command with one suitable for your card
# Let's assume we are storing a private key in a specific location
private_key = "your_private_key_in_hex"  # Use a hex string format
apdu_command = [0xFF, 0xD6, 0x00, 0x00, len(private_key)//2] + toBytes(private_key)

try:
    response, sw1, sw2 = connection.transmit(apdu_command)
    print("Response: ", response)
    print("SW1 SW2: ", sw1, sw2)

    if (sw1 == 0x90) and (sw2 == 0x00):
        print("Data written successfully.")
    else:
        print("Failed to write data: SW1 SW2 =", sw1, sw2)

except Exception as e:
    print("An error occurred:", e)

# Disconnect from the smart card
connection.disconnect()
