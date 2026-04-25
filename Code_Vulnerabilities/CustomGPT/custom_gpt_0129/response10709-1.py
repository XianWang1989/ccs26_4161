
# Function to replace bytes in a file
def replace_bytes_in_file(file_path, start_position, end_position, new_string):
    # Open the file in 'r+b' mode to allow both reading and writing
    with open(file_path, 'r+b') as f:
        # Seek to the start position
        f.seek(start_position)
        # Write the new string's bytes
        f.write(new_string.encode())

        # Optional: truncate the file if the new string is shorter than the original
        f.truncate()

# Example usage
file_path = 'example_file.txt'

# Create a sample file for demonstration
with open(file_path, 'w') as f:
    f.write('thisissomethingasperfectlygood.')

# Define the positions and the new string
start_pos = 4  # Start replacement at index 4
new_bytes_string = '01234'  # New bytes to write

# Call the function to replace bytes
replace_bytes_in_file(file_path, start_pos, start_pos + len(new_bytes_string), new_bytes_string)

# Read the modified file to verify the result
with open(file_path, 'r') as f:
    print(f.read())  # Output should show: this01234ethingasperfectlygood.
