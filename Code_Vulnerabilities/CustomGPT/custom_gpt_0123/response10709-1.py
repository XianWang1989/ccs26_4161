
# Open the file in append and binary mode
with open('yourfile.txt', 'rb+') as file:
    # Seek to the desired position (4 bytes offset)
    file.seek(4)

    # Define the new bytes to write
    new_bytes = b'01234'

    # Write the new bytes at the specified position
    file.write(new_bytes)

    # Optional: To read and print the new content for confirmation
    file.seek(0)  # Go back to the beginning to read
    updated_content = file.read()
    print(updated_content.decode('utf-8'))
