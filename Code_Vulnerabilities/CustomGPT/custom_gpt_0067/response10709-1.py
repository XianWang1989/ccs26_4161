
# Define the file name
file_name = 'example_file.txt'

# Open the file in binary mode for reading and writing
with open(file_name, 'ab+') as file:
    # Move to the desired position (4, 0) - 4 bytes from the start
    file.seek(4)

    # The new string to write
    new_string = b'01234'

    # Read current bytes at the position to verify
    current_bytes = file.read(4)  # Read the existing 4 bytes
    print(f'Original bytes at position 4: {current_bytes}')

    # Move back to the same position to overwrite
    file.seek(4)

    # Write the new bytes
    file.write(new_string)

# Confirm the change by reading the file content
with open(file_name, 'rb') as file:
    content = file.read()
    print(f'Updated file content: {content.decode()}')
