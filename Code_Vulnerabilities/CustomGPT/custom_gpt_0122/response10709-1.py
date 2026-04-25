
def replace_bytes_in_file(filename, position, new_bytes):
    with open(filename, 'r+b') as file:  # Open the file in read/write binary mode
        file.seek(position[0])  # Move to the specified byte position
        file.write(new_bytes.encode())  # Write new bytes (encode string to bytes)

# Usage
filename = 'yourfile.txt'  # specify your file name
position = (4, 0)  # (byte position, unused offset)
new_string = '01234'  # the string you want to write

replace_bytes_in_file(filename, position, new_string)
