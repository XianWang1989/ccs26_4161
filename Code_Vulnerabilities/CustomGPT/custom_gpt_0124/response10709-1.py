
def replace_bytes_in_file(file_path, position, new_string):
    # Open the file in 'r+b' mode to read and write in binary
    with open(file_path, 'r+b') as file:
        # Seek to the given position
        file.seek(position)

        # Encode the new string to bytes
        new_bytes = new_string.encode('utf-8')

        # Write the new bytes to the file at that position
        file.write(new_bytes)

# Usage example
file_path = 'example.txt'
replace_position = 4  # Position to replace
replacement_string = '01234'  # String to replace

replace_bytes_in_file(file_path, replace_position, replacement_string)
