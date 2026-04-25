
# Open the file in binary update mode
with open('yourfile.txt', 'r+b') as file:
    # Seek to the specified position (4, 0) as a tuple (offset, whence)
    file.seek(4, 0)

    # Prepare the new bytes to write
    new_bytes = b'01234'

    # Replace the bytes in the file
    file.write(new_bytes)

# Note: Ensure the new bytes are the same length as the bytes being replaced
