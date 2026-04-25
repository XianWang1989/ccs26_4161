
# Example code to replace bytes in a file at a specific position

# Open the file in binary append mode
with open('example_file.txt', 'r+b') as file:
    # Define the string to write and convert it into bytes
    new_bytes = b'01234'

    # Define the position to replace (4, 0) means starting at position 4
    position = 4

    # Seek to the position in the file
    file.seek(position)

    # Write the new bytes
    file.write(new_bytes)

# To verify the change, read the file again
with open('example_file.txt', 'rb') as file:
    content = file.read()
    print(content.decode())
