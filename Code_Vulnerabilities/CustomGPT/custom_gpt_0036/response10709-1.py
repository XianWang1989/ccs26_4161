
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'r+b') as file:
        # Seek to the position in the file where we want to start replacing
        file.seek(position[0] + position[1])

        # Read the contents from the position to get the exact bytes we may want to replace
        old_bytes = file.read(len(new_bytes))

        # Check length compatibility
        if len(old_bytes) != len(new_bytes):
            raise ValueError("The new byte string must be of the same length as the old bytes being replaced.")

        # Seek back to the position to write new bytes
        file.seek(position[0] + position[1])
        file.write(new_bytes)

# Example usage
file_path = 'example.txt'
# Replace bytes starting from index 4, replace 4 bytes
position = (0, 4)  # (line, index in the line)
new_string = '01234'

# Converting the string to bytes
new_bytes = new_string.encode('utf-8')

replace_bytes_in_file(file_path, position, new_bytes)
