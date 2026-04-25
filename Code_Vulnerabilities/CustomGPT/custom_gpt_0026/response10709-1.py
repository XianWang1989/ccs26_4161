
def replace_bytes_in_file(file_path, position, new_bytes):
    # Open the file in read+write binary mode
    with open(file_path, 'r+b') as file:
        # Move the cursor to the specified position
        file.seek(position[0])  # Position the cursor at the 4th byte
        # Read existing bytes
        original_bytes = file.read(position[1])
        print(f'Original bytes: {original_bytes}')

        # Rewind to the starting position again to overwrite
        file.seek(position[0])
        # Write the new bytes
        file.write(new_bytes)

# Usage example
file_path = 'your_file.txt'  # Ensure this file exists
replace_bytes_in_file(file_path, (4, 4), b'01234')
