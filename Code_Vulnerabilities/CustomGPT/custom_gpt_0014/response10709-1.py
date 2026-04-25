
# Define the file path
file_path = 'example.txt'

# String to replace
replacement_string = '01234'

# Open the file in 'r+b' mode for reading and writing
with open(file_path, 'r+b') as f:
    # Seek to the specific position (4, 0) -> byte position 4
    f.seek(4)

    # Write the replacement string as bytes
    f.write(replacement_string.encode('utf-8'))

# Printing the result from the file to verify
with open(file_path, 'rb') as f:
    content = f.read()
    print(content.decode('utf-8'))
