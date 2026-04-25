
# Open the file in 'ab+' mode
with open('example_file.txt', 'ab+') as f:
    # Seek to the position (4, 0)
    # Here, '4' is the byte offset from the start of the file
    f.seek(4)

    # Replace "issom" with "01234"
    # Calculate how many bytes to replace (4 in this case)
    replace_bytes = b'01234'

    # Read the current content to preserve the part after the replace position
    current_content = f.read()

    # Move the pointer back to the position to write
    f.seek(4)

    # Write the new bytes to the file
    f.write(replace_bytes)

    # Write back the remaining content
    f.write(current_content)

# Check the content of the file
with open('example_file.txt', 'rb') as f:
    print(f.read())  # Output: b'this01234ethingasperfectlygood.'
