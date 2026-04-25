
# Open the file in binary append/read mode
with open('example.txt', 'ab+') as file:
    # Move to the desired position (4, 0) means position 4
    position = 4
    file.seek(position)  # Move the cursor to position 4

    # The string to replace with
    replacement_bytes = b'01234'

    # Read the existing bytes to ensure we know the size
    original_bytes = file.read()

    # Prepare the new content
    # The part before the position, the replacement, and the part after
    new_content = (
        original_bytes[:position] + 
        replacement_bytes + 
        original_bytes[position + len(replacement_bytes):]
    )

    # Move back to the beginning of the file to write the new content
    file.seek(0)
    file.write(new_content)
