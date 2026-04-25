
# Open the file in 'r+b' mode to read and write
with open('yourfile.txt', 'r+b') as f:
    # Move to the position (4, 0) which means starting at byte 4
    f.seek(4)  # Seek to the desired position

    # Create the replacement bytes
    replacement = b'01234'

    # Write the replacement bytes at the current position
    f.write(replacement)

# Verify by reading the modified file
with open('yourfile.txt', 'rb') as f:
    content = f.read()
    print(content)  # Output should show the modified content
