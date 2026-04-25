
# Opening the file in 'ab+' mode
with open('yourfile.txt', 'ab+') as f:
    # Seek to position (4, 0) which means byte offset 4
    position = 4
    f.seek(position)

    # Create the byte sequence to write
    new_bytes = b'01234'

    # Read remaining bytes after the position where we write
    remaining_bytes = f.read()

    # Move back to the position for overwriting
    f.seek(position)

    # Write the new bytes
    f.write(new_bytes)

    # Write back the remaining bytes, if any
    f.write(remaining_bytes)

# Now the contents in the file should reflect the changes
