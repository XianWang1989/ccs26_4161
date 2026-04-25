
def replace_bytes_in_file(file_path, position, new_bytes):
    with open(file_path, 'rb+') as file:
        # Seek to the specified position
        file.seek(position[0])

        # Write the new bytes
        file.write(new_bytes)

# Example usage
file_path = 'example.txt'  # Path to your file
position = (4, 0)  # Seek to byte position 4
new_string = '01234'
new_bytes = new_string.encode('utf-8')  # Convert string to bytes

replace_bytes_in_file(file_path, position, new_bytes)
