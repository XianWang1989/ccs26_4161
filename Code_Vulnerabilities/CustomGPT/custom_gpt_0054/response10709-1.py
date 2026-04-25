
def replace_bytes_in_file(file_path, position, replacement_string):
    # Open the file in 'r+b' mode for reading and writing
    with open(file_path, 'r+b') as file:
        # Move the pointer to the position specified
        file.seek(position[0])

        # Calculate the length of the replacement string
        len_replacement = len(replacement_string)

        # Read the existing bytes to determine how many bytes to overwrite
        existing_bytes = file.read(len_replacement)

        # Move back the pointer to the position to write the new bytes
        file.seek(position[0])

        # Write the replacement bytes
        file.write(replacement_string.encode())

        # If the replacement is shorter, you may consider truncating the file
        # Uncomment the following line to truncate the file if needed
        # file.truncate()

# Example usage
file_path = 'your_file.txt'  # Replace with your actual file path
replacement_string = '01234'
position = (4, 0)  # Replace from the 4th byte

replace_bytes_in_file(file_path, position, replacement_string)
