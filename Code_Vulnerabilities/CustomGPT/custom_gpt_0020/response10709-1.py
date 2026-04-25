
# The file you want to modify
file_path = 'example.txt'

# The string to replace with
replacement_str = '01234'

# Position in the file to start replacing (4, 0 means index 4)
start_position = 4

# Open the file in 'r+b' mode (read/write binary mode)
with open(file_path, 'r+b') as file:
    # Seek to the specified position
    file.seek(start_position)  

    # Read the existing bytes (for example, to ensure you know the length)
    existing_bytes = file.read(len(replacement_str))

    # Move back to the start position to write the new bytes
    file.seek(start_position)

    # Write the replacement bytes. Make sure the new string is the same length as what you're replacing.
    # If the replacement is shorter, you can simply write it.
    # If it's longer, you'd have to handle the existing content appropriately.
    file.write(replacement_str.encode('utf-8'))

# After running this code, the content of example.txt will be modified
