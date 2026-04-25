
# Open the file in 'r+b' mode to allow reading and writing in binary
with open('file.txt', 'r+b') as file:
    # Seek to the desired position
    position = (4, 0)
    file.seek(position[0])  # Move to byte position 4

    # The string to replace with
    replacement_string = b'01234'

    # Write the bytes into the file at the specified position
    file.write(replacement_string)

# Note: Make sure the replacement string length does not exceed the length of the original string slice.
