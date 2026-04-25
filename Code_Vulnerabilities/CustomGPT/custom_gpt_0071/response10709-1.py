
# Define the file path and the replacement values
file_path = 'your_file.txt'
replacement_string = b'01234'  # bytes to write
start_position = 4  # starting position to replace

# Open the file in 'r+b' mode to read and write binary data
with open(file_path, 'r+b') as file:
    # Move the cursor to the desired start position
    file.seek(start_position)

    # Write the replacement bytes
    file.write(replacement_string)

# Verification (optional)
with open(file_path, 'rb') as file:
    content = file.read()
    print(content)  # Output the modified content
