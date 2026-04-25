
def replace_bytes_in_file(file_path, position, new_string):
    # Open the file in 'r+b' mode to read and write bytes
    with open(file_path, 'r+b') as f:
        # Seek to the specified position
        f.seek(position[0])  # Move to the byte position
        # Write the new string as bytes
        f.write(new_string.encode())

# Example usage
file_path = 'example.txt'  # Ensure this file exists with the initial content
new_string = '01234'
position = (4, 0)  # Start position (4, 0) implies byte index 4

replace_bytes_in_file(file_path, position, new_string)

# Read back the content to verify
with open(file_path, 'r') as f:
    content = f.read()
print(content)  # Should output: this01234ethingasperfectlygood.
