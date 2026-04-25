
# Open the file in 'ab+' mode
with open('example.txt', 'ab+') as file:
    # Seek to the position (4, 0) which means byte offset 4
    file.seek(4)

    # Create the bytes to insert
    new_bytes = b'01234'

    # Write the new bytes into the file
    # Read the existing bytes first to account for possible overwriting
    current_content = file.read()

    # Move back the position to overwrite
    file.seek(4)

    # Write new bytes
    file.write(new_bytes)

    # To ensure the file size is correct, fill the gap if needed
    if len(new_bytes) < 5:
        # Create padding if new bytes are shorter
        file.write(b'\x00' * (5 - len(new_bytes)))

    # Optionally, you might want to read back the updated content for verification
    file.seek(0)
    updated_content = file.read()
    print(updated_content.decode('utf-8'))
