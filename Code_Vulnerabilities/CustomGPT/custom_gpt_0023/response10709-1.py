
def replace_bytes_in_file(file_path, position, new_bytes):
    # Open the file in read + write binary mode
    with open(file_path, 'r+b') as f:
        # Seek to the specified position
        f.seek(position)
        # Write the new bytes
        f.write(new_bytes)

# Example usage
file_path = 'your_file.txt'  # Change this to your file path
position = 4  # Starting position to replace
new_string = '01234'  # New string to write
new_bytes = new_string.encode('utf-8')  # Convert string to bytes

replace_bytes_in_file(file_path, position, new_bytes)
