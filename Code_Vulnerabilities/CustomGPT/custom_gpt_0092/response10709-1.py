
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'r+b') as file:  # Open in read/write binary mode
        file.seek(position)  # Move to the specified byte position
        file.write(new_bytes)  # Write the new bytes

# Example usage
file_path = 'example.txt'  # Make sure this file exists with appropriate content
replace_position = 4  # Replace starting at byte index 4
new_string = '01234'  # String to write

# Convert string to bytes
new_bytes = new_string.encode('utf-8')

replace_bytes_in_file(file_path, replace_position, new_bytes)
