
# Open the file in 'ab+' mode
with open('example_file.txt', 'ab+') as file:
    # Example initial content
    initial_content = b'thisissomethingasperfectlygood.'
    file.write(initial_content)

    # Seek to the position where you want to start replacing
    # Position (4, 0) means start from index 4 (0-based)
    file.seek(4)

    # Replace 'issom' with '01234'
    new_bytes = b'01234'
    file.write(new_bytes)

    # Move back to the beginning to read the file content
    file.seek(0)

    # Print the updated content
    updated_content = file.read()
    print(updated_content.decode())
