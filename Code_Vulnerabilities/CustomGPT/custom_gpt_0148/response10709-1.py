
# Specify the file path
file_path = 'example.txt'

# The string to write
new_string = b'01234'  # Note: binary string
# The position where to start replacing
start_position = 4

# Open the file in binary read/write mode
with open(file_path, 'rb+') as file:
    # Move the file pointer to the desired position
    file.seek(start_position)

    # Read the current bytes for verification (optional)
    original_bytes = file.read(5)  # Read the bytes to be replaced
    print(f"Original bytes: {original_bytes}")

    # Write the new bytes
    file.seek(start_position)  # Go back to the starting position
    file.write(new_string)

# Confirm the changes
with open(file_path, 'rb') as file:
    updated_content = file.read()
    print(f"Updated content: {updated_content}")
