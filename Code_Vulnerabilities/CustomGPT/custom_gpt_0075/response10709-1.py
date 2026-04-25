
def replace_bytes_in_file(file_path, position, replacement_string):
    # Open the file in 'ab+' mode
    with open(file_path, 'r+b') as file:
        # Seek to the desired position
        file.seek(position[0])

        # Read current bytes at the position
        current_bytes = file.read(position[1])

        # Check if replacement fits the original range
        if len(replacement_string) != position[1]:
            raise ValueError("Replacement string must match the length of bytes to replace.")

        # Move the cursor back to the start of the position to replace
        file.seek(position[0])

        # Write the new bytes
        file.write(replacement_string.encode())

        # Flush changes to the file
        file.flush()

# Example usage
file_path = 'example.txt'  # Adjust this path as needed
replacement_string = '01234'
position = (4, 5)  # Replace 5 bytes starting from position 4

replace_bytes_in_file(file_path, position, replacement_string)
