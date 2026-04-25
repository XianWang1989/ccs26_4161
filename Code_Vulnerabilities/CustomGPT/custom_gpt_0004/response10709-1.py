
# Open the file in binary append/update mode
with open('example_file.txt', 'ab+') as file:
    # Move to the desired position (4, 0) translates to byte position 4
    position = 4
    file.seek(position)

    # Prepare the string to replace and convert it to bytes
    new_string = "01234".encode()  # Convert to bytes

    # Replace 5 bytes at the given position
    file.write(new_string)

# To verify the result, read the entire file
with open('example_file.txt', 'rb') as file:
    content = file.read()
    print(content.decode())  # Display the content
