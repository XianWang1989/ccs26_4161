
from smartcard.System import readers
from smartcard.util import toHexString

# Function to send APDU command to the smart card
def send_apdu(apdu):
    reader = readers()[0]  # Select your reader
    connection = reader.createConnection()
    connection.connect()

    # Send the command
    response, sw1, sw2 = connection.transmit(apdu)
    return response, sw1, sw2

# Example APDU to write data; modify according to your smart card specifications
def write_data_to_card(data):
    # LL indicates length; modify the command according to your card’s documentation
    apdu = [0xFF, 0xD6, 0x00, 0x00, len(data)] + data
    response, sw1, sw2 = send_apdu(apdu)
    print(f"Response: {toHexString(response)}, Status Word: {sw1:02X} {sw2:02X}")

if __name__ == "__main__":
    # Example private key in byte format; it must be provided according to your card's format
    private_key = bytes.fromhex("YOUR_PRIVATE_KEY_HERE")

    write_data_to_card(private_key)
