
# Specify the file path
file_path = 'example_file.txt'

# The string to replace and the position
replacement_string = b'01234'  # Use bytes
position = (4, 0)  # Position (4, 0) means starting at byte 4

# Open the file in 'r+b' mode (read and write in binary)
with open(file_path, 'r+b') as file:
    # Move to the specific position
    file.seek(position[0])  # Seek to the byte position
    # Replace bytes in the file
    file.write(replacement_string)

print("Replacement done!")
