
# Define the file name
file_name = 'example.txt'
# Define the string to write and its position
string_to_write = b'01234'
position = (4, 0)  # (offset, byte identifier)

# Function to replace bytes at a specific position
def replace_bytes_in_file(file_name, position, new_bytes):
    offset, _ = position
    with open(file_name, 'r+b') as f:  # Open in read and write binary mode
        f.seek(offset)  # Move to the specified position
        f.write(new_bytes)  # Write the new bytes

# Call the function to execute the replacement
replace_bytes_in_file(file_name, position, string_to_write)

# Verify the change
with open(file_name, 'rb') as f:
    content = f.read()
    print(content)  # Output the updated content
