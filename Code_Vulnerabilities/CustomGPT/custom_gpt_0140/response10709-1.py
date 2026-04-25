
# Define the file path
file_path = 'example.txt'

# Open the file in 'r+b' mode to read and write binary
with open(file_path, 'r+b') as file:
    # Seek to the position (4, 0) which means byte offset 4
    file.seek(4)

    # Define the replacement string
    replacement = b'01234'

    # Write the replacement bytes to the file
    file.write(replacement)

# To confirm the changes, read the modified content
with open(file_path, 'rb') as file:
    content = file.read()
    print(content)  # Will output b'this01234ethingasperfectlygood.'
