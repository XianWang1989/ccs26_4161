
# Open the file in binary read/write mode
with open('yourfile.txt', 'r+b') as file:
    # Seek to the specified position (4, 0) = position 4
    position = 4
    file.seek(position)

    # String to write
    new_string = b'01234'  # Note: It should be in bytes

    # Read the existing content
    existing_bytes = file.read()

    # Check the length of the new string
    existing_length = len(existing_bytes)

    # Ensure the file is large enough
    if position + len(new_string) > existing_length:
        # Extend the file if necessary
        file.write(b'\x00' * (position + len(new_string) - existing_length))

    # Seek back to the desired position and write the new bytes
    file.seek(position)
    file.write(new_string)

# The file will now contain: this01234ethingasperfectlygood.
