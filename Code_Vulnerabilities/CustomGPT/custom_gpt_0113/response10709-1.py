
# Example code to replace bytes in a file at a given position

# Define the file path
file_path = 'example_file.txt'

# Create an example file for demonstration
with open(file_path, 'wb') as f:
    f.write(b'thisis something asperfectly good.')

# String to replace and its position
replacement_string = '01234'
start_position = 4  # Starting position to replace

# Open the file in 'r+b' mode for reading and writing
with open(file_path, 'r+b') as f:
    # Seek to the specified position
    f.seek(start_position)
    # Write the new bytes, converting to bytes if needed
    f.write(replacement_string.encode())

# Read the file to see the result
with open(file_path, 'rb') as f:
    modified_content = f.read()

# Print the modified content
print(modified_content.decode())
