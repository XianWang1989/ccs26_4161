
def replace_bytes_in_file(file_path, position, replacement):
    with open(file_path, 'r+b') as file:
        # Move to the specified position
        file.seek(position[0])
        # Read the bytes to be replaced
        original_bytes = file.read(position[1])

        # Replace original bytes with new bytes
        file.seek(position[0])
        file.write(replacement.encode('utf-8'))

# Example usage
file_path = 'example.txt'  # Ensure this file contains initial text
position = (4, 4)  # Start at byte 4, replace 4 bytes
replacement = '01234'  # New bytes to write

replace_bytes_in_file(file_path, position, replacement)
