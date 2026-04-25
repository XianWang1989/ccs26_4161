
# Open the file in 'ab+' mode
with open('yourfile.txt', 'ab+') as f:
    # Seek to the desired position
    position = 4  # This is the starting byte index
    f.seek(position)  # Move the cursor to the specified position

    # Define the bytes you want to write
    new_bytes = b'01234'  # Should match the length of the bytes being replaced
    old_bytes_length = len(b'issom')  # Length of the bytes to replace

    # Read the content after the replacement segment to preserve it
    content_after = f.read()  # Read the rest of the file

    # Move the cursor back to the position again to write the new bytes
    f.seek(position)

    # Write the new bytes
    f.write(new_bytes)

    # Write back the content that was after the replaced segment
    f.write(content_after)

# The content of your file is now updated
