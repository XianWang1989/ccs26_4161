
# Open the file in 'r+b' mode to read and write binary data
with open('example.txt', 'r+b') as f:
    # Specify the position to start replacing bytes
    position = 4  # Starting index for replacement
    new_string = b'01234'  # Bytes to write

    # Seek to the specified position
    f.seek(position)

    # Write the new bytes
    f.write(new_string)

# The contents of 'example.txt' will now be modified
