
# Open the file in 'r+b' mode to read and write binary
with open('your_file.txt', 'r+b') as file:
    # Seek to position (4, 0)
    # In this case, you want to go to the 4th byte (0-indexed)
    file.seek(4) 

    # The string you want to write
    new_string = b'01234'  # Ensure it's bytes

    # Write the new string, replacing the original bytes
    file.write(new_string)

    # Optionally: To verify the change, reset and read the file content
    file.seek(0)
    content = file.read()
    print(content.decode())  # Print the updated content
