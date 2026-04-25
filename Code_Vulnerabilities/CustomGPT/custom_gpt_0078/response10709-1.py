
# Define the file path and the string to replace
file_path = 'example.txt'
replacement_string = '01234'

# Open the file in 'ab+' mode
with open(file_path, 'ab+') as file:
    # Seek to the position where you want to start replacing
    position = (4, 0)  # (offset, block size)
    byte_position = position[0]

    # Move the file pointer to the specified position
    file.seek(byte_position)

    # Replace the bytes
    # Note: Ensure the file is at least as long as the replacement
    current_length = file.tell()
    if current_length < byte_position + len(replacement_string):
        file.write(b'\x00' * (byte_position + len(replacement_string) - current_length))

    # Write the replacement string as bytes
    file.write(replacement_string.encode())

# Result: Reads back the modified file
with open(file_path, 'rb') as file:
    modified_content = file.read()
    print(modified_content.decode())
