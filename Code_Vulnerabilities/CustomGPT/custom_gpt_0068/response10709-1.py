
# Example file path
file_path = 'example.txt'

# The string we want to write
new_string = b'01234'  # It needs to be in bytes

# Define the position where you want to start replacing
# In the example, we want to replace starting from index 4
start_position = 4
length_to_replace = len(new_string)  # Length of the new string to replace

# Open the file in binary read and write mode
with open(file_path, 'rb+') as file:
    # Move the file cursor to the start position
    file.seek(start_position)

    # Read the file content from the start position
    original_bytes = file.read(length_to_replace)

    # Overwrite with the new bytes
    file.seek(start_position)  # Go back to the start position
    file.write(new_string)      # Write the new bytes

    print(f"Replaced bytes '{original_bytes}' with '{new_string}' at position {start_position}.")
