
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'r+b') as f:
        # Seek to the given position
        f.seek(position[0] + position[1])
        # Replace the bytes
        f.write(new_bytes.encode())

# Example usage
file_path = 'example_file.txt'

# Create an example file
with open(file_path, 'wb') as f:
    f.write(b'thisis somethingasperfectlygood.')

# Replace 'issom' at position (4, 0) with '01234'
replace_bytes_in_file(file_path, (4, 0), '01234')

# Read and print the modified file content
with open(file_path, 'rb') as f:
    content = f.read()
    print(content.decode())
