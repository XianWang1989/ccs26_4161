
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'r+b') as file:  # Open the file in read/write binary mode
        # Seek to the given position
        file.seek(position)  

        # Write the new bytes at that position
        file.write(new_bytes)

# Specify the file path
file_path = 'example_file.txt'

# The position in the file where the new bytes should start being written
position = 4  # This is the byte offset

# The bytes to be written (make sure they are of the same length as what you're replacing)
new_bytes = b'01234'  # Ensure this matches the number of bytes you're replacing

# Call the function to perform the replacement
replace_bytes_in_file(file_path, position, new_bytes)

# Debugging: read back the modified content to verify
with open(file_path, 'rb') as f:
    content = f.read()
    print(content.decode('utf-8'))  # Display content after the replacement
