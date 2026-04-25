
# Define the file path and the string to replace
file_path = 'example.txt'
replacement_string = b'01234'  # Use bytes for binary write

# Open the file in read and write binary mode
with open(file_path, 'r+b') as file:
    # Seek to the desired position (4, 0) which is position 4
    position = 4
    file.seek(position)

    # Write the replacement string
    file.write(replacement_string)

# The content of the file will now be modified
