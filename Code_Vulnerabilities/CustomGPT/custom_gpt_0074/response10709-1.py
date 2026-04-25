
# Open the file in binary mode to read and write bytes
with open('your_file.txt', 'r+b') as file:
    # Seek to position (4, 0)
    position = 4  # The starting position to write
    file.seek(position)  # Move the pointer to the desired position

    # Prepare the string to write
    replacement_string = b'01234'  # Make sure to use bytes
    file.write(replacement_string)  # Write the new bytes at the current position

# Now the file will have "this01234ethingasperfectlygood."
