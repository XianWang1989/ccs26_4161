
# Open the file in 'r+b' mode (read and write in binary mode)
with open('yourfile.txt', 'r+b') as file:
    # Move the cursor to position 4
    file.seek(4)  # This is the starting position where you want to replace
    # The new bytes to write
    new_bytes = b'01234'

    # Write the new bytes in the file
    file.write(new_bytes)
