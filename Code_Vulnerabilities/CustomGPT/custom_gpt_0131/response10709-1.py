
# Open the file in 'rb+' mode to read and write binary data
with open('your_file.txt', 'rb+') as file:
    # Move the cursor to the desired position (4, 0) in this case
    position = 4
    file.seek(position)

    # The string you want to insert
    replacement_string = b'01234'  # Ensure this is in bytes

    # Write the replacement string to the file
    file.write(replacement_string)

    # Optional: Fill the remainder of the replacement with spaces or zeros
    # Depending on the context you might want it to be filled or not
    # offset = len('issom') - len(replacement_string)
    # if offset > 0:
    #     file.write(b' ' * offset)  # only if you want to maintain length

# Closing file is done automatically with the 'with' statement
