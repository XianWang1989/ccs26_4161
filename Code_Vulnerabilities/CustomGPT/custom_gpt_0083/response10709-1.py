
# Open the file in 'r+b' mode (read and write binary)
with open('example.txt', 'r+b') as file:
    # Seek to position (4, 0) which is the 4th byte
    file.seek(4) 

    # Define the replacement string
    replacement = b'01234'

    # Write the replacement bytes
    file.write(replacement)
