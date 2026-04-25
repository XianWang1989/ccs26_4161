
# Specify the file name
filename = 'example.txt'

# Open the file in 'ab+' mode
with open(filename, 'ab+') as file:
    # Seek to the position where you want to replace bytes
    position = 4  # Position to start replacing
    file.seek(position)

    # Read bytes that need to remain intact after replacement
    remaining_data = file.read()  # Read the rest of the file after the position

    # Create the new bytes to insert
    new_string = '01234'
    new_bytes = new_string.encode()  # Convert the string to bytes

    # Move back to the position to write the new bytes
    file.seek(position)

    # Write the new bytes into the file
    file.write(new_bytes)

    # If you need to restore the rest of the file after writing (optional)
    file.write(remaining_data)

# Notify to user that operation was successful
print(f"Replaced bytes starting at position {position} with '{new_string}' in '{filename}'.")
