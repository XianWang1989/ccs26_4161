
# The file name you want to operate on
file_name = 'example_file.txt'

# The string you want to insert
replacement_string = b'01234'  # Must be in bytes

# Position to replace (start byte, offset)
start_position = 4
offset = 0

# Calculate the target position
target_position = start_position + offset

with open(file_name, 'r+b') as file:  # Open the file in read/write binary mode
    file.seek(target_position)  # Move to the target position
    file.write(replacement_string)  # Write the replacement bytes

# The final output in the file will show the replacement.
