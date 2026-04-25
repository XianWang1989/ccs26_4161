
# Define the file name
file_name = "example.txt"

# The string to write
replacement_string = b"01234"  # Use bytes for binary mode

# Function to replace bytes in the file
def replace_bytes_in_file(file_name, position, replacement_string):
    with open(file_name, 'r+b') as file:  # Open file in read and write binary mode
        file.seek(position)  # Seek to the specified position
        file.write(replacement_string)  # Write the replacement bytes

# Specify position to start replacing (4, 0 means offset 4)
position = 4  

# Call the function
replace_bytes_in_file(file_name, position, replacement_string)

# For testing, let's read the modified file content
with open(file_name, 'rb') as file:
    content = file.read()
    print(content.decode())  # Decode bytes to read as string
