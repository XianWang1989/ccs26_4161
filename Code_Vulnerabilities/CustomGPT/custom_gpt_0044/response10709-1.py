
# Define the file path and the string to replace
file_path = 'your_file.txt'
string_to_replace = '01234'
position = (4, 0)  # (byte offset, line offset, here line offset isn't used)

# Open the file in 'ab+' mode
with open(file_path, 'r+b') as file:
    # Seek to position (4 bytes from the start)
    file.seek(position[0])

    # Write the new bytes
    file.write(string_to_replace.encode())

# Confirm changes
with open(file_path, 'rb') as file:
    print(file.read().decode())
