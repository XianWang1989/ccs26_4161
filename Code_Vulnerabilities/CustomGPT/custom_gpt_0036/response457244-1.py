
from smartcard.System import readers
from smartcard.util import toBytes

def write_key_to_card(private_key, card_memory_address):
    # Get a list of available smart card readers
    r = readers()
    if len(r) < 1:
        print("No Card Readers found!")
        return

    # Connect to the first available reader
    reader = r[0]
    connection = reader.createConnection()
    connection.connect()

    print(f"Connected to reader: {reader}")

    # Prepare the command to write the private key to the card
    # The command should be adapted based on the smart card's specifications
    command = [
        0xFF,  # Class (Vendor-Specific)
        0xD0,  # Instruction (Write Binary)
        0x00,  # P1: First byte address
        card_memory_address,  # P2: Memory address (specific to your card)
        len(private_key),  # Le: Length of the data to write
    ] + list(private_key)

    # Send the command to the smart card
    response, sw1, sw2 = connection.transmit(toBytes(command))

    if sw1 == 0x90 and sw2 == 0x00:
        print("Private key written successfully!")
    else:
        print(f"Failed to write the private key. Status words: {sw1:02X} {sw2:02X}")

# Example Usage
private_key = b'\x01\x02\x03\x04'  # Replace this with your actual private key in binary format
card_memory_address = 0x00  # Replace this with the actual address for your card

write_key_to_card(private_key, card_memory_address)
