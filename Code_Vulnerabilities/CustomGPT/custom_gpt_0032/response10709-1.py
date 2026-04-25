
# Open the file in 'ab+' mode
with open('yourfile.txt', 'ab+') as file:
    # Move the cursor to the desired position (4, 0) which is the start of 5th byte
    position = 4
    file.seek(position)

    # The bytes you want to write
    new_bytes = b'01234'

    # Read the existing content to ensure we maintain its structure
    # Save the rest of the file after the position
    remaining_content = file.read()

    # Write the new bytes at the specified position
    file.seek(position)
    file.write(new_bytes)

    # Append the remaining content back into the file
    file.write(remaining_content)

# Output to verify the changes
with open('yourfile.txt', 'rb') as file:
    print(file.read())  # Print the modified content
