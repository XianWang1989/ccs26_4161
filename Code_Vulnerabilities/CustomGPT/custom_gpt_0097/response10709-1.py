
# Define the file path
file_path = 'example.txt'

# Open the file in binary append mode
with open(file_path, 'ab+') as f:
    # Seek to the desired position (4, 0 means 4 bytes from the start)
    f.seek(4)

    # Create the new byte string
    new_bytes = b'01234'

    # Read the current content (to verify or process later if needed)
    f.seek(0)
    content = f.read()

    # Print the current content for reference
    print("Current Content:", content)

    # Move the pointer back to the position and write the new bytes
    f.seek(4)
    f.write(new_bytes)

    # Optionally, move the pointer to the start and read the updated content
    f.seek(0)
    updated_content = f.read()

# Print the updated content
print("Updated Content:", updated_content)
