
# Example of replacing bytes in a file at a specified position

# Define the string to replace and the position
replacement_string = b'01234'
position = (4, 0)  # Start position for replacement (4, 0)

# Open the file in 'ab+' mode
with open('example_file.txt', 'ab+') as f:
    # Move to the specified position
    f.seek(position[0])  # Position the pointer at the start index

    # Read the current content
    current_content = f.read()

    # Create a new content by replacing the specified bytes
    new_content = current_content[:position[0]] + replacement_string + current_content[position[0] + len(replacement_string):]

    # Move back to the start position
    f.seek(0)

    # Write the new content back to the file
    f.write(new_content)
