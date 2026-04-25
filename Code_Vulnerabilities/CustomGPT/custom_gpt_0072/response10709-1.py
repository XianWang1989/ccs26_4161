
# File path
file_path = 'yourfile.bin'

# Content to replace
replacement_string = b'01234'  # bytes to write

# Position to start replacing (4, 0)
position = 4

# Open the file in binary read/write mode
with open(file_path, 'r+b') as file:
    # Move to the desired position
    file.seek(position)
    # Write the replacement bytes
    file.write(replacement_string)

# Confirm the write (optional)
with open(file_path, 'rb') as file:
    content = file.read()
    print(content)  # Display new content for verification
