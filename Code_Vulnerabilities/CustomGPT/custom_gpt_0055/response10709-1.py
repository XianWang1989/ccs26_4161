
def replace_bytes_in_file(file_path, position, new_bytes):
    # Open the file in binary append/read mode
    with open(file_path, 'r+b') as file:
        # Seek to the specified position
        file.seek(position[0])
        # Write the new bytes
        file.write(new_bytes.encode('utf-8'))

# Specify the file path
file_path = 'example.txt'

# Replace "issom" at position (4, 0) with "01234"
position = (4, 0)
new_string = "01234"

# Call the function
replace_bytes_in_file(file_path, position, new_string)

# Verify by reading the modified file
with open(file_path, 'rb') as file:
    print(file.read().decode('utf-8'))
