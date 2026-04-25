
from smartcard.System import readers
from smartcard.util import toHexString

# Select the reader
r = readers()
if len(r) < 1:
    print("No smart card readers found")
    exit()

reader = r[0]
print(f"Using reader: {reader}")

connection = reader.createConnection()
connection.connect()

# The command to write data (this is an example command)
# Replace this command with the command specific to your smart card
command = [0xFF, 0xD0, 0x00, 0x00, 0x20]  # Example command (to write to file)
private_key = bytes.fromhex('your_private_key_in_hex_format')  # Convert your private key into bytes format

# Send command to write private key
data = command + list(private_key)
response, sw1, sw2 = connection.transmit(data)

print(f"SW1: {toHexString([sw1])} SW2: {toHexString([sw2])} Response: {toHexString(response)}")

# Check status word for success
if sw1 == 0x90 and sw2 == 0x00:
    print("Private key written successfully.")
else:
    print("Failed to write private key, check status words.")
