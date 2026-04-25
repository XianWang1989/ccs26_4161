
# Open the file in 'ab+' mode
with open('your_file.txt', 'ab+') as file:
    # Seek to the desired position
    position = 4
    file.seek(position)

    # Create the bytes you want to write
    replacement_bytes = b'01234'

    # Read the current content for verification
    file.seek(0)  # Go back to the start to read the file
    original_content = file.read()
    print("Original Content:", original_content)

    # Write the replacement bytes at the specified position
    file.seek(position)
    file.write(replacement_bytes)

    # Seek back to the start to verify the new content
    file.seek(0)
    new_content = file.read()
    print("New Content:", new_content)
