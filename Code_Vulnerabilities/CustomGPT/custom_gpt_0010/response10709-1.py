
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'r+b') as f:  # Open in read and binary write mode
        f.seek(position[0])  # Move to the specified byte position
        f.write(new_bytes.encode('utf-8'))  # Write the new bytes

# Example usage
file_path = 'example.txt'  # Your file name
position = (4, 0)  # Start replacing from position 4
new_string = '01234'  # String to insert

replace_bytes_in_file(file_path, position, new_string)

# After execution, the file will have the bytes replaced
