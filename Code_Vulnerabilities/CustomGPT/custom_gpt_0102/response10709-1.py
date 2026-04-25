
# Open the file in read and write binary mode
with open('yourfile.txt', 'r+b') as f:
    # Move the cursor to the start position (4, 0) means position 4 in terms of bytes
    f.seek(4)

    # The string to be written (ensure it's in bytes)
    new_string = b'01234'

    # Replace the bytes - make sure the new string is the same length or shorter
    f.write(new_string)

    # Optionally, to fill the rest of the space with spaces if needed
    f.write(b' ' * (5 - len(new_string)))  # Assuming we are replacing 5 bytes

# To verify, read the file content
with open('yourfile.txt', 'rb') as f:
    content = f.read()
    print(content.decode())
