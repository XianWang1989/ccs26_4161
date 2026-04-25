
# Define the file path and the string to insert
file_path = 'example.txt'
replace_string = b'01234'  # The new bytes to write

# Position in the file where we want to start replacing: (4, 0)
# Here, we just use the first part, so we'll seek to position 4.
start_position = 4

# Open the file in binary mode for updating
with open(file_path, 'rb+') as file:
    # Seek to the specified position
    file.seek(start_position)

    # Write the new bytes at that position
    file.write(replace_string)

# Verify the changes by reading the content
with open(file_path, 'rb') as file:
    content = file.read()
    print(content)
