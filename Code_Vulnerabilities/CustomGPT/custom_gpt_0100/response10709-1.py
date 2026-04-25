
# Open the file in 'r+b' mode to read and write binary data
with open('yourfile.txt', 'r+b') as file:
    # Seek to the desired position (4, 0) means 4 bytes from the start
    file.seek(4)

    # Create the new string bytes you want to write
    new_bytes = b'01234'

    # Write the new bytes; ensure to replace the exact number of bytes
    file.write(new_bytes)
