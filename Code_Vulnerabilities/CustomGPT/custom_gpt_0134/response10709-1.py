
# Open the file in 'r+b' mode (read and write in binary)
with open('yourfile.txt', 'r+b') as file:
    # Seek to the position (4, 0)
    file.seek(4)  # Move to the 4th byte

    # Prepare the new string to replace "issom"
    new_bytes = b'01234'

    # Write the new bytes
    file.write(new_bytes)

    # Optionally, truncate the file to ensure it isn't longer than needed
    file.truncate()
