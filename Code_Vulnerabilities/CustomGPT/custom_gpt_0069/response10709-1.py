
# Define the path to your file
file_path = 'your_file.txt'  # Change this to your actual file path

# The new bytes to write
replacement_bytes = b'01234'

# Define the position to replace bytes (4, 0)
start_position = 4
length_to_replace = 5  # Length of 'issom'

with open(file_path, 'r+b') as file:
    # Move to the start position
    file.seek(start_position)

    # Read the current bytes (optional, for verification)
    original_bytes = file.read(length_to_replace)
    print(f'Original bytes: {original_bytes}')

    # Seek back to the start position
    file.seek(start_position)

    # Write the new bytes
    file.write(replacement_bytes)

    # Optionally, you can truncate the file if the new bytes are shorter
    # file.truncate()

# Output the final content for verification
with open(file_path, 'rb') as file:
    final_content = file.read()
    print(f'Final file content: {final_content.decode()}')
