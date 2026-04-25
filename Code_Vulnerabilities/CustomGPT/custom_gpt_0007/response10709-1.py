
# Open the file in binary mode for reading and writing
with open('example_file.txt', 'r+b') as file:
    # Seek to the desired position (4, 0) which means 4 bytes from the start
    # The second argument of 0 in seek() means the position is absolute from the start of the file
    position = 4
    file.seek(position)

    # Ensure to overwrite the correct number of bytes
    # In this case, we need to overwrite 4 bytes ("issom")
    new_bytes = b'01234'  # The bytes you want to write
    file.write(new_bytes)  # Write the new bytes at the current file position

# The original content 'thisissomethingasperfectlygood.' will now become 'this01234ethingasperfectlygood.'
