
# Define the file path
file_path = 'example_file.txt'

# Open the file in binary append mode
with open(file_path, 'ab+') as file:
    # The string to insert
    new_bytes = b'01234'

    # Define the position to insert the new bytes
    position = (4, 0)

    # Seek to the desired position
    file.seek(position[0])

    # Write the new bytes
    file.write(new_bytes)
