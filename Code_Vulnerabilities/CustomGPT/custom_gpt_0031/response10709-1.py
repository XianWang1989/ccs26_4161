
# Open the file in 'r+b' mode to allow reading and writing
with open('file.txt', 'r+b') as f:
    # Seek to the specified position (4, 0)
    position = 4
    f.seek(position)

    # Create the bytes to write
    new_bytes = b'01234'

    # Write the new bytes to the file
    f.write(new_bytes)

# Ensure the changes are saved
print("Bytes replaced in the file successfully.")
