
# Define the file path
file_path = 'example.txt'

# Open the file in 'r+b' mode (read and write in binary)
with open(file_path, 'r+b') as file:
    # Seek to the desired position (4 bytes in)
    position = 4
    file.seek(position)

    # The string to replace with
    new_string = b'01234'

    # Write the new bytes
    file.write(new_string)

# Verify the result by reading the file
with open(file_path, 'rb') as file:
    content = file.read()
    print(content.decode('utf-8'))
