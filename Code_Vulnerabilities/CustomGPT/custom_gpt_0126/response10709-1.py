
# Define the file name and the replacement string
file_name = 'example_file.txt'
replacement_string = '01234'
start_position = 4  # Starting byte position to replace
length_to_replace = 4  # Number of bytes to replace

# Open the file in 'r+b' mode for reading and writing
with open(file_name, 'r+b') as file:
    # Seek to the specified position
    file.seek(start_position)

    # Write the bytes of the replacement string
    file.write(replacement_string.encode('utf-8'))

    # If the replacement string is shorter, truncate the file
    # Move back to the end of the original string section
    file.truncate(start_position + len(replacement_string))

# Now the file contains the modified string.
