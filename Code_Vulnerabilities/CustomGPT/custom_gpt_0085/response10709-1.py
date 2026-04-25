
def replace_bytes_in_file(filename, position, new_bytes):
    with open(filename, 'r+b') as file:
        # Move the cursor to the desired position
        file.seek(position)

        # Write the new bytes
        file.write(new_bytes)

# Example usage
file_name = 'example.txt'  # Your file name
replace_position = 4  # Starting position to replace
bytes_to_write = b'01234'  # Bytes to write (must be in bytes)

replace_bytes_in_file(file_name, replace_position, bytes_to_write)

# Optional: To see the effect
with open(file_name, 'rb') as file:
    content = file.read()
    print(content.decode())  # Prints the updated content
