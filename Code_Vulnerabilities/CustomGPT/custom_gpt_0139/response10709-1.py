
# Example function to replace bytes in a file at a given position
def replace_bytes_in_file(file_path, position, replacement_str):
    # Open the file in 'r+b' mode to allow reading and writing
    with open(file_path, 'r+b') as file:
        # Move to the given position
        file.seek(position[0])
        # Create a bytes object from the replacement string
        replacement_bytes = replacement_str.encode('utf-8')
        # Write the bytes to the file at the current position
        file.write(replacement_bytes)

# Example usage
file_path = 'example.txt'  # Path to your file
replace_position = (4, 0)   # Position (4, 0) means start from byte 4
replacement_string = '01234' # The string to insert

replace_bytes_in_file(file_path, replace_position, replacement_string)

# To verify that the replacement was done, you can read the file content
with open(file_path, 'rb') as file:
    content = file.read()
    print(content.decode('utf-8'))  # Print the modified content
