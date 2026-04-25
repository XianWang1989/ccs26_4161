
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'r+b') as file:
        # Move the cursor to the specified position
        file.seek(position)

        # Write the new bytes at the current position
        file.write(new_bytes)

# Usage
file_path = 'your_file.txt'
position = 4  # The position to start replacing
new_string = "01234"

# Convert the new string to bytes
new_bytes = new_string.encode('utf-8')

# Call the function to replace the bytes in the file
replace_bytes_in_file(file_path, position, new_bytes)

print("Bytes replaced successfully.")
