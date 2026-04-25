
# Open the file in binary append mode
with open('your_file.txt', 'rb+') as file:
    # Specify the starting position and the content to be written
    position = (4, 0)  # (4, 0) means we want to start from the 4th byte
    replacement_string = "01234"

    # Convert the string to bytes
    replacement_bytes = replacement_string.encode('utf-8')

    # Seek to the specified position in the file
    file.seek(position[0])

    # Read the existing bytes to get context (optional)
    original_bytes = file.read(len(replacement_bytes))

    # Move back to the desired position to write the replacement bytes
    file.seek(position[0])

    # Write the replacement bytes
    file.write(replacement_bytes)

# After running this, 'your_file.txt' will now have "issom" replaced with "01234".
