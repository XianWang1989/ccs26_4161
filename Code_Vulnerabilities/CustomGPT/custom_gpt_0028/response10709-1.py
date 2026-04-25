
def replace_bytes_in_file(filename, position, new_bytes):
    # Open the file in binary append and read mode
    with open(filename, 'ab+') as file:
        # Move the cursor to the specified position
        file.seek(position)

        # Get the current position and read the rest of the file
        original_content = file.read()

        # Move the cursor back to the specified position
        file.seek(position)

        # Write the new bytes
        file.write(new_bytes.encode())

        # Optionally, write back the remaining original content
        file.write(original_content[len(new_bytes):])

# Usage
filename = 'example_file.txt'
position = 4  # Specify the position
new_string = '01234'  # New bytes to write
replace_bytes_in_file(filename, position, new_string)
