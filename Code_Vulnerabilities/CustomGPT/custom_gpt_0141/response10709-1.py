
def replace_bytes_in_file(file_path, position, new_bytes):
    # Open the file in read-write binary mode ('r+b' allows reading and writing)
    with open(file_path, 'r+b') as f:
        # Seek to the specified position
        f.seek(position)

        # Read the current contents from the position
        original_bytes = f.read(len(new_bytes))
        print(f'Original bytes at position {position}: {original_bytes}')

        # Seek back to the position to write new bytes
        f.seek(position)

        # Write the new bytes to the file
        f.write(new_bytes.encode('utf-8'))  # Encode string to bytes

        # If the new bytes are shorter than the original, truncate the file
        f.truncate()  # This ensures that any leftover bytes are removed

# Example usage
file_path = 'example.txt'  # Path to your file
position = 4                # Position to start replacing
new_string = '01234'       # String to write

# Call the function to replace bytes
replace_bytes_in_file(file_path, position, new_string)

# Check the updated file content
with open(file_path, 'rb') as f:
    print(f.read())  # Read and print the modified content of the file
