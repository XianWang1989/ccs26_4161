
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'r+b') as f:
        # Move to the specified position
        f.seek(position[0] + position[1])  # (4, 0) for "issom"

        # Write the new bytes
        f.write(new_bytes.encode('utf-8'))

# Define the file path and bytes to replace
file_path = 'example.txt'
new_string = '01234'

# Replace bytes at (4, 0)
replace_bytes_in_file(file_path, (4, 0), new_string)
