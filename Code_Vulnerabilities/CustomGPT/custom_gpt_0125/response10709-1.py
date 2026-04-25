
def replace_bytes_in_file(file_path, start_pos, new_bytes):
    with open(file_path, 'r+b') as f:
        f.seek(start_pos)  # Move to the start position
        f.write(new_bytes.encode('utf-8'))  # Write the new bytes

# Example usage
file_path = 'example_file.txt'
start_position = 4  # Start replacing at position 4
replacement_string = '01234'

replace_bytes_in_file(file_path, start_position, replacement_string)
