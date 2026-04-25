
def replace_bytes_in_file(file_path, position, string_to_replace):
    # Open the file in 'ab+' mode
    with open(file_path, 'r+b') as file:
        # Seek to the given position
        file.seek(position[0])

        # Write the new bytes
        file.write(string_to_replace.encode())

# Example usage
file_path = 'example_file.txt'  # specify your file path
position = (4, 0)  # (byte position, offset is ignored here)
string_to_replace = '01234'

replace_bytes_in_file(file_path, position, string_to_replace)
