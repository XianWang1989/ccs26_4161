
# Open the file in 'r+b' mode to read and write in binary mode
with open('yourfile.txt', 'r+b') as f:
    # Seek to the starting position (4)
    f.seek(4)

    # Prepare the new string to replace (must be bytes)
    new_string = b'01234'

    # Write the new bytes
    f.write(new_string)
