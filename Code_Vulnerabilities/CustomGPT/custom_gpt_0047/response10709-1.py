
# Define the file name
file_name = 'example.txt'

# Open the file in 'ab+' mode
with open(file_name, 'ab+') as file:
    # Move to the desired position (4, 0)
    position = 4
    file.seek(position)

    # New bytes to write
    new_bytes = b'01234'

    # Read the current content to show before replacement (optional)
    file.seek(0)
    original_content = file.read()
    print("Original content:", original_content)

    # Write the new bytes
    file.write(new_bytes)

# To confirm the change, read the file again
with open(file_name, 'rb') as file:
    updated_content = file.read()
    print("Updated content:", updated_content)
