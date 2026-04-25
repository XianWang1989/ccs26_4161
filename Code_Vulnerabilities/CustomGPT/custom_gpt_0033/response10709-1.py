
def replace_bytes_in_file(file_path, position, replacement_string):
    # Convert replacement string to bytes
    replacement_bytes = replacement_string.encode('utf-8')

    # Open the file in binary mode
    with open(file_path, 'r+b') as file:
        # Seek to the specified position
        file.seek(position[0])

        # Read current bytes to replace
        current_bytes = file.read(position[1])

        # Check if replacement length matches
        if len(current_bytes) != len(replacement_bytes):
            raise ValueError("Replacement string must match the length of the bytes to replace.")

        # Go back to the position and write the new bytes
        file.seek(position[0])
        file.write(replacement_bytes)

# Example usage
file_path = 'example_file.txt'  # Path to your file
position = (4, 4)  # (offset, length to replace)
replacement_string = '01234'  # The bytes to write

replace_bytes_in_file(file_path, position, replacement_string)
