
# Define the file path
file_path = 'example.txt'

# The string to replace and its corresponding bytes
new_string = b'01234'

# The specific position to replace (4, 0)
seek_position = 4  # Start replacing at byte position 4

# Open the file in binary append mode
with open(file_path, 'rb+') as file:
    # Seek to the given position
    file.seek(seek_position)

    # Write the new string bytes
    file.write(new_string)

# Confirming the changes
with open(file_path, 'rb') as file:
    content = file.read()
    print(content.decode('utf-8'))  # Display updated content
