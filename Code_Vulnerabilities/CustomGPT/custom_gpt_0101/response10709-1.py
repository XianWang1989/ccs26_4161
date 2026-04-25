
# Open the file in 'r+b' mode to allow for reading and writing
with open('yourfile.txt', 'r+b') as file:
    # Move the cursor to the desired position (4, 0)
    file.seek(4)
    # Write the new bytes at the current position
    file.write(b'01234')
