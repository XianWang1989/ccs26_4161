
import sys
import PCSC

def write_private_key_to_card(private_key):
    try:
        # Connect to the card reader
        context = PCSC.PCSC()
        readers = context.list_readers()

        if not readers:
            print("No card reader found!")
            return

        # Pick the first reader
        reader = readers[0]
        connection = context.connect(reader)

        # Ensure the card is present
        if not connection.is_card_present():
            print("No card present!")
            return

        # Select the appropriate application (if needed)
        select_application_apdu = bytearray([0x00, 0xA4, 0x04, 0x00, 0x00])
        response = connection.transmit(select_application_apdu)

        if response[0] != 0x90:
            print("Failed to select application!")
            return

        # Prepare the APDU command to write the private key
        # Example: Writing to specific memory location
        write_apdu = bytearray([0x00, 0xD0, 0x00, 0x00, len(private_key)]) + private_key
        response = connection.transmit(write_apdu)

        if response[0] == 0x90:
            print("Successfully wrote the private key to the card.")
        else:
            print(f"Error writing to card: {response}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            context.disconnect()

if __name__ == "__main__":
    private_key = bytearray.fromhex("YOUR_PRIVATE_KEY_HEX")
    write_private_key_to_card(private_key)
