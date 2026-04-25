
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'r+b') as file:  # Open the file in read and write binary mode
        file.seek(position[0])  # Move to the given position
        file.write(new_bytes.encode())  # Write the new bytes at the current position

# Example usage
file_path = 'example_file.bin'  # Path to your binary file
position = (4, 0)  # Position to start replacing (4 bytes in this case)
new_string = '01234'  # String to replace with

replace_bytes_in_file(file_path, position, new_string)
