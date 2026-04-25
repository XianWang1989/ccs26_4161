
# Specify the file path
file_path = 'example_file.txt'

# String to replace
replacement_string = b'01234'  # Use bytes for binary mode

# Position to replace (4, 0) means starting at byte 4
start_position = 4
end_position = start_position + len(replacement_string)

# Open the file in 'ab+' mode to read and write
with open(file_path, 'rb+') as file:
    # Seek to the start position
    file.seek(start_position)

    # Replace bytes
    file.write(replacement_string)

    # Optional: If you want to fill the leftover with spaces (for keeping file size same)
    current_pos = file.tell()
    file.seek(end_position)
    file.write(b'\x20' * (end_position - current_pos))  # Fill with space if needed

# Now, the file has 'this01234ethingasperfectlygood.'
