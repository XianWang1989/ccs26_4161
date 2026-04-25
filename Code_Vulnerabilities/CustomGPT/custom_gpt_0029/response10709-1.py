
def replace_bytes_in_file(file_path, start_pos, replace_bytes):
    with open(file_path, 'r+b') as file:
        # Move to the specified start position
        file.seek(start_pos)
        # Overwrite with the new bytes
        file.write(replace_bytes.encode('utf-8'))

# Example usage
file_path = 'example.txt'
replace_string = '01234'
# Replace bytes starting at position 4
replace_bytes_in_file(file_path, 4, replace_string)
