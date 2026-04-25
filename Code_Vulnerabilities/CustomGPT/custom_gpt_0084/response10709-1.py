
def replace_bytes_in_file(file_path, position, new_bytes):
    # Open the file in 'r+b' mode to allow reading and writing
    with open(file_path, 'r+b') as file:
        # Move the pointer to the specified position
        file.seek(position[0])
        # Write the new bytes to the file
        file.write(new_bytes.encode('utf-8'))  # Ensure the new string is encoded to bytes

# Example usage
file_path = 'example.txt'
position = (4, 0)  # Start from position 4
new_string = '01234'

replace_bytes_in_file(file_path, position, new_string)

# Optional: Read back the file to show results
with open(file_path, 'r') as file:
    modified_content = file.read()
    print(modified_content)
