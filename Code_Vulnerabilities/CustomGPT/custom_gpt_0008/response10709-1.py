
# Open the file in 'r+b' mode to read and write in binary
with open('example.txt', 'r+b') as file:
    # Move the cursor to the desired position (4, 0) means position 4
    position = 4
    file.seek(position)

    # String to write
    replacement_string = "01234"

    # Replace the bytes
    # Read the existing bytes to check length
    original_bytes = file.read(4)  # Read 4 bytes to replace
    print("Original bytes:", original_bytes)

    # Seek back to the position to overwrite
    file.seek(position)

    # Write the new bytes
    file.write(replacement_string.encode('utf-8'))

# Confirm the changes by reading the file
with open('example.txt', 'rb') as file:
    content = file.read()
    print("Modified file content:", content.decode('utf-8'))
