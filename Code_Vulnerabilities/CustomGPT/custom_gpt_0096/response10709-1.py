
# Open the file in 'ab+' mode (binary append and read)
file_path = 'example_file.txt'

# The string to insert
replacement_string = b'01234'  # Use bytes for binary mode

# Starting position to replace (4, 0) indicates position 4
start_position = 4
replacement_length = len(replacement_string)

with open(file_path, 'r+b') as file:
    # Move to the start position
    file.seek(start_position)

    # Read existing data that will be replaced
    original_data = file.read(replacement_length)

    # Ensure we're overwriting the same number of bytes
    if len(original_data) < replacement_length:
        raise ValueError("Replacement string is longer than the space available.")

    # Move back to the start position to write
    file.seek(start_position)

    # Write the new string in the file
    file.write(replacement_string)

# Confirmation message
print("Replacement completed.")
