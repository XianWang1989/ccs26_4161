
# Open the file in 'r+b' mode to read and write in binary
with open('your_file.txt', 'r+b') as file:
    # Define the position to start replacing
    position = (4, 0)
    # The starting byte position
    start_byte = position[0]
    # The replacement string
    replacement_string = '01234'

    # Seek to the specified position
    file.seek(start_byte)

    # Write the replacement string as bytes
    file.write(replacement_string.encode('utf-8'))
