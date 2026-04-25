
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'r+b') as file:
        file.seek(position[0])  # Move to the start position
        file.write(new_bytes)    # Write the new bytes

# File path
file_path = 'your_file.txt'  # Replace with your actual file path

# Specify the position (4, 0)
position = (4, 0)  # (offset, unused for this case)

# New bytes to write
new_bytes = b'01234'

# Call the function to replace bytes
replace_bytes_in_file(file_path, position, new_bytes)
