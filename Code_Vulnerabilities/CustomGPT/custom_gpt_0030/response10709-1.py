
def replace_bytes_in_file(file_path, position, new_string):
    # Open the file in append and binary mode
    with open(file_path, 'r+b') as file:
        # Move the cursor to the specified position
        file.seek(position[0])

        # Write the new string (as bytes)
        file.write(new_string.encode())

# Example usage
file_path = 'example.txt'

# Initial content
with open(file_path, 'w') as f:
    f.write("thisissomethingasperfectlygood.")

# Replace bytes at position (4, 0)
replace_bytes_in_file(file_path, (4, 0), "01234")

# Verify the result
with open(file_path, 'r') as f:
    print(f.read())
