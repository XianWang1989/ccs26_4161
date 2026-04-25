
# Open the file in 'ab+' mode
with open('your_file.txt', 'ab+') as f:
    # Move the cursor to the desired position (4, 0)
    position = 4
    f.seek(position)

    # The string to replace with
    new_string = '01234'
    # Convert the string to bytes
    new_bytes = new_string.encode()

    # Write the new bytes to the file
    f.write(new_bytes)

# To verify, read the content of the file
with open('your_file.txt', 'rb') as f:
    content = f.read()
    print(content.decode())
