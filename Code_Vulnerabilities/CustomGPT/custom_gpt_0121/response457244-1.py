
import pcsclite
import sys

def main():
    try:
        # Start the PC/SC context
        context = pcsclite.Context()

        # List available readers
        readers = context.list_readers()
        if not readers:
            print("No Smart Card readers found.")
            return

        print("Available Readers:")
        for reader in readers:
            print(f"- {reader}")

        # Connect to the first reader
        connection = context.connect(readers[0])
        print(f"Connected to {readers[0]}")

        # Select the applet (assuming the applet is available)
        SELECT_APPLET_CMD = [0x00, 0xA4, 0x04, 0x00, 0x00]  # Example command
        response = connection.transmit(bytearray(SELECT_APPLET_CMD))
        print(f"Applet selection response: {response}")

        # Writing data to the card
        WRITE_DATA_CMD = [0x00, 0xD0, 0x00, 0x00, len(data)] + data  # Adjust command as necessary
        data = [0x01, 0x02, 0x03, 0x04]  # Example data to write
        response = connection.transmit(bytearray(WRITE_DATA_CMD))
        print(f"Write operation response: {response}")

    except pcsclite.PCSCLiteError as e:
        print(f"PC/SC error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'connection' in locals():
            context.disconnect(connection)

if __name__ == "__main__":
    main()
