
def replace_bytes_in_file(file_path, position, new_bytes):
    # Open the file in 'r+b' mode to read and write binary data
    with open(file_path, 'r+b') as file:
        # Move the file pointer to the specified position
        file.seek(position[0])  # position[0] is the byte offset
        # Write the new bytes at the specified position
        file.write(new_bytes.encode())  # Convert string to bytes

# Example usage
file_path = 'example.txt'
replace_position = (4, 0)  # Start replacing at byte 4
new_string = "01234"  # String to replace

replace_bytes_in_file(file_path, replace_position, new_string)
