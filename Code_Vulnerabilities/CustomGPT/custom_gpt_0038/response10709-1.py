
# Open the file in 'r+b' mode, which allows reading and writing in binary
with open('yourfile.txt', 'r+b') as file:
    # Seek to the desired position (4, 0) which is 4 bytes from the start
    position = 4
    file.seek(position)

    # Define the new bytes to write
    new_bytes = b'01234'

    # Write the new bytes at the specified position
    file.write(new_bytes)

    # Optionally, read the modified content
    file.seek(0)  # Move back to the start to read
    modified_content = file.read()
    print(modified_content.decode('utf-8'))
