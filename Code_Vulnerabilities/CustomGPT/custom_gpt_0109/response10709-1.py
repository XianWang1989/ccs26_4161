
def replace_bytes_in_file(file_path, position, new_string):
    # Open the file in 'r+b' mode (read and write in binary)
    with open(file_path, 'r+b') as file:
        # Seek to the specified position
        file.seek(position[0])  # Move to the byte position
        # Write the new string as bytes
        file.write(new_string.encode())

# Usage
file_path = 'example_file.bin'  # Replace with your file path
replace_position = (4, 0)        # Position (4, 0) means position 4
new_string = '01234'             # String to write

replace_bytes_in_file(file_path, replace_position, new_string)
