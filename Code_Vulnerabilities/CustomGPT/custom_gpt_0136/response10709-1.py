
# Open the file in 'ab+' mode
file_path = 'example.txt'

# The string to insert
new_string = "01234".encode('utf-8')  # Convert to bytes

# The position to replace
position = (4, 0)  # Replace starting at index 4

with open(file_path, 'r+b') as file:  # Open in read/write binary mode
    file.seek(position[0])  # Move to the starting position
    file.write(new_string)   # Write the new bytes

# Optional: read back to show the result
with open(file_path, 'rb') as file:
    content = file.read()
    print(content.decode('utf-8'))  # Display the modified content
