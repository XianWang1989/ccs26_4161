
import pcsclite

# Connect to the PC/SC subsystem
sc = pcsclite.PCSCLite()
sc.connect()

# List available readers
readers = sc.list_readers()
print("Available Readers:", readers)

# Select the smart card reader
reader_name = readers[0]  # Choose the first reader
connection = sc.connect(reader_name)

# Data to write (example: GPG private key)
private_key_data = b'YOUR_PRIVATE_KEY_DATA'

# Command to write data to the card (customize according to your card's specification)
command = [0xFF, 0xD6, 0x00, 0x00, len(private_key_data)] + list(private_key_data)

# Send the command to the card
response = connection.transmit(command)

# Check the response
if response:
    print("Data written successfully!")
else:
    print("Failed to write data.")

# Disconnect from the card
connection.disconnect()
