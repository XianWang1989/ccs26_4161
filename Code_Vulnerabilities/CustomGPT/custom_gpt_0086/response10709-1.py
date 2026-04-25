
def replace_bytes_in_file(file_path, position, new_bytes):
    # Open the file in 'r+b' mode to read and write binary
    with open(file_path, 'r+b') as file:
        # Move the cursor to the specified position
        file.seek(position)
        # Write the new bytes to file
        file.write(new_bytes)

# Example usage
file_path = 'example.txt'  # Replace with your file path
position = 4                # Starting position for the replacement
new_string = '01234'       # The string to replace with

# Convert the string to bytes
new_bytes = new_string.encode('utf-8')

# Replace bytes in the file
replace_bytes_in_file(file_path, position, new_bytes)

# Output to verify the content
with open(file_path, 'rb') as file:
    print(file.read().decode('utf-8'))
