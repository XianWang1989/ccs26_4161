
def replace_bytes_in_file(file_path, position, replacement_string):
    # Open the file in binary mode for read and write
    with open(file_path, 'r+b') as file:
        # Seek to the desired position
        file.seek(position[0])  # The byte position to start replacing
        # Convert the string to bytes
        replacement_bytes = replacement_string.encode('utf-8')
        # Calculate the length to overwrite
        length_to_replace = len(replacement_bytes)

        # Read the existing content
        original_content = file.read()
        # Prepare the new content
        new_content = (
            original_content[:position[0]] + 
            replacement_bytes + 
            original_content[position[0] + length_to_replace:]
        )

        # Move to the start position and write the new content
        file.seek(position[0])
        file.write(new_content)

# Example usage
file_path = 'example.txt'  # Path to your file
replace_bytes_in_file(file_path, (4, 0), '01234')
