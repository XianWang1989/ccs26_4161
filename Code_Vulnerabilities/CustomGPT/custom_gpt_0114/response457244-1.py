
from smartcard.System import readers
from smartcard.util import toBytes

def write_to_smart_card(key_data):
    # Select the first available reader
    reader = readers()[0]
    connection = reader.createConnection()
    connection.connect()

    # Command to select the application on the smart card (example)
    select_app = [0x00, 0xA4, 0x04, 0x00]  # Change according to your card's structure
    connection.transmit(select_app)

    # Command to write the private key (adjust according to your card specification)
    write_command = [0x00, 0xD0, 0x00, 0x00]  # Command to write data
    key_data_bytes = toBytes(key_data)  # Convert string to bytes

    # Write the private key
    response, sw1, sw2 = connection.transmit(write_command + key_data_bytes)

    # Check response status
    if sw1 == 0x90 and sw2 == 0x00:
        print("Key written successfully!")
    else:
        print(f"Failed to write key, SW1: {sw1}, SW2: {sw2}")

# Example private key data to write (use actual key data)
private_key = "YOUR_PRIVATE_KEY_HERE"
write_to_smart_card(private_key)
