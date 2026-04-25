
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'r+b') as file:
        # Seek to the specified position
        file.seek(position[0])

        # Write new bytes
        file.write(new_bytes.encode('utf-8'))

        # To ensure remaining bytes are untouched, truncate if necessary
        # This is optional and typically not needed unless reducing size
        file.truncate()

# Example usage
file_path = 'example.txt'  # Your file path here
position = (4, 0)          # Start at byte 4
new_string = '01234'       # New bytes to write

replace_bytes_in_file(file_path, position, new_string)
