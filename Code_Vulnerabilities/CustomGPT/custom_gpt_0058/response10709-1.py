
# Open the file in 'r+b' mode for reading and writing binary
with open('yourfile.txt', 'r+b') as file:
    # Seek to the position where you want to start replacing (4 bytes from the start)
    position = 4
    file.seek(position)

    # The string to be written
    replace_string = '01234'

    # Write the new bytes to the file, only replacing the exact number of bytes needed
    file.write(replace_string.encode())

# To confirm, you can read the modified file and print the output
with open('yourfile.txt', 'rb') as file:
    content = file.read()
    print(content.decode())
