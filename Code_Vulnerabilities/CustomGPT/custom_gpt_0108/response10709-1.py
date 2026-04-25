
# Open the file in 'ab+' mode
with open('example_file.txt', 'ab+') as file:
    # Read the existing content
    file.seek(0)
    content = file.read()

    # Position where to start replacing (4, 0)
    start_position = 4
    new_string = b'01234'

    # Go back to the start position
    file.seek(start_position)

    # Replace bytes by writing new bytes and truncating the file
    # Ensure the new string length matches the section being replaced
    old_length = 5  # Length of the string to be replaced
    file.write(new_string)
    file.truncate(start_position + len(new_string))

# Note: The example assumes you want to replace exactly 5 bytes.
