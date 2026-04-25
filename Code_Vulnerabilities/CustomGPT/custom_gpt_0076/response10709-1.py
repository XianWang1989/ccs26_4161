
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'r+b') as file:  # Open in read and write binary mode
        file.seek(position[0])  # Seek to the specified position
        file.write(new_bytes)    # Write the new bytes

# Example usage
file_path = 'example.txt'

# Create a sample file
with open(file_path, 'wb') as f:
    f.write(b'thisis somethingasperfectlygood.')

# Replace 'issom' with '01234' starting from position (4, 0)
replace_bytes_in_file(file_path, (4, 0), b'01234')

# Read the file to check the result
with open(file_path, 'rb') as f:
    print(f.read())  # Output: b'this01234ethingasperfectlygood.'
