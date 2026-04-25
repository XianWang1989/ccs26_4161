
# Define the file name and the string to replace
filename = 'example.txt'
replacement_string = b'01234'  # bytes to write

# Specify the position (4, 0) as a single offset
# In this case, we want to start writing at byte position 4
position = 4

# Open the file in 'r+b' mode (read and write in binary)
with open(filename, 'r+b') as file:
    # Seek to the desired position
    file.seek(position)

    # Write the replacement bytes
    file.write(replacement_string)

# Output confirmation
print("Bytes replaced successfully.")
