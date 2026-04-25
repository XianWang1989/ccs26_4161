
# Define the file path
file_path = 'example.txt'

# Content to be written
replacement_string = '01234'
# Converting the string to bytes
replacement_bytes = replacement_string.encode()

# Specify the position to start replacing (0-based index)
start_position = 4  # The 'i' in "thisissomething"
# Optionally, you can define how many bytes to replace
num_bytes_to_replace = len(replacement_bytes)

# Open the file in 'ab+' mode
with open(file_path, 'r+b') as file:
    # Move to the start position in the file
    file.seek(start_position)

    # Read the current content
    original_bytes = file.read(num_bytes_to_replace)

    # Replace existing bytes with the new bytes
    file.seek(start_position)  # Go back to the start position to write
    file.write(replacement_bytes)

# Verify the changes by reading the file content again
with open(file_path, 'rb') as file:
    content = file.read()
    print(content.decode())  # Print the new content of the file
