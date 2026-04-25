
# Open the file in binary append mode
with open('your_file.txt', 'rb+') as file:
    # Define the string to write
    string_to_replace = b'01234'

    # Define the start position and length of the substring to replace
    start_position = 4
    length_to_replace = 5  # Length of "issom"

    # Seek to the starting position
    file.seek(start_position)

    # Read the existing bytes if needed (for verification)
    existing_bytes = file.read(length_to_replace)
    print(f'Existing bytes: {existing_bytes}')

    # Move back to the start position to write
    file.seek(start_position)

    # Write the new bytes
    file.write(string_to_replace)

# Output the modified file content to verify the change
with open('your_file.txt', 'rb') as file:
    print(file.read())
