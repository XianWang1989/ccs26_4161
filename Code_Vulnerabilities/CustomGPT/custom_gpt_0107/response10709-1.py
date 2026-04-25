
# Define the function to replace bytes at a specified position
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'r+b') as f:  # Open in read/write binary mode
        f.seek(position[0])  # Move to the specified byte position
        f.write(new_bytes)   # Write the new bytes

# Example usage
file_path = 'example.txt'  # Make sure this file exists
position = (4, 0)          # Position to start replacing
new_bytes = b'01234'       # Bytes to write

# Call the function
replace_bytes_in_file(file_path, position, new_bytes)

# To verify the change:
with open(file_path, 'rb') as f:
    content = f.read()
    print(content)
