
# Open the file in 'r+b' mode to allow for reading and writing
with open('yourfile.txt', 'r+b') as f:
    # Set the position where you want to start replacing (4, 0)
    position = 4

    # Move the file cursor to the specified position
    f.seek(position)

    # The string to replace and convert it to bytes
    replacement_string = "01234"
    replacement_bytes = replacement_string.encode('utf-8')

    # Write the new bytes to the file
    f.write(replacement_bytes)

# After this, the content of your file will be modified
