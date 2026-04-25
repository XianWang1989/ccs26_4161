
# Example: Replacing bytes in a file at a given position

# Open the file in 'ab+' mode
with open('example.txt', 'ab+') as file:
    # Write initial content for demonstration
    file.write(b'thisis somethingasperfectlygood.\n')

    # Define the position (offset) and string to insert
    position = 4  # Starting position
    new_string = b'01234'  # The string to insert

    # Move to the specified position in the file
    file.seek(position)

    # Read the current contents to keep track
    current_content = file.read()  # Read the rest of the file
    print("Current content after position:", current_content)

    # Move back to the specified position to write
    file.seek(position)

    # Write the new string, and overwrite the length of the old string
    file.write(new_string)

    # To maintain the file length, we can truncate if necessary
    # Seek to the end of the new write
    file.seek(position + len(new_string))

    # Truncate the file here if necessary
    file.truncate()

# Confirm the changes
with open('example.txt', 'rb') as file:
    content = file.read()
    print("Updated file content:", content.decode('utf-8'))
