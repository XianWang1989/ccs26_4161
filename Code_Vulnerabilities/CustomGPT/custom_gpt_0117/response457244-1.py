
from smartcard.System import readers
from smartcard.exceptions import CardConnectionException

# Define the data you want to write (for example, a private key)
data_to_write = bytes.fromhex('YOUR_PRIVATE_KEY_HEX')

# Obtain the available smart card readers
r = readers()
print("Available readers:", r)

if not r:
    print("No smart card readers found!")
else:
    try:
        # Connect to the first available reader
        reader = r[0]
        connection = reader.createConnection()
        connection.connect()

        # Define APDU command for writing data; this will vary based on your card's specifications
        # Example APDU command to write data (change as needed)
        write_command = [0x00, 0xD0, 0x00, 0x00, len(data_to_write)] + list(data_to_write)

        # Send the command to the card
        response, sw1, sw2 = connection.transmit(write_command)

        # Check response status
        if sw1 == 0x90:
            print("Data written successfully!")
        else:
            print(f"Failed to write data: SW1={sw1}, SW2={sw2}")

    except CardConnectionException as e:
        print("Could not connect to card:", e)
    finally:
        # Always disconnect the reader
        connection.disconnect()
