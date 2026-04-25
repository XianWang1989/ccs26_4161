
# Open the file in append and binary mode
with open('example.bin', 'ab+') as file:
    # Move to the desired position (4 bytes in)
    position = 4
    file.seek(position)

    # Create the replacement bytes
    replacement = b'01234'

    # Get the current content from the position
    current_bytes = file.read(5)  # Read 5 bytes to replace "issom"

    # Move back to the position to overwrite
    file.seek(position)

    # Write the replacement bytes
    file.write(replacement)

    # Optional: Write back the remaining bytes if needed
    remaining_bytes = current_bytes[5:]  # Keep any remaining bytes after replacement
    file.write(remaining_bytes)

# To verify, read the file back
with open('example.bin', 'rb') as file:
    content = file.read()
    print(content.decode('utf-8', errors='ignore'))
