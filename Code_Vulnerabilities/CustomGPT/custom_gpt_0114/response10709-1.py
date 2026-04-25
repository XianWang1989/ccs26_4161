
# Open the file in read and write binary mode
with open('yourfile.bin', 'r+b') as file:
    # Seek to the position (4, 0) as a single index
    position = 4
    file.seek(position)

    # The new bytes to write
    new_bytes = b'01234'

    # Replace the bytes in the file
    file.write(new_bytes)

# Confirm the change by reading back the file
with open('yourfile.bin', 'rb') as file:
    content = file.read()
    print(content)
