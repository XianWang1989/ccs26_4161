
def replace_in_file(filename, position, new_bytes):
    with open(filename, 'r+b') as file:
        # Move the file pointer to the specified position
        file.seek(position[0] + position[1])

        # Write the new bytes
        file.write(new_bytes)

# Usage
file_path = 'example.txt'
# Ensure the original content of example.txt is: 'thisissomethingasperfectlygood.'
replace_in_file(file_path, (4, 0), b'01234')

# Verify the change
with open(file_path, 'rb') as file:
    print(file.read().decode())
