
# Open the file in 'ab+' mode
with open('your_file.bin', 'ab+') as file:
    # Move to the desired position (4, 0) means position 4
    position = 4
    file.seek(position)

    # The string to write
    new_string = b'01234'

    # Replace 4 bytes in the file starting from position 4
    file.write(new_string)

# To verify the change, read the content of the file
with open('your_file.bin', 'rb') as file:
    content = file.read()
    print(content)  # Prints updated content
