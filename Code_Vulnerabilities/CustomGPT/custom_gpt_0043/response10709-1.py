
# Replace bytes in a binary file by given position

# Open the file in 'ab+' mode to read and write to binary
with open('example_file.bin', 'ab+') as file:
    # First, seek to the specified position
    position = 4  # The starting position in the file
    file.seek(position)  # Move to the desired position in the file

    # Prepare the new string to write (in bytes)
    new_string = b'01234'  # Note: The string must be in bytes

    # Read the current content to know the length of the replacement
    original_content = file.read()
    print("Original content:", original_content)

    # Calculate the number of bytes to overwrite
    bytes_to_overwrite = len(new_string)

    # If needed, adjust the content after the replaced section
    # You can read the bytes after the target...
    remaining_content = original_content[position + bytes_to_overwrite:]

    # Clear the current position and write the new string
    file.seek(position)  # Go back to the position to overwrite
    file.write(new_string)  # Write the new string

    # Extend the remaining content after the inserted bytes
    file.write(remaining_content)  # Write the remaining content

# Re-open the file to read the updated content
with open('example_file.bin', 'rb') as file:
    updated_content = file.read()
    print("Updated content:", updated_content)
