
# File: replace_bytes.py

# Define the file path
file_path = 'example.txt'

# Open the file in 'ab+' mode
with open(file_path, 'ab+') as file:
    # Read the existing content
    file.seek(0)
    content = file.read()

    # New string to insert
    new_string = b'01234'  # Make sure to represent the string as bytes

    # Define the position to start replacing (4, 0)
    start_pos = 4
    end_pos = start_pos + len(new_string)

    # Confirm the file has enough length
    if end_pos <= len(content):
        # Seek to the start position
        file.seek(start_pos)
        # Write the new bytes
        file.write(new_string)

        # Optional: Truncate the file if the new string is shorter
        if len(new_string) < (end_pos - start_pos):
            file.truncate()

        # Output the modified content
        file.seek(0)
        print(file.read().decode('utf-8'))  # Decode for human-readable output
    else:
        print("Error: New string exceeds file length.")
