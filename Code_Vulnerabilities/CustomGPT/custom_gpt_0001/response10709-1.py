
# Open the file in 'r+b' mode (read and write binary).
file_path = 'example.txt'

# The string to be replaced with.
replacement_string = '01234'

# The position where the replacement starts.
start_position = 4  # The position in the file where the replacement begins.

# Open the file and replace the bytes.
with open(file_path, 'r+b') as file:
    # Move the pointer to the start position.
    file.seek(start_position)

    # Write the new string (in bytes).
    file.write(replacement_string.encode('utf-8'))

# Note: If the replacement string is shorter than the original, 
# you may need to handle the remaining characters in the original file.
