
# Define the function to replace bytes in a file
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'r+b') as file:
        # Move the pointer to the specified position
        file.seek(position)

        # Read the existing bytes after the position to preserve the content
        remaining_bytes = file.read()

        # Move back to the specified position to write the new bytes
        file.seek(position)

        # Write the new bytes
        file.write(new_bytes)

        # Write back the remaining bytes
        file.write(remaining_bytes)

# Example usage
file_path = 'example.txt'  # Path to your file
new_string = b'01234'  # New bytes to write
position = 4  # Starting position for replacement

replace_bytes_in_file(file_path, position, new_string)
