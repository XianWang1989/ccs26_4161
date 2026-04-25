
# Open the file in 'rb+' mode to read and write binary
with open('yourfile.txt', 'rb+') as f:
    # Seek to the desired position (4, 0) means position 4
    f.seek(4)

    # The string to replace 'issom' with
    new_string = b'01234'  # Use bytes

    # Write the new string bytes to the file
    f.write(new_string)

    # Optionally, truncate the file if the new string is shorter than the old one
    # f.truncate()  # Uncomment this if needed

# The content of your file should now reflect the changes
