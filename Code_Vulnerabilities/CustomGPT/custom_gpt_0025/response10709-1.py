
# Define the file path
file_path = 'example_file.txt'

# Open the file in 'r+b' mode to read and write in binary
with open(file_path, 'r+b') as file:
    # Seek to the position (4, 0), so we use 4 for this example
    file.seek(4)

    # Define the new bytes to write
    replacement_bytes = b'01234'

    # Replace 5 bytes at the current position with the new bytes
    file.write(replacement_bytes)
