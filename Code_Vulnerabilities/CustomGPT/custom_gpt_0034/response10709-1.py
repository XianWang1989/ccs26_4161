
def replace_bytes_in_file(file_path, position, new_bytes):
    # Open the file in binary mode for reading and writing
    with open(file_path, 'r+b') as f:
        # Move the cursor to the specified position
        f.seek(position[0])
        # Write the new bytes at the specified position
        f.write(new_bytes.encode())  # Encode the string to bytes

# Example usage
file_path = 'example.bin'  # Change this to your file path
position = (4, 0)          # Position to start replacing (4 bytes in)
new_string = '01234'      # New string to write

replace_bytes_in_file(file_path, position, new_string)

# Verify the result
with open(file_path, 'rb') as f:
    print(f.read())
