
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'r+b') as file:
        # Move to the specified position
        file.seek(position[0])
        # Write the new bytes
        file.write(new_bytes.encode())

# Example usage
file_path = 'example.txt'
position = (4, 0)  # Start at byte position 4
new_string = '01234'  # The string to write

replace_bytes_in_file(file_path, position, new_string)
