
# Function to replace bytes in a file at a specified position
def replace_bytes_in_file(file_path, position, new_string):
    # Open the file in read-write binary mode
    with open(file_path, 'r+b') as file:
        # Move the cursor to the specified position
        file.seek(position[0])

        # Convert the new string to bytes
        new_bytes = new_string.encode('utf-8')

        # Write the new bytes at the current position
        file.write(new_bytes)

# Usage
file_path = 'example.txt'  # Make sure this file exists
position = (4, 0)  # Start position for replacement
new_string = '01234'  # String to write

replace_bytes_in_file(file_path, position, new_string)
