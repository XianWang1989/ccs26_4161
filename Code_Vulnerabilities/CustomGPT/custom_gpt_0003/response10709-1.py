
# Open the file in 'ab+' mode to read and write bytes
with open('example.txt', 'ab+') as file:
    # Move to the position where you want to start replacing bytes
    file.seek(4)  # Move to position 4

    # Create the new bytes you want to write
    new_bytes = b'01234'  # The bytes to replace the old ones

    # Write the new bytes
    file.write(new_bytes)

    # To visualize the changes, if you want to read back the modified content
    file.seek(0)  # Move back to the start of the file to read the content
    modified_content = file.read()
    print(modified_content)  # Display the modified content
