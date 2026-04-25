
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'rb+') as f:
        # Move the cursor to the specified position
        f.seek(position[0] + position[1])
        # Write the new bytes at the current cursor position
        f.write(new_bytes)

# Example usage
file_path = 'example.txt'  # Replace with your file path
position = (4, 0)          # Start position (4, 0)
new_string = '01234'
# Convert string to bytes
new_bytes = new_string.encode('utf-8')

# Perform the byte replacement
replace_bytes_in_file(file_path, position, new_bytes)
