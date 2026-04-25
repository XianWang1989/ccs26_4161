
# Open the file in 'r+b' mode to read and write in binary
with open('your_file.txt', 'r+b') as file:
    # Move the cursor to the desired position (4, 0)
    position = 4
    file.seek(position)

    # Prepare the string to replace, ensuring binary format
    string_to_write = b'01234'

    # Write the bytes to the file
    file.write(string_to_write)

# Optionally, verify the result by reading the modified content
with open('your_file.txt', 'rb') as file:
    content = file.read()
    print(content.decode())  # Print the modified content as a string
