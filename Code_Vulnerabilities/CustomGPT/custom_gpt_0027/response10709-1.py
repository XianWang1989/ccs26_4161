
def replace_bytes_in_file(file_path, position, replacement):
    # Open the file in 'ab+' mode
    with open(file_path, 'r+b') as file:
        # Seek to the specified position
        file.seek(position[0])

        # Convert the replacement string to bytes
        replacement_bytes = replacement.encode('utf-8')

        # Write the replacement bytes
        file.write(replacement_bytes)

        # Optionally, if you need to fill the remaining space with bytes, you can do this:
        file.truncate(position[0] + len(replacement_bytes))

# File content: thisissomethingasperfectlygood.
# Replace 'issom' starting at position 4 with '01234'
replace_bytes_in_file('example.txt', (4, 0), '01234')
