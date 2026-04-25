
def replace_bytes_in_file(file_path, position, new_string):
    # Make sure the new string is in bytes
    new_bytes = new_string.encode('utf-8')

    # Open the file in read+write ('r+b') mode
    with open(file_path, 'r+b') as f:
        # Move the file cursor to the given position
        f.seek(position[0])  # Position is a tuple (start_position, length_of_substring)

        # Replace the bytes at the given position
        f.write(new_bytes)

# Example usage
file_path = 'example.txt'

# Create an example file with initial content
with open(file_path, 'w') as f:
    f.write("thisissomethingasperfectlygood.")

# Now replace the bytes
replace_bytes_in_file(file_path, (4, 4), '01234')

# Read back the file to see the changes
with open(file_path, 'r') as f:
    modified_content = f.read()

print(modified_content)
