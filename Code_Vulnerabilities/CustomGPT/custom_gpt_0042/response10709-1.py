
# Define the function to replace bytes in a file
def replace_bytes_in_file(file_path, position, new_bytes):
    # Open the file in binary mode
    with open(file_path, 'r+b') as file:
        # Move the cursor to the specified position
        file.seek(position[0])
        # Write the new bytes at the given position
        file.write(new_bytes)

# Example usage
file_path = 'example.txt'  # Path to your file

# The bytes you want to write
new_bytes = b'01234'

# Position where you want to start writing (4 means 4th byte)
position = (4, 0)

# Replace bytes in the file
replace_bytes_in_file(file_path, position, new_bytes)

# If you wish to see the result, you can read the file back afterwards
with open(file_path, 'rb') as file:
    print(file.read())
