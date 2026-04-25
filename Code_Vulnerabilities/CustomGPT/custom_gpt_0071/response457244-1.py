
from smartcard.System import readers
from smartcard.Exceptions import NoCardException

# Function to write data to the smart card
def write_data_to_card(data):
    try:
        # Get the list of available readers
        r = readers()
        if not r:
            print("No smart card readers found.")
            return

        # Select the first available reader
        reader = r[0]
        print(f"Using reader: {reader}")

        # Connect to the reader
        connection = reader.createConnection()
        connection.connect()

        # APDU command to write the data (example command)
        # This varies depending on the smart card's specifications
        # 0x00 is the CLA, 0xD0 is the INS for data writing, 
        # you need to specify P1, P2, and your data as needed
        apdu = [0x00, 0xD0, 0x00, 0x00] + list(data)
        # Send the APDU command
        response, sw1, sw2 = connection.transmit(apdu)

        # Check response status
        if sw1 == 0x90:
            print("Data written successfully.")
        else:
            print(f"Error: SW1={sw1} SW2={sw2}")

    except NoCardException:
        print("No card present in the reader.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
data_to_write = [0x01, 0x02, 0x03]  # Example data to write
write_data_to_card(data_to_write)
