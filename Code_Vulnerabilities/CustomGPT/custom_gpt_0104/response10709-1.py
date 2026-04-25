
# Open the file in read/write binary mode
with open('yourfile.txt', 'r+b') as file:
    # Move to the desired position to replace bytes
    position = 4  # The byte offset where you want to start replacing
    file.seek(position)

    # The new bytes you want to write
    new_string = b'01234'

    # Write the new bytes to the file
    file.write(new_string)

    # Check the new contents by reading back from the start
    file.seek(0)  # Go back to the start of the file
    content = file.read()
    print(content.decode())  # Decode from bytes to string for display

# Make sure to update the file path and contents as required
