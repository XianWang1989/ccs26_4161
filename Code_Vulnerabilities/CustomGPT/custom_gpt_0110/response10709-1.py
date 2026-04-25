
# Define the file path
file_path = 'your_file.txt'

# String you want to write
replacement_string = '01234'

# Convert the replacement string to bytes
replacement_bytes = replacement_string.encode('utf-8')

# Open the file in 'r+b' mode (read and write in binary)
with open(file_path, 'r+b') as file:
    # Seek to the desired position (4th byte)
    position = 4
    file.seek(position)

    # Replace the bytes in the file
    file.write(replacement_bytes)

# The content of the file is now modified as desired
