
from smartcard.System import cards
from smartcard.util import toHexString

# Connect to the smart card
try:
    card_reader = cards.listCards()[0]
    connection = card_reader.createConnection()
    connection.connect()
    print("Connected to:", toHexString(connection.getReader()))

except Exception as e:
    print("Error connecting to card:", e)
    exit()

# Define the APDU command for writing data
# Replace [YOUR_DATA] with the actual data you want to write
data_to_write = b'YOUR_DATA_HERE'
apdu_write = [0xFF, 0xD6, 0x00, 0x00, len(data_to_write)] + list(data_to_write)

# Send the APDU command
try:
    response, sw1, sw2 = connection.transmit(apdu_write)
    if sw1 == 0x90:
        print("Data written successfully.")
    else:
        print(f"Error writing data, status word: {sw1:02X} {sw2:02X}")

except Exception as e:
    print("Error sending APDU:", e)

# Disconnect from the card
connection.disconnect()
