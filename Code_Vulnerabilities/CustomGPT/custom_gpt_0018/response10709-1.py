
# Define the position tuple as (4, 0)
position = (4, 0)  # Position in the file where to replace starts at 4

# The string to write into the file
replacement_string = "01234"

# Open the file in read and write binary mode
with open('yourfile.txt', 'r+b') as f:
    # Move the file cursor to the position (4 in this case)
    f.seek(position[0])  # Move to byte position 4

    # Write the replacement string as bytes
    f.write(replacement_string.encode('utf-8'))

# At the end of your operation, the file content would have the changes.
