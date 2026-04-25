
# Define the file path and the string to insert
file_path = 'example.txt'
new_string = b'01234'  # Note: Use bytes
start_position = 4  # Starting position to replace

# Open the file in binary read/write mode
with open(file_path, 'rb+') as file:
    # Move the cursor to the specified start position
    file.seek(start_position)

    # Read the existing data in the same length as the new string
    existing_data = file.read(len(new_string))

    # Move the cursor back to the start position for replacement
    file.seek(start_position)

    # Write the new bytes to the file
    file.write(new_string)

    # Optional: If you want to see the result immediately, you can seek back and read
    file.seek(0)  # Move to the beginning to read the updated file
    updated_content = file.read()
    print(updated_content.decode())  # Print the content as string
