
# Open the file in 'ab+' mode (append binary)
with open('example_file.txt', 'ab+') as f:
    # If the initial content is not present, write it first
    f.write(b"thisissomethingasperfectlygood.")

    # Seek to the desired position where you want to start replacing
    # In this case, position (4, 0) means starting at byte index 4
    position = 4
    f.seek(position)

    # Prepare the new byte string you want to write
    new_bytes = b"01234"

    # Write the new bytes
    f.write(new_bytes)

    # To verify the result, seek back to the beginning and read the content
    f.seek(0)  # Go back to the start of the file
    updated_content = f.read()
    print(updated_content.decode('utf-8'))  # Decode the bytes to string for display
