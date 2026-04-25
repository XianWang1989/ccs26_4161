
# Define the file path
file_path = 'example.txt'

# Open the file in 'r+b' (read and write in binary) mode
with open(file_path, 'r+b') as file:
    # Seek to position 4
    position = 4
    file.seek(position)

    # Define the new bytes to write
    new_bytes = b'01234'

    # Write the new bytes
    file.write(new_bytes)

# Optionally, you can verify the change
with open(file_path, 'rb') as file:
    content = file.read()
    print(content.decode())
