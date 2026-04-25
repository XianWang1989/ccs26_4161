
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'ab+') as f:
        f.seek(position[0])
        f.write(new_bytes.encode('utf-8'))
        f.truncate()  # Ensure the file doesn't retain old content beyond the new bytes

# Example usage
file_path = 'example.txt'  # Make sure this file exists
position = (4, 0)  # Replace bytes starting from index 4
new_string = '01234'
replace_bytes_in_file(file_path, position, new_string)

# Read back to verify the change
with open(file_path, 'rb') as f:
    content = f.read()
    print(content.decode('utf-8'))  # To see the final content in the file
