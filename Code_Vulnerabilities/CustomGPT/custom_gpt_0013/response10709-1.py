
# Define the file path
file_path = 'example.txt'

# Open the file in 'ab+' mode
with open(file_path, 'ab+') as file:
    # Seek to position (4, 0) - 4 bytes from the start
    file.seek(4)

    # Prepare the new string
    new_str = '01234'

    # Convert the string to bytes
    new_bytes = new_str.encode('utf-8')

    # Read the current content after the position
    current_content = file.read()

    # Calculate the total bytes we need to replace
    total_bytes_to_replace = len(new_bytes)

    # Move back to the starting position and write the new bytes
    file.seek(4)  # Go back to position 4
    file.write(new_bytes)

    # Append the remaining content
    file.write(current_content[total_bytes_to_replace:])

# Verify the changes
with open(file_path, 'r') as file:
    print(file.read())
