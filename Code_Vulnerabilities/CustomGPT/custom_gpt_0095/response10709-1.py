
# Define the file name and the new string
file_name = 'example_file.txt'
new_string = b'01234'  # Ensure this is a bytes object

# Open the file in read/write binary mode
with open(file_name, 'r+b') as f:
    # Move the file pointer to position 4 (0-based index)
    f.seek(4)

    # Write the new bytes to the file
    f.write(new_string)

# The file now has "this01234ethingasperfectlygood."
