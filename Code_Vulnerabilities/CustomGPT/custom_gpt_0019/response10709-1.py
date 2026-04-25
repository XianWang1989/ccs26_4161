
def replace_bytes_in_file(file_path, position, new_string):
    # Open the file in 'r+b' mode to read and write binary data
    with open(file_path, 'r+b') as file:
        # Seek to the specified position
        file.seek(position[0])

        # Read the current data at the position to ensure you know its length
        original_data = file.read(position[1])

        # Move the cursor back to the starting position to overwrite
        file.seek(position[0])

        # Write the new string's bytes, ensuring it matches the length of the original
        file.write(new_string.encode('utf-8'))

        # Optionally, you can truncate the file if the new string is shorter
        # file.truncate()  # Uncomment if needed

# Usage example
file_path = 'example.txt'  # Replace with your file path
replace_bytes_in_file(file_path, (4, 4), '01234')  # Position (4, 4) means start at position 4 and replace 4 bytes
