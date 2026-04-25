
# Define the file name
file_name = 'example.txt'

# Your original content in the file will look like:
# thisissomethingasperfectlygood.

# The string you want to insert
new_bytes = b'01234'

# The position you want to replace (4, 0): 'issom'
# This means starting at position 4 in the file
start_position = 4

# Open the file in 'r+b' mode (read and write in binary mode)
with open(file_name, 'r+b') as file:
    # Move the cursor to the desired start position
    file.seek(start_position)

    # Read the part of the original string that you want to replace
    # This is important as you need to know how many bytes to overwrite
    original_bytes = file.read(5)  # Read 5 bytes for "issom"

    # Print out what is being replaced (optional)
    print(f'Replacing "{original_bytes.decode()}" with "{new_bytes.decode()}"')

    # Move back to the start position and replace it with the new bytes
    file.seek(start_position)
    file.write(new_bytes)

    # Optionally truncate the file to the new desired length if the replacement is shorter
    # Here we replace a 5-byte substring with another 5-byte substring
    # So truncating isn't necessary in this case, but if it were:
    # file.truncate()

# Print the updated content of the file to verify
with open(file_name, 'rb') as file:
    print(file.read().decode())  # Output should be: this01234ethingasperfectlygood.
