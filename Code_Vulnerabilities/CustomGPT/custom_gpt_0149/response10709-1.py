
def replace_bytes_in_file(filename, position, new_bytes):
    with open(filename, 'r+b') as f:
        # Move to the start position
        f.seek(position[0])

        # Write the new bytes
        f.write(new_bytes.encode())

# Example usage
file_path = 'example.txt'

# Replace 'issom' at position (4, 0) with '01234'
replace_bytes_in_file(file_path, (4, 0), '01234')
