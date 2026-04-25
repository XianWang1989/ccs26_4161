
# Define the file name
file_name = 'example.txt'

# String to replace
replacement_string = b'01234'  # Must be in bytes

# Open the file in 'ab+' mode
with open(file_name, 'ab+') as file:
    # Move to position 4
    file.seek(4)

    # Read the existing content to adjust the file size if needed
    current_content = file.read()

    # Move back to position 4 to write the replacement string
    file.seek(4)

    # Replace the bytes by writing the new bytes, ensuring length matches
    # Extend or truncate the file if replacement is shorter or longer
    file.write(replacement_string)

    # If the replacement string is shorter than the original content,
    # you might want to truncate the file to the new size
    new_length = min(len(current_content), 4 + len(replacement_string))
    file.truncate(new_length)

# To verify, read the file back
with open(file_name, 'rb') as file:
    modified_content = file.read()
    print(modified_content)
